#!/usr/bin/env python3
"""Build separate recent-data panels from checksum-pinned WDI and ILO mirrors."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/recent-economy'
COUNTRIES = {'aus': 'Australia', 'usa': 'United States', 'gbr': 'United Kingdom',
             'fra': 'France', 'deu': 'Germany', 'jpn': 'Japan', 'kor': 'South Korea',
             'chn': 'China', 'ind': 'India', 'bra': 'Brazil', 'mex': 'Mexico',
             'zaf': 'South Africa'}
FIRST, LAST = 1990, 2024
HOURS_FIRST = 2000
TFR = 'sp_dyn_tfrt_in'
GDP = 'ny_gdp_pcap_pp_kd'
HOURS = 'how_temp_sex_eco_nb'


def table(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'))))


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f'Nonpositive or nonfinite source value: {value}')
    return number


def keyed(rows, field, code_field, year_field):
    result = {}
    for row in rows:
        code, year = row[code_field], int(row[year_field])
        if code not in COUNTRIES or not FIRST <= year <= LAST:
            continue
        key = code, year
        if key in result:
            raise ValueError(f'Duplicate source key: {key}')
        result[key] = positive(row[field])
    return result


def write_csv(name, fields, rows):
    with (OUT / name).open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-cache', type=Path,
                        help='Read checksum-verified input files from this directory instead of downloading.')
    args = parser.parse_args()
    manifest = json.loads((OUT / 'sources.json').read_text())
    payloads = {}
    for name, spec in manifest['sources'].items():
        if args.input_cache:
            data = (args.input_cache / name).read_bytes()
        else:
            with urlopen(spec['url'], timeout=60) as response:
                data = response.read()
        if hashlib.sha256(data).hexdigest() != spec['sha256']:
            raise ValueError(f'Checksum mismatch: {name}')
        payloads[name] = data
    fertility = keyed(table(payloads['fertility.csv']), TFR, 'economy', 'year')
    gdp = keyed(table(payloads['gdp.csv']), GDP, 'economy', 'year')
    hours = {}
    for code in COUNTRIES:
        rows = [r for r in table(payloads[f'hours-{code}.csv'])
                if r['sex'] == 'sex_t' and r['classif1'] == 'eco_aggregate_total']
        if any(r['ref_area'] != code for r in rows):
            raise ValueError('Country differs from filename')
        hours.update(keyed(rows, HOURS, 'ref_area', 'time'))
    country_rows, income_rows, hours_rows, coverage = [], [], [], []
    recent_codes = [c for c in COUNTRIES if (c, LAST) in hours]
    for code, country in COUNTRIES.items():
        for year in range(FIRST, LAST + 1):
            key = code, year
            row = {'code': code, 'country': country, 'year': year,
                   'tfr_births_per_woman': fertility.get(key, ''),
                   'gdp_per_person_2021_ppp': gdp.get(key, ''),
                   'weekly_hours_per_employed_person': hours.get(key, '') if year >= HOURS_FIRST else ''}
            country_rows.append(row)
            if key in fertility and key in gdp:
                income_rows.append({k: row[k] for k in
                                    ['code', 'country', 'year', 'tfr_births_per_woman', 'gdp_per_person_2021_ppp']})
            if code in recent_codes and year >= HOURS_FIRST and key in fertility and key in hours:
                hours_rows.append({k: row[k] for k in
                                   ['code', 'country', 'year', 'tfr_births_per_woman', 'weekly_hours_per_employed_person']})
        h = sorted(y for c, y in hours if c == code and y >= HOURS_FIRST)
        pairs = [r for r in income_rows if r['code'] == code]
        coverage.append({'code': code, 'country': country,
                         'gdp_tfr_first': pairs[0]['year'], 'gdp_tfr_last': pairs[-1]['year'],
                         'gdp_tfr_years': len(pairs), 'hours_first': h[0], 'hours_last': h[-1],
                         'hours_years': len(h), 'hours_at_last_year': hours[(code, h[-1])],
                         'hours_plot_included': code in recent_codes})
    write_csv('country-years.csv', list(country_rows[0]), country_rows)
    write_csv('fertility-gdp.csv', list(income_rows[0]), income_rows)
    write_csv('fertility-hours.csv', list(hours_rows[0]), hours_rows)
    write_csv('coverage.csv', list(coverage[0]), coverage)
    wdi_metadata = [r for r in table(payloads['wdi-metadata.csv']) if r['concept'] in (TFR, GDP)]
    ilo_metadata = [r for r in table(payloads['ilo-metadata.csv']) if r['concept'] == HOURS]
    entities = [r for r in table(payloads['wdi-entities.csv']) if r['country'] in COUNTRIES]
    if len(wdi_metadata) != 2 or len(ilo_metadata) != 1 or len(entities) != len(COUNTRIES):
        raise ValueError('Missing metadata or country definitions')
    (OUT / 'indicator-metadata.json').write_text(json.dumps(
        {'wdi': wdi_metadata, 'ilo': ilo_metadata, 'wdi_country_labels': entities,
         'ilo_sex': [r for r in table(payloads['ilo-sex.csv']) if r['sex'] == 'sex_t'],
         'ilo_sector': [r for r in table(payloads['ilo-sector.csv']) if r['classif1'] == 'eco_aggregate_total']}, indent=2) + '\n')
    provenance = {
        **manifest, 'period': [FIRST, LAST], 'hours_period': [HOURS_FIRST, LAST],
        'selection': COUNTRIES, 'recent_hours_codes': recent_codes,
        'source_revisions': {'wdi': '4252d91d988efc0f116d4fa48e92357b778729e5 (2026-10-14)',
                             'ilo': 'c4dd68c687df8162835e1684cffec8723b19eee8 (2026-02-27)'},
        'coverage': {'country_year_rows': len(country_rows), 'fertility_gdp_pairs': len(income_rows),
                     'fertility_hours_pairs': len(hours_rows), 'recent_hours_countries': len(recent_codes)},
        'join': 'Exact lowercase country code + calendar year. Separate pairwise joins; GDP does not require hours.',
        'transformations': ['Copy published values; retain floating-point precision.',
                            '1990–2024 for GDP/fertility; 2000–2024 for weekly hours.',
                            'ILO SEX_T (total sex) and ECO_AGGREGATE_TOTAL (all economic activities).',
                            'Hours graphs select original countries with a 2024 hours value.',
                            'Missing values left empty; no interpolation, extrapolation, averaging, or weighting added.',
                            'Do not multiply weekly hours by 52 or splice with PWT annual hours.'],
        'limits': ['WDI includes statistical estimates and interpolated/extrapolated fertility; exact WPP vintage and row flags absent.',
                   'ILO mirror selects one source per country using metadata ordering, then note_source ordering; original flags and source IDs are discarded.',
                   'Country survey definitions, age coverage and series breaks not harmonized by this project.',
                   '2024 cutoff excludes later rows but does not establish that every included figure is directly measured or forecast-free.',
                   'Original-provider API/file agreement and current revisions unverified due network restrictions.',
                   'GDP/person is not productivity; market hours are not leisure; associations are not causal.']}
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    page = ROOT / 'src/content/docs/data/recent-fertility-hours.md'
    if page.exists():
        content = '| Country | GDP + fertility years | Weekly-hours years (count) | Latest weekly hours | In recent hours graphs? |\n'
        content += '| --- | --- | --- | ---: | --- |\n'
        for row in coverage:
            content += (f"| {row['country']} | {row['gdp_tfr_first']}–{row['gdp_tfr_last']} ({row['gdp_tfr_years']}) | "
                        f"{row['hours_first']}–{row['hours_last']} ({row['hours_years']}) | "
                        f"{row['hours_at_last_year']:.2f} ({row['hours_last']}) | {'Yes' if row['hours_plot_included'] else 'No'} |\n")
        text = page.read_text()
        before, rest = text.split('<!-- BEGIN COVERAGE -->')
        _, after = rest.split('<!-- END COVERAGE -->')
        page.write_text(before + '<!-- BEGIN COVERAGE -->\n' + content + '<!-- END COVERAGE -->' + after)
    print(json.dumps(provenance['coverage']))


if __name__ == '__main__':
    main()
