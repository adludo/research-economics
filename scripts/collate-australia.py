#!/usr/bin/env python3
"""Extract Australia data from pinned, checksum-checked public archives."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import urlopen
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/australia'

def rows(data, delimiter=','):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig')), delimiter=delimiter))

def write(name, data):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(data)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-cache', type=Path)
    args = p.parse_args()
    manifest = json.loads((OUT / 'sources.json').read_text())
    payload = {}
    for name, spec in manifest['sources'].items():
        b = (args.input_cache / name).read_bytes() if args.input_cache else urlopen(spec['url'], timeout=60).read()
        if hashlib.sha256(b).hexdigest() != spec['sha256']:
            raise ValueError('Checksum mismatch: ' + name)
        payload[name] = b
    persons = rows(payload['census-persons.tsv'], '\t')
    age = rows(payload['census-age.tsv'], '\t')
    families = rows(payload['census-families.tsv'], '\t')
    if (len(persons), len(age), len(families)) != (9, 99, 134):
        raise ValueError('Unexpected Census coverage')
    write('census-population.csv', [{'state': r['STE_NAME21'], 'persons': int(r['persons'])} for r in persons])
    bands = {'0-4': 'under_15', '5-14': 'under_15', '65-74': '65_plus', '75-84': '65_plus', '85+': '65_plus'}
    age_out, family_out = [], []
    for state in [r['STE_NAME21'] for r in persons]:
        a = {k: 0 for k in ('under_15', '15_to_64', '65_plus')}
        for r in age:
            if r['STE_NAME21'] == state:
                a[bands.get(r['Age'], '15_to_64')] += int(r['persons'])
        age_out.append({'state': state, **a, 'age_cell_total': sum(a.values())})
        for couple in ('0', '1'):
            count = sum(int(r['families']) for r in families if r['STE_NAME21'] == state and r['HasChild'] == '1' and r['CoupleFamily'] == couple)
            family_out.append({'state': state, 'family_type': 'couple' if couple == '1' else 'one_parent', 'families_with_under_15_children': count})
    write('census-age.csv', age_out)
    write('census-families.csv', family_out)
    for n in ('census-persons.tsv', 'census-age.tsv', 'census-families.tsv'):
        (OUT / n).write_bytes(payload[n])
    indicators = [n[:-4] for n in payload if n.endswith('.csv') and n != 'wdi-metadata.csv']
    wdi = []
    for k in indicators:
        data = [r for r in rows(payload[k + '.csv']) if r['economy'] == 'aus' and 2000 <= int(r['year']) <= 2025]
        if len(data) != 26 or len({r['year'] for r in data}) != 26:
            raise ValueError('Unexpected WDI coverage: ' + k)
        wdi.extend({'indicator': k, 'year': int(r['year']), 'value': r[k]} for r in data)
    write('annual-indicators.csv', sorted(wdi, key=lambda r: (r['indicator'], r['year'])))
    meta = [r for r in rows(payload['wdi-metadata.csv']) if r['concept'] in indicators]
    if len(meta) != 8:
        raise ValueError('Missing indicator metadata')
    (OUT / 'indicator-metadata.json').write_text(json.dumps(meta, indent=2) + '\n')
    ws = openpyxl.load_workbook(io.BytesIO(payload['industry-employment.xlsx']), data_only=True)['Data1']
    values = list(ws.values)
    employment, metadata = [], []
    for j in range(1, ws.max_column):
        if values[2][j] != 'Seasonally Adjusted':
            continue
        if values[1][j] != '000' or values[4][j] != 'Quarter':
            raise ValueError('Unexpected employment unit/frequency')
        label = values[0][j].split(';')[0].strip()
        series = values[9][j]
        observations = [(r[0], r[j]) for r in values[10:] if r[j] is not None]
        if len(observations) != 163 or observations[-1][0].strftime('%Y-%m-%d') != '2025-05-01':
            raise ValueError('Unexpected employment coverage')
        metadata.append({'series_id': series, 'label': label, 'header': values[0][j], 'unit': 'thousands of employed persons', 'series_type': values[2][j], 'data_type': values[3][j], 'frequency': values[4][j], 'collection_month': values[5][j], 'observations': len(observations)})
        employment.extend({'date': d.strftime('%Y-%m-%d'), 'series_id': series, 'industry': label, 'employed_thousands': v} for d, v in observations)
    if len(metadata) != 20:
        raise ValueError('Expected 19 industries and separately adjusted total')
    write('industry-employment.csv', employment)
    (OUT / 'employment-metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
    (OUT / 'coverage.json').write_text(json.dumps({'census_geographies': 9, 'census_age_cells': 99, 'family_groups': len(family_out), 'annual_indicators': 8, 'annual_rows': len(wdi), 'annual_years': [2000, 2025], 'employment_series': len(metadata), 'employment_rows': len(employment), 'employment_period': ['1984-11-01', '2025-05-01']}, indent=2) + '\n')
    print((OUT / 'coverage.json').read_text())

if __name__ == '__main__':
    main()
