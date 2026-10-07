#!/usr/bin/env python3
"""Summarize one normalized actual Ads export; no network or account writes."""
import argparse, csv, json, math
from collections import defaultdict

FIELDS=('impressions','clicks','orders','sales','spend')
def div(a,b):return a/b if b else None
def metrics(d,royalty):
    out=dict(d)
    out.update(ctr=div(d['clicks'],d['impressions']),
        attributed_order_rate=div(d['orders'],d['clicks']),
        cpc=div(d['spend'],d['clicks']),acos=div(d['spend'],d['sales']),
        cost_per_order=div(d['spend'],d['orders']),
        estimated_royalty_contribution=d['orders']*royalty-d['spend'])
    return out
def summarize(path,currency,royalty):
    if not math.isfinite(royalty) or royalty<0:raise ValueError('Unit royalty must be finite and nonnegative')
    terms=defaultdict(lambda:{f:0.0 for f in FIELDS});warnings=[];count=0
    with open(path,encoding='utf-8-sig',newline='') as fh:
        reader=csv.DictReader(fh)
        required=set(FIELDS)|{'currency','search_term'}
        if not required.issubset(reader.fieldnames or []):raise ValueError('Missing canonical columns: '+str(required-set(reader.fieldnames or [])))
        for n,row in enumerate(reader,2):
            if row['currency'].strip()!=currency:raise ValueError('Currency mismatch on row '+str(n))
            term=row['search_term'].strip()
            if not term:raise ValueError('Missing search term on row '+str(n))
            vals={f:float(row[f]) for f in FIELDS}
            if any(not math.isfinite(x) or x<0 for x in vals.values()):raise ValueError('Invalid/negative number on row '+str(n))
            if vals['clicks']==0 and (vals['orders'] or vals['sales'] or vals['spend']):warnings.append('Inspect attribution/timing on row '+str(n)+': activity with zero clicks.')
            for f in FIELDS:terms[term][f]+=vals[f]
            count+=1
    total={f:sum(d[f] for d in terms.values()) for f in FIELDS}
    return {'currency':currency,'rows':count,'unit_royalty_assumption':royalty,
        'totals':metrics(total,royalty),'search_terms':{t:metrics(d,royalty) for t,d in terms.items()},
        'warnings':warnings+['Order-based royalty estimate assumes one copy per attributed order; not audited profit.',
        'These are ad metrics only; no organic traffic or keyword search volume is inferred.']}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('csv');ap.add_argument('--currency',required=True);ap.add_argument('--royalty-per-unit',type=float,required=True);a=ap.parse_args()
    try:print(json.dumps(summarize(a.csv,a.currency,a.royalty_per_unit),indent=2,allow_nan=False))
    except (ValueError,KeyError) as e:ap.error(str(e))
