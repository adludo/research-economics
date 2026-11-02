#!/usr/bin/env python3
"""Reproduce the working-hours extracts and documentation from pinned OWID files."""
import csv
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/working-hours'
PAGE = ROOT / 'src/content/docs/data/working-hours.md'
REVISION = '6155d4ca1ea14ef30e753010a25521eeb416e8a2'
BASE = f'https://raw.githubusercontent.com/owid/owid-datasets/{REVISION}/datasets/'
NAMES = {'pwt': 'Penn World Table version 10.0',
         'historical': 'Working Hours Data - Huberman & Minns (2007)'}
EXPECTED = {"pwt.csv": "0ecd5c71e0f1dfdbeecd624f7c61875b5fa64094e639cccf6304b2fd181be505", "pwt.json": "79bcd8893b84bbdc00cea3465c7d1710301de364b526a4d139e2d8469e4d1a57", "historical.csv": "534c2e6df4c4d8ca165598052021b70fe4143ddba68fe0f4ae61b3f9a1482291", "historical.json": "99c047264eb01a2460b0c6c9f45a176c25a45cb7470dbcd4ebd25865edeb09cc"}


def fetch(series, extension):
    name = NAMES[series]
    file = name + '.csv' if extension == 'csv' else 'datapackage.json'
    url = BASE + quote(f'{name}/{file}')
    with urlopen(url, timeout=60) as response:
        data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED[f'{series}.{extension}']:
        raise ValueError(f'Unexpected checksum: {series}.{extension}')
    return data, {'url': url, 'sha256': digest}


def write_csv(name, fields, rows):
    with (OUT / name).open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def replace_section(text, name, content):
    start, end = f'<!-- BEGIN {name} -->', f'<!-- END {name} -->'
    before, rest = text.split(start)
    _, after = rest.split(end)
    return before + start + '\n' + content + '\n' + end + after


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sources, content = {}, {}
    # Fetch and verify all inputs before writing outputs.
    for series in NAMES:
        for extension in ('csv', 'json'):
            data, provenance = fetch(series, extension)
            key = f'{series}.{extension}'
            sources[key] = provenance
            content[key] = data
    for series in NAMES:
        metadata = json.loads(content[f'{series}.json'])
        (OUT / f'{series}-metadata.json').write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False) + '\n')
    pwt = list(csv.DictReader(io.StringIO(content['pwt.csv'].decode('utf-8-sig'))))
    field = 'Annual working hours per worker'
    annual = [{'country': r['Entity'], 'year': r['Year'], 'annual_hours': r[field]}
              for r in pwt if r[field].strip()]
    annual.sort(key=lambda r: (r['country'], int(r['year'])))
    current = [r for r in annual if r['year'] == '2019']
    if not current or any(float(r['annual_hours']) <= 0 for r in annual):
        raise ValueError('Missing 2019 data or nonpositive hours')
    write_csv('pwt-hours.csv', ['country', 'year', 'annual_hours'], annual)
    write_csv('pwt-hours-2019.csv', ['country', 'year', 'annual_hours'], current)
    historical = list(csv.DictReader(io.StringIO(content['historical.csv'].decode('utf-8-sig'))))
    weekly = next(k for k in historical[0] if '(Weekly Work Hours)' in k)
    yearly = next(k for k in historical[0] if '(Annual Work Hours)' in k)
    hist = [{'country': r['Entity'], 'year': r['Year'], 'annual_hours': r[yearly],
             'weekly_hours': r[weekly], 'weeks_worked': r['Weeks Worked'],
             'vacation_holiday_days': r['Days of Vacation and Holidays']} for r in historical]
    write_csv('historical-hours.csv', list(hist[0]), hist)
    table = '| Country/economy | Year | Annual hours per worker |\n| --- | --- | ---: |\n'
    table += '\n'.join(f"| {r['country']} | 2019 | {float(r['annual_hours']):,.0f} |" for r in current)
    endpoints = {}
    for r in hist:
        if r['year'] in ('1870', '2000') and r['annual_hours']:
            endpoints.setdefault(r['country'], {})[r['year']] = float(r['annual_hours'])
    historical_table = '| Country | Annual hours, 1870 | Annual hours, 2000 | Change |\n| --- | ---: | ---: | ---: |\n'
    changes = []
    for country, values in sorted(endpoints.items()):
        if len(values) != 2:
            continue
        a, b = values['1870'], values['2000']
        change = 100 * (b / a - 1)
        changes.append(change)
        historical_table += f'| {country} | {a:,.0f} | {b:,.0f} | {change:.1f}% |\n'
    low = min(current, key=lambda r: float(r['annual_hours']))
    high = max(current, key=lambda r: float(r['annual_hours']))
    summary = (
        f"- The PWT extract contains **{len(annual):,} non-missing country-year observations** "
        f"for **{len({r['country'] for r in annual})} economies**, with **{len(current)}** observed in 2019.\n"
        f"- In this 2019 sample, annual hours range from **{float(low['annual_hours']):,.0f} in {low['country']}** "
        f"to **{float(high['annual_hours']):,.0f} in {high['country']}**. These are sample extremes, not world-wide bounds.\n"
        f"- Annual hours fall between 1870 and 2000 in **{sum(c < 0 for c in changes)} of {len(changes)}** "
        'historical endpoint comparisons. Changing source coverage limits a like-for-like interpretation.'
    )
    text = PAGE.read_text()
    for name, value in [('PWT TABLE', table), ('HISTORICAL TABLE', historical_table.rstrip()),
                        ('DATA SUMMARY', summary)]:
        text = replace_section(text, name, value)
    PAGE.write_text(text)
    provenance = {
        'retrieved_date_utc': datetime.now(timezone.utc).date().isoformat(),
        'archive_revision': REVISION, 'sources': sources,
        'transformations': [
            'PWT: select nonempty annual working hours, preserve values and OWID labels, sort country/year.',
            '2019: filter PWT extract to one common year; round displayed hours only.',
            'Historical: rename columns, retain empty cells; endpoint changes = 100*(2000/1870-1).',
            'No interpolation, population weighting, or imputation. Do not splice the series.'
        ],
        'attribution': 'PWT 10.0 / Feenstra, Inklaar and Timmer; Huberman and Minns (2007); distributed by Our World in Data.',
        'usage': 'Consult original-provider and OWID terms for reuse; no new licence is asserted for third-party data.'
    }
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    print(f'Wrote {len(annual)} PWT observations, {len(current)} for 2019, and {len(hist)} historical rows.')


if __name__ == '__main__':
    main()
