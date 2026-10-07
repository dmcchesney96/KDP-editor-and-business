#!/usr/bin/env python3
"""Read-only local package validation; does not authorize or perform KDP writes."""
import argparse, hashlib, json, sys
from pathlib import Path
import fitz

def validate(manifest_path):
    root=Path(manifest_path).resolve().parent
    m=json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    failures=[]; warnings=[]; checks=[]
    def check(ok,label):
        checks.append({'check':label,'status':'PASS' if ok else 'FAIL'})
        if not ok:failures.append(label)
    check(m.get('schema_version')==1,'manifest schema version')
    meta=m.get('metadata',{}); p=m.get('print',{})
    check(bool(meta.get('title','').strip()),'title supplied')
    if not meta.get('author'):warnings.append('Public author unresolved: required before completing KDP details/publication.')
    kws=meta.get('keywords',[])
    check(isinstance(kws,list) and 0<len(kws)<=7 and all(isinstance(k,str) and k.strip() for k in kws),'one to seven nonempty keyword candidates')
    check(len(kws)==len(set(kws)),'keyword candidates unique')
    files=m.get('files',[])
    for role in ['interior','cover']:
        selected=[f for f in files if f.get('role')==role]
        check(len(selected)==1,role+' file role uniquely identified')
        if len(selected)!=1:continue
        item=selected[0]; path=root/item['path']
        check(path.is_file(),role+' file exists')
        if not path.is_file():continue
        check(hashlib.sha256(path.read_bytes()).hexdigest()==item.get('sha256'),role+' SHA-256 matches')
        try:d=fitz.open(path)
        except Exception as e:check(False,role+' PDF readable: '+str(e));continue
        check(not d.needs_pass,role+' PDF unencrypted')
        if d.needs_pass:continue
        expected=int(p['interior_pages']) if role=='interior' else 1
        dims=p['trim_inches'] if role=='interior' else p['cover_inches']
        check(len(d)==expected,role+' page count')
        check(all(abs(pg.rect.width-dims[0]*72)<.03 and abs(pg.rect.height-dims[1]*72)<.03 for pg in d),role+' page dimensions')
        fontx={f[0] for pg in d for f in pg.get_fonts(full=True)}
        embedded=True
        for x in fontx:
            try:
                if not d.extract_font(x)[3]:embedded=False
            except Exception:embedded=False
        check(embedded,role+' referenced fonts embedded')
        check(all(pg.get_text().strip() or pg.get_images() or pg.get_drawings() for pg in d),role+' no empty pages detected')
    warnings.append('Local checks do not certify margins, image DPI, barcode, editorial/rights quality, KDP Previewer, or physical proof.')
    return {'local_file_verdict':'PASS' if not failures else 'FAIL','checks':checks,'failures':failures,'warnings':warnings}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('manifest');a=ap.parse_args()
    try:r=validate(a.manifest)
    except Exception as e:r={'local_file_verdict':'FAIL','failures':[str(e)]}
    print(json.dumps(r,indent=2));sys.exit(0 if r['local_file_verdict']=='PASS' else 1)
