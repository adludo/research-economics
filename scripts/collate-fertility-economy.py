#!/usr/bin/env python3
"""Rebuild a same-year TFR/GDP/hours panel from checksum-pinned public archives."""
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/fertility-economy'
FIRST_YEAR, LAST_YEAR = 1970, 2014  # Gapminder v12 marks 2015 onward as forecasts.
COUNTRIES = ['Australia', 'United States', 'United Kingdom', 'France', 'Germany',
             'Japan', 'South Korea', 'China', 'India', 'Brazil', 'Mexico', 'South Africa']
SOURCES = {
  "gapminder.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Fertility%20rate%20%28Complete%20Gapminder%2C%20v12%29%20%282017%29/Fertility%20rate%20%28Complete%20Gapminder%2C%20v12%29%20%282017%29.csv",
    "sha256": "75495635c5dd08d7b7df7f192b0567f9f917eafbce45084ea9a73ee81de45527"
  },
  "gapminder.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Fertility%20rate%20%28Complete%20Gapminder%2C%20v12%29%20%282017%29/datapackage.json",
    "sha256": "b07f8bcb818f6973ff74314200728dde2d941f88bd569a91b051396826bd84c8"
  },
  "pwt.csv": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/Penn%20World%20Table%20version%2010.0.csv",
    "sha256": "0ecd5c71e0f1dfdbeecd624f7c61875b5fa64094e639cccf6304b2fd181be505"
  },
  "pwt.json": {
    "url": "https://raw.githubusercontent.com/owid/owid-datasets/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets/Penn%20World%20Table%20version%2010.0/datapackage.json",
    "sha256": "79bcd8893b84bbdc00cea3465c7d1710301de364b526a4d139e2d8469e4d1a57"
  },
  "pwt-codebook.Rd": {
    "url": "https://raw.githubusercontent.com/cran/pwt10/957b298fd706a567af96ccb1663ad68d5e5d07ba/man/pwt10.01.Rd",
    "sha256": "1423777c6f945858bad194f86d8791c4ac16e5dec0ef078b893fb13ac35f35a4"
  }
}
GDP = 'GDP (expenditure, multiple price benchmarks)'
POP = 'Population'
HOURS = 'Annual working hours per worker'
FERTILITY = 'Fertility rate (Complete Gapminder, v12) (2017)'
FIELDS = ['country', 'year', 'tfr_births_per_woman', 'gdp_per_person_2017_ppp', 'annual_hours_per_worker']


def fetch_all():
    payloads = {}
    for name, source in SOURCES.items():
        with urlopen(source['url'], timeout=60) as response:
            data = response.read()
        if hashlib.sha256(data).hexdigest() != source['sha256']:
            raise ValueError(f'Source checksum mismatch: {name}')
        payloads[name] = data
    return payloads


def keyed(data):
    rows = list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'))))
    result = {}
    for row in rows:
        key = row['Entity'], int(row['Year'])
        if key in result:
            raise ValueError(f'Duplicate country-year: {key}')
        result[key] = row
    return result


def number(value):
    if not value or not value.strip():
        return None
    x = float(value)
    if not math.isfinite(x) or x <= 0:
        raise ValueError(f'Invalid positive value: {value}')
    return x


def write_csv(name, fields, rows):
    with (OUT / name).open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    payloads = fetch_all()
    pwt, fertility = keyed(payloads['pwt.csv']), keyed(payloads['gapminder.csv'])
    rows = []
    missing = {'fertility': 0, 'gdp_population_or_hours': 0}
    for (country, year), p in sorted(pwt.items()):
        if not FIRST_YEAR <= year <= LAST_YEAR:
            continue
        f = fertility.get((country, year))
        tfr = number(f[FERTILITY]) if f else None
        if tfr is None:
            missing['fertility'] += 1
            continue
        gdp, population, hours = number(p[GDP]), number(p[POP]), number(p[HOURS])
        if None in (gdp, population, hours):
            missing['gdp_population_or_hours'] += 1
            continue
        # OWID's archive expresses GDP in 2017 international dollars and population
        # in people. Both are scaled from the original PWT million-unit variables.
        rows.append(dict(zip(FIELDS, [country, year, tfr, gdp / population, hours])))
    selected = [r for r in rows if r['country'] in COUNTRIES]
    if {r['country'] for r in selected} != set(COUNTRIES):
        raise ValueError('A selected country has no complete observations')
    OUT.mkdir(parents=True, exist_ok=True)
    write_csv('matched-country-years.csv', FIELDS, rows)
    write_csv('selected-country-years.csv', FIELDS, selected)
    endpoint_fields = ['country', 'first_year', 'last_year', 'observations',
                       'first_tfr', 'last_tfr', 'first_gdp_per_person', 'last_gdp_per_person',
                       'first_hours', 'last_hours']
    endpoints = []
    for country in COUNTRIES:
        country_rows = [r for r in selected if r['country'] == country]
        a, b = country_rows[0], country_rows[-1]
        endpoints.append(dict(zip(endpoint_fields, [country, a['year'], b['year'], len(country_rows),
                         a[FIELDS[2]], b[FIELDS[2]], a[FIELDS[3]], b[FIELDS[3]], a[FIELDS[4]], b[FIELDS[4]]])))
    write_csv('country-endpoints.csv', endpoint_fields, endpoints)
    for key in ('pwt.json', 'gapminder.json'):
        (OUT / key.replace('.json', '-metadata.json')).write_bytes(payloads[key])
    (OUT / 'pwt10.01-codebook.Rd').write_bytes(payloads['pwt-codebook.Rd'])
    provenance = {
        'retrieved_date_utc': datetime.now(timezone.utc).date().isoformat(),
        'sources': SOURCES,
        'vintage_note': 'OWID archive title/metadata say PWT10.0; matched GDP/person and hours values agree with CRAN-distributed PWT10.01. See pwt-vintage-check.json; no original-provider identity is asserted.',
        'period': [FIRST_YEAR, LAST_YEAR],
        'forecast_exclusion': 'Gapminder v12 metadata classifies 2015 onward as UN forecasts; all such rows excluded.',
        'measure': 'TFR, births per woman implied by age-specific period rates; not a count of births or crude birth rate.',
        'gdp': 'OWID GDP (expenditure, multiple price benchmarks) / Population; expenditure-side real GDP per person, 2017 PPP international dollars. Not GDP per hour or TFP.',
        'hours': 'PWT average annual market hours per worker/person engaged; not leisure or unpaid care.',
        'join': 'Exact OWID Entity name and calendar Year, no aliases; require all three measures even for GDP-only comparisons.',
        'transformations': ['1970–2014 only', 'No imputation, interpolation, extrapolation or country weighting added',
                            'Positive finite values only; exclude incomplete rows; retain full float precision in CSV',
                            'Gapminder historical series itself includes interpolated estimates; original inputs are not all annual observations'],
        'coverage': {'matched_rows': len(rows), 'economies': len({r['country'] for r in rows}),
                     'selected_rows': len(selected), 'selected_economies': len(COUNTRIES), 'excluded_pwt_rows': missing},
        'selection': COUNTRIES,
        'limits': ['Archived releases, not current-year values', 'No causal inference or paper-estimate replication',
                   'Original-provider records, corrections, later revisions and third-party reuse terms remain to be checked'],
    }
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2, ensure_ascii=False) + '\n')
    table = '| Country | Years | Matched years | TFR, first → last | GDP/person, first → last | Hours/worker, first → last |\n'
    table += '| --- | --- | ---: | ---: | ---: | ---: |\n'
    for e in endpoints:
        table += (f"| {e['country']} | {e['first_year']}–{e['last_year']} | {e['observations']} | "
                  f"{e['first_tfr']:.2f} → {e['last_tfr']:.2f} | ${e['first_gdp_per_person']:,.0f} → ${e['last_gdp_per_person']:,.0f} | "
                  f"{e['first_hours']:,.0f} → {e['last_hours']:,.0f} |\n")
    page = ROOT / 'src/content/docs/data/fertility-charts.md'
    text = page.read_text()
    start, end = '<!-- BEGIN ENDPOINT TABLE -->', '<!-- END ENDPOINT TABLE -->'
    before, rest = text.split(start)
    _, after = rest.split(end)
    page.write_text(before + start + '\n' + table + end + after)
    print(json.dumps(provenance['coverage']))


if __name__ == '__main__':
    main()
