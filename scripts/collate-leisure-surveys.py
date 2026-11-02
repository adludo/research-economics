#!/usr/bin/env python3
"""Extract illustrative leisure-survey series from pinned public archives."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/leisure-surveys'
COMPANY = ['alone', 'children', 'coworkers', 'family', 'friends', 'partner']


def rows(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'))))


def number(value):
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise ValueError(f'Invalid nonnegative value: {value}')
    return result


def write(name, fields, data):
    keys = [tuple(r.get(k) for k in fields[:-1]) for r in data]
    if len(set(keys)) != len(keys):
        raise ValueError(f'Duplicate extracted key: {name}')
    with (OUT / name).open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-cache', type=Path)
    args = parser.parse_args()
    manifest = json.loads((OUT / 'sources.json').read_text())
    inputs = {}
    for name, source in manifest['sources'].items():
        if args.input_cache:
            data = (args.input_cache / name).read_bytes()
        else:
            with urlopen(source['url'], timeout=60) as response:
                data = response.read()
        if hashlib.sha256(data).hexdigest() != source['sha256']:
            raise ValueError(f'Checksum mismatch: {name}')
        inputs[name] = data
    for name, data in inputs.items():
        if name.endswith('.json'):
            (OUT / name).write_bytes(data)
    atus = []
    for row in rows(inputs['atus.csv']):
        if row['Entity'] != 'United States':
            raise ValueError('Unexpected ATUS entity')
        # The archive's Year field encodes respondent AGE, not calendar year.
        age = int(row['Year'])
        if not 15 <= age <= 85:
            raise ValueError('Unexpected respondent age')
        for company in COMPANY:
            field = ('Time spent alone' if company == 'alone' else f'Time spent with {company}')
            field += ', by age of respondent (United States)'
            atus.append({'age': age, 'company': company, 'minutes_per_day': number(row[field])})
    write('atus-social-time.csv', ['age', 'company', 'minutes_per_day'], atus)
    mtus = [{'country': r['Entity'], 'survey_year': int(r['Year']),
             'reported_activity_fields': sum(bool(v.strip()) for k, v in r.items() if k not in ('Entity', 'Year'))}
            for r in rows(inputs['mtus.csv'])]
    write('mtus-coverage.csv', ['country', 'survey_year', 'reported_activity_fields'], mtus)
    field = 'Time spent on leisure, social, and associative life (Eurostat)'
    hetus = [{'country': r['Entity'], 'wave_label': int(r['Year']),
              'leisure_minutes_per_day': number(r[field])} for r in rows(inputs['hetus.csv']) if r[field].strip()]
    write('hetus-leisure.csv', ['country', 'wave_label', 'leisure_minutes_per_day'], hetus)
    finland = []
    for row in rows(inputs['finland.csv']):
        if row['Entity'] == 'Free time':
            for sex in ['all', 'men', 'women']:
                finland.append({'year': int(row['Year']), 'sex': sex,
                                'free_time_minutes_per_day': number(row[f'Time allocation, {sex} (Statistics Finland)'])})
    write('finland-free-time.csv', ['year', 'sex', 'free_time_minutes_per_day'], finland)
    historical = []
    for row in rows(inputs['historical.csv']):
        for measure in range(1, 5):
            if row['Entity'] == f'Leisure Measure {measure} (All individuals)':
                historical.append({'measure': measure, 'year': int(row['Year']),
                                   'hours_per_week': number(row['Hours per week spent in leisure (Aguiar and Hurst (2006))'])})
    write('historical-definitions.csv', ['measure', 'year', 'hours_per_week'], historical)
    coverage = {'atus_age_company_rows': len(atus), 'atus_ages': len({r['age'] for r in atus}),
                'mtus_country_years': len(mtus), 'mtus_countries': len({r['country'] for r in mtus}),
                'hetus_country_waves': len(hetus), 'hetus_countries': len({r['country'] for r in hetus}),
                'finland_sex_years': len(finland), 'historical_measure_years': len(historical)}
    provenance = {**manifest, 'coverage': coverage,
        'transformations': {
            'atus': 'Copy six reported company categories; relabel Year as respondent age. Values are pooled 2009–2019, not annual or longitudinal observations. Do not sum overlapping company categories or call them leisure-only time.',
            'mtus': 'Only country-year coverage and number of nonempty activity fields; do not aggregate processed conditional activity means. A dot identifies an archive row, not a complete population leisure estimate.',
            'hetus': 'Copy population Time spent on leisure/social/associative life; do not select Participation time/rate. Year is retained as wave label, not verified fieldwork year. Preserve archive normalization.',
            'finland': 'Copy Free time for all/men/women; years are archive labels. No renormalization. Age coverage not established in archive metadata.',
            'historical': 'Copy four All individuals leisure definitions. OWID attributes to Aguiar–Hurst2006 working paper, not a current AHTUS extract or a replication of the final2007 paper.',
            'diagrams': 'Authored conceptual guides only; no AHTUS or OECD empirical numerical extract downloaded.'},
        'limits': ['Archived releases, not current provider estimates.', 'Original data/provider definitions and reuse terms remain unverified where access is blocked.',
                   'No interpolation, averaging, weighting, imputation, or causal inference added by this project.',
                   'AHTUS/OECD diagram semantics are reading aids, not verified release-specific processing or category definitions.',
                   'Country and wave population definitions differ; do not pool these measures or infer a global leisure ranking.']}
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    print(json.dumps(coverage))


if __name__ == '__main__':
    main()
