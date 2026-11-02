#!/usr/bin/env python3
"""Fetch frozen aggregates and build explicit leisure/productivity/export panels."""
import csv, hashlib, io, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/topic-graphs'
SOURCES = {
  "us.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/A%20Century%20of%20Work%20and%20Leisure%20-%20Ramey%20and%20Francis%20%282009%29/A%20Century%20of%20Work%20and%20Leisure%20-%20Ramey%20and%20Francis%20%282009%29.csv",
    "sha256": "d0ea41541b2d98a3c85545e68e920ada3e320ddb6314a56ca5efd5bc0b960c21"
  },
  "us.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/A%20Century%20of%20Work%20and%20Leisure%20-%20Ramey%20and%20Francis%20%282009%29/datapackage.json",
    "sha256": "b1b79d00d180b0197daa2d342226218d3c184f5c9cebad0c89460e5923cbdad7"
  },
  "norway.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Long%20run%20time%20use%20in%20Norway%2C%20by%20sex%20-%20Norway%20Statistics/Long%20run%20time%20use%20in%20Norway%2C%20by%20sex%20-%20Norway%20Statistics.csv",
    "sha256": "634814fabcf8b666e93d56d4245e807c328dcec38cdb9a7c066c1eb22fb8a2b4"
  },
  "norway.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Long%20run%20time%20use%20in%20Norway%2C%20by%20sex%20-%20Norway%20Statistics/datapackage.json",
    "sha256": "6049dc776561f0f6a1d1dc0e16a933f8439c923d059896b0a841d197b53a8b68"
  },
  "trade.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Total%20value%20of%20exports%20by%20country%20to%20world%20%28%25GDP%29%20%28OWID%20calculations%20based%20on%20Fouquin%20and%20Hugot%20%28CEP/Total%20value%20of%20exports%20by%20country%20to%20world%20%28%25GDP%29%20%28OWID%20calculations%20based%20on%20Fouquin%20and%20Hugot%20%28CEP.csv",
    "sha256": "ffe93173136819da4295f3c76ed66487bfed1aae04dd2ccc0306f0828cec46d9"
  },
  "trade.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Total%20value%20of%20exports%20by%20country%20to%20world%20%28%25GDP%29%20%28OWID%20calculations%20based%20on%20Fouquin%20and%20Hugot%20%28CEP/datapackage.json",
    "sha256": "4dd22859e32522ee70ecd1da41db091c21ace1078914ee38df48d5ebeb519357"
  },
  "pwt.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/Penn%20World%20Table%20version%2010.0.csv",
    "sha256": "0ecd5c71e0f1dfdbeecd624f7c61875b5fa64094e639cccf6304b2fd181be505"
  },
  "pwt.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/datapackage.json",
    "sha256": "79bcd8893b84bbdc00cea3465c7d1710301de364b526a4d139e2d8469e4d1a57"
  }
}
TRADE_COUNTRIES = ['Australia','United States','United Kingdom','France','Japan','China','India','Brazil']
US_GROUPS = ['Ages 14+ (total)','Ages 14-17 (total)','Ages 18-24 (total)','Ages 25-54 (total)','Ages 55-64 (total)','Ages 65+ (total)']

def write(name, rows):
    if not rows: raise ValueError('Empty output '+name)
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    data={};OUT.mkdir(parents=True,exist_ok=True)
    for k,s in SOURCES.items():
        b=urlopen(s['url'],timeout=60).read()
        if hashlib.sha256(b).hexdigest()!=s['sha256']:raise ValueError('Checksum '+k)
        if k.endswith('.csv'):
            rows=list(csv.DictReader(io.StringIO(b.decode('utf-8-sig'))))
            keys=[(r['Entity'],r['Year']) for r in rows]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate key '+k)
            data[k]=rows
        else:(OUT/k).write_bytes(b)
    us=[];key=next(k for k in data['us.csv'][0] if k.startswith('Average weekly leisure'))
    for r in data['us.csv']:
        if r['Entity'] in US_GROUPS and r[key]:us.append({'group':r['Entity'],'year':int(r['Year']),'leisure_hours_week':float(r[key])})
    norway=[]
    for r in data['norway.csv']:
        for sex in ['all','female','male']:
            k=f'Time spent on leisure, {sex} (Statistics Norway)'
            if r[k]:norway.append({'country':r['Entity'],'sex':sex,'year':int(r['Year']),'leisure_minutes_day':float(r[k])})
    pwt={(r['Entity'],int(r['Year'])):r for r in data['pwt.csv']}
    def measures(country,year):
        r=pwt.get((country,year))
        fields=['GDP (output, multiple price benchmarks)','GDP (expenditure, multiple price benchmarks)','Population','Number of people in work','Annual working hours per worker']
        if not r or not all(r[k] for k in fields):return None
        output,expenditure,pop,workers,hours=[float(r[k]) for k in fields]
        if min(output,expenditure,pop,workers,hours)<=0:raise ValueError('Nonpositive macro value')
        return output/(workers*hours),expenditure/pop
    linked=[]
    for r in norway:
        if r['sex']!='all':continue
        m=measures('Norway',r['year'])
        if m:linked.append({'country':'Norway','year':r['year'],'leisure':r['leisure_minutes_day'],'leisure_unit':'minutes/day, national all-sex series','output_per_hour_2017_ppp':m[0]})
    for r in us:
        if r['group']!='Ages 14+ (total)':continue
        m=measures('United States',r['year'])
        if m:linked.append({'country':'United States','year':r['year'],'leisure':r['leisure_hours_week'],'leisure_unit':'hours/week, age14+ residual estimate','output_per_hour_2017_ppp':m[0]})
    trade=[];key=next(k for k in data['trade.csv'][0] if k not in ('Entity','Year'))
    for r in data['trade.csv']:
        year=int(r['Year']);country=r['Entity']
        if country not in TRADE_COUNTRIES or not 1970<=year<=2014 or not r[key]:continue
        m=measures(country,year)
        if m:trade.append({'country':country,'year':year,'merchandise_exports_pct_gdp':float(r[key]),'gdp_per_person_2017_ppp':m[1]})
    us.sort(key=lambda r:(r['group'],r['year']));norway.sort(key=lambda r:(r['sex'],r['year']));linked.sort(key=lambda r:(r['country'],r['year']));trade.sort(key=lambda r:(r['country'],r['year']))
    for n,r in [('us-leisure.csv',us),('norway-leisure.csv',norway),('leisure-productivity.csv',linked),('trade-income.csv',trade)]:write(n,r)
    provenance={'retrieved_date_utc':datetime.now(timezone.utc).date().isoformat(),'sources':SOURCES,'counts':{'us_leisure':len(us),'norway_leisure':len(norway),'leisure_productivity':len(linked),'trade_income':len(trade)},'transformations':['Exact year matches only; no filling/interpolation or country aliases','US leisure copied only for declared six total-sex age groups; no reconstruction added','Norway all/female/male leisure minutes copied unchanged; archive normalization retained','Output/hour = output-side real GDP / (persons engaged × annual hours); GDP/person = expenditure-side real GDP / population; archive inputs use absolute dollar/person units','Export/GDP percentage copied as supplied; its documentation defines exports despite broader column label; not recomputed with PPP GDP'],'pwt_vintage':'Archive folder/metadata say10.0; earlier matched data and these macro definitions are cross-checked against CRAN10.01; original-provider identity not established','limits':['Not causal estimates or replications of paper models','US residual and Norway daily leisure definitions/populations are incompatible; not pooled','Norway age coverage not specified in archived metadata','Published archive normalization and historical assumptions not independently validated','Exports measure excludes services and is not policy openness; no inference of autarky','Original providers/revisions/reuse conditions and live deployment remain separate checks']}
    (OUT/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n');print(provenance['counts'])
if __name__=='__main__':main()
