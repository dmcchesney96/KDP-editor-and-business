# Canonical Ads CSV

Required UTF-8 columns: `search_term,impressions,clicks,orders,sales,spend,currency`. Each row is a mutually exclusive reporting cell from one title/marketplace/window. Numeric values are nonnegative, without currency symbols or thousands separators. `currency` is an ISO code such as USD. Preserve source rows; do not insert made-up zero rows into real reports.

Map the export's exact column names and attribution horizon into this schema. Record whether `orders` means purchases or units; estimated unit-royalty contribution is valid only if `orders` represents one copy per order or after an explicit unit mapping. The script reports an order-based approximation. For multi-unit orders use verified attributed units and document the change.

CTR=clicks/impressions; attributed-order rate=orders/clicks; CPC=spend/clicks; ACoS=spend/sales; cost/order=spend/orders; estimated royalty contribution=orders×supplied unit royalty−spend. Zero denominators yield null, not zero. Totals use summed numerators/denominators. Negative/invalid values and mixed currencies fail rather than disappear. A nonzero order/revenue/spend row with no clicks can reflect attribution timing; inspect the source instead of silently repairing it.

KDP data stays separate with ASIN, marketplace, currency, period, units, refunds, and royalties. TACoS requires aligned total revenue, not estimated royalties. Ordinary KDP reports do not reveal organic conversion.
