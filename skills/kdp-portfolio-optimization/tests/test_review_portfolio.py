"""Regression checks for evidence/denominator safety."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "review_portfolio.py"
spec = importlib.util.spec_from_file_location("review_portfolio", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PortfolioReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.catalog = self.base / "catalog.json"
        self.catalog.write_text(json.dumps({"books": [
            {"id": "one", "working_title": "Book One", "marketplace": "Amazon.com",
             "format": "paperback", "status": "live", "first_live_date": None},
            {"id": "two", "working_title": "Book Two", "marketplace": "Amazon.com",
             "format": "paperback", "status": "in_review", "first_live_date": None}
        ]}), encoding="utf-8")

    def csv(self, name, content):
        path = self.base / name
        path.write_text(content, encoding="utf-8")
        return str(path)

    def run_review(self, **kwargs):
        return module.analyze(str(self.catalog), "2026-10-08", **kwargs)

    def test_no_export_means_unknown_not_zero(self):
        result = self.run_review()
        self.assertIsNone(result["books"][0]["kdp_paid_processed_units"])
        self.assertIsNone(result["books"][0]["ads"])
        self.assertEqual(result["books"][0]["diagnosis"], "INSUFFICIENT_ACCOUNT_DATA")
        self.assertEqual(result["books"][1]["diagnosis"], "PENDING_REVIEW")
        self.assertIn("unknown", module.render_markdown(result))

    def test_empty_complete_export_proves_processed_zero_only_with_scope(self):
        path = self.csv("orders.csv", "date,book_id,marketplace,paid_units,free_units\n")
        result = self.run_review(orders_path=path, orders_start="2026-10-01",
                                 orders_end="2026-10-08", orders_complete=True,
                                 orders_marketplace="Amazon.com", orders_format="paperback")
        self.assertEqual(result["books"][0]["kdp_paid_processed_units"], 0)
        self.assertEqual(result["books"][0]["diagnosis"], "NO_CONFIRMED_PRINT_SHIPMENTS")
        self.assertEqual(result["books"][1]["diagnosis"], "PENDING_REVIEW")

    def test_empty_incomplete_export_does_not_prove_zero(self):
        path = self.csv("orders.csv", "date,book_id,marketplace,paid_units,free_units\n")
        result = self.run_review(orders_path=path, orders_start="2026-10-01", orders_end="2026-10-08")
        self.assertIsNone(result["books"][0]["kdp_paid_processed_units"])

    def test_aggregate_kdp_positive(self):
        path = self.csv("orders.csv",
                        "date,book_id,marketplace,paid_units,free_units\n"
                        "2026-10-07,one,Amazon.com,2,0\n"
                        "2026-10-08,one,Amazon.com,1,0\n")
        result = self.run_review(orders_path=path, orders_start="2026-10-01", orders_end="2026-10-08")
        self.assertEqual(result["books"][0]["kdp_paid_processed_units"], 3)
        self.assertEqual(result["books"][0]["diagnosis"], "MEASURABLE_TRACTION")
        self.assertIsNone(result["books"][1]["kdp_paid_processed_units"])

    def test_weighted_ads_rates_and_no_double_count(self):
        path = self.csv("ads.csv",
                        "date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend\n"
                        "2026-10-06,one,Amazon.com,USD,100,1,0,0,0.50\n"
                        "2026-10-07,one,Amazon.com,USD,10,9,1,10,3.00\n")
        result = self.run_review(ads_path=path, ads_type="advertised_product", attribution_window="14d")
        ads = result["books"][0]["ads"]
        self.assertEqual(ads["impressions"], 110)
        self.assertEqual(ads["clicks"], 10)
        self.assertAlmostEqual(ads["ad_ctr"], 10 / 110, places=6)
        self.assertAlmostEqual(ads["ad_acos"], 0.35, places=6)
        self.assertIsNone(result["books"][0]["kdp_paid_processed_units"])

    def test_search_terms_not_full_ads_diagnostic(self):
        path = self.csv("terms.csv",
                        "date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend,search_term\n"
                        "2026-10-07,one,Amazon.com,USD,1000,1,0,0,0.40,scripture journal\n")
        result = self.run_review(ads_path=path, ads_type="search_terms", attribution_window="14d")
        self.assertEqual(result["books"][0]["ads"]["top_clicked_terms"][0]["term"], "scripture journal")
        self.assertEqual(result["books"][0]["diagnosis"], "INSUFFICIENT_ACCOUNT_DATA")

    def test_reject_negative_units(self):
        path = self.csv("orders.csv",
                        "date,book_id,marketplace,paid_units,free_units\n"
                        "2026-10-07,one,Amazon.com,-1,0\n")
        with self.assertRaises(module.DataError):
            self.run_review(orders_path=path, orders_start="2026-10-01", orders_end="2026-10-08")

    def test_reject_future_rows(self):
        path = self.csv("orders.csv",
                        "date,book_id,marketplace,paid_units,free_units\n"
                        "2026-10-09,one,Amazon.com,1,0\n")
        with self.assertRaises(module.DataError):
            self.run_review(orders_path=path, orders_start="2026-10-01", orders_end="2026-10-08")

    def test_reject_mixed_currency(self):
        path = self.csv("ads.csv",
                        "date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend\n"
                        "2026-10-06,one,Amazon.com,USD,10,1,0,0,0.40\n"
                        "2026-10-07,one,Amazon.com,CAD,10,1,0,0,0.40\n")
        with self.assertRaises(module.DataError):
            self.run_review(ads_path=path, ads_type="advertised_product", attribution_window="14d")

    def test_reject_mixed_marketplaces(self):
        path = self.csv("orders.csv",
                        "date,book_id,marketplace,paid_units,free_units\n"
                        "2026-10-07,one,Amazon.co.uk,1,0\n")
        with self.assertRaises(module.DataError):
            self.run_review(orders_path=path, orders_start="2026-10-01", orders_end="2026-10-08")

    def test_reject_ads_without_report_type(self):
        path = self.csv("ads.csv",
                        "date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend\n")
        with self.assertRaises(module.DataError):
            self.run_review(ads_path=path, attribution_window="14d")

    def test_reject_false_complete_scope(self):
        path = self.csv("orders.csv", "date,book_id,marketplace,paid_units,free_units\n")
        with self.assertRaises(module.DataError):
            self.run_review(orders_path=path, orders_complete=True)

    def test_denom_zero_is_null(self):
        path = self.csv("ads.csv",
                        "date,book_id,marketplace,currency,impressions,clicks,orders,sales,spend\n"
                        "2026-10-07,one,Amazon.com,USD,0,0,0,0,0\n")
        result = self.run_review(ads_path=path, ads_type="advertised_product", attribution_window="14d")
        self.assertIsNone(result["books"][0]["ads"]["ad_ctr"])
        self.assertIsNone(result["books"][0]["ads"]["ad_cpc"])
        self.assertIsNone(result["books"][0]["ads"]["ad_acos"])


if __name__ == "__main__":
    unittest.main()
