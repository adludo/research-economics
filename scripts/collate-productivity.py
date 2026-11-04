#!/usr/bin/env python3
"""Reproduce a dated labour-productivity growth example from pinned inputs."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/data/productivity'
COUNTRIES = ['Australia', 'Canada', 'France', 'Germany', 'Japan', 'South Korea',
             'United Kingdom', 'United States']
GDP = 'GDP (using national accounts growth rates)'
EMP = 'Number of people in work'
HOURS = 'Annual working hours per worker'
PERIODS = [(1995, 2007), (2010, 2019)]


def positive(value):
    x = float(value)
    if not math.isfinite(x) or x <= 0:
        raise ValueError('Missing or invalid input')
    return x


def write(name, fields, rows):
    with (OUT / name).open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-cache', type=Path)
    args = parser.parse_args()
    manifest = json.loads((OUT / 'sources.json').read_text())
    payloads = {}
    for name, source in manifest['sources'].items():
        if args.input_cache:
            data = (args.input_cache / name).read_bytes()
        else:
            with urlopen(source['url'], timeout=60) as response:
                data = response.read()
        if hashlib.sha256(data).hexdigest() != source['sha256']:
            raise ValueError(f'Checksum mismatch: {name}')
        payloads[name] = data
    panel = []
    keys = set()
    for row in csv.DictReader(io.StringIO(payloads['pwt.csv'].decode('utf-8-sig'))):
        country, year = row['Entity'], int(row['Year'])
        if country not in COUNTRIES or not 1995 <= year <= 2019:
            continue
        if (country, year) in keys:
            raise ValueError('Duplicate country-year')
        keys.add((country, year))
        gdp, emp, avh = [positive(row[f]) for f in [GDP, EMP, HOURS]]
        # OWID already expands original PWT million-unit GDP and employment.
        panel.append({'country': country, 'year': year, 'real_gdp_national_accounts': gdp,
                      'persons_engaged': emp, 'annual_hours_per_person': avh,
                      'total_hours': emp * avh, 'real_output_per_hour': gdp / (emp * avh)})
    panel.sort(key=lambda row: (COUNTRIES.index(row['country']), row['year']))
    if len(panel) != len(COUNTRIES) * 25:
        raise ValueError('Incomplete 1995–2019 panel')
    growth = []
    for country in COUNTRIES:
        lookup = {r['year']: r for r in panel if r['country'] == country}
        rates = []
        for first, last in PERIODS:
            p0, p1 = lookup[first]['real_output_per_hour'], lookup[last]['real_output_per_hour']
            rates.append(100 * ((p1 / p0) ** (1 / (last - first)) - 1))
        growth.append({'country': country, 'growth_1995_2007_percent': rates[0],
                       'growth_2010_2019_percent': rates[1],
                       'difference_percentage_points': rates[1] - rates[0]})
    write('country-years.csv', list(panel[0]), panel)
    write('growth-comparison.csv', list(growth[0]), growth)
    (OUT / 'pwt-metadata.json').write_bytes(payloads['pwt.json'])
    codebook = payloads['pwt-codebook.Rd'].decode('utf-8')
    (OUT / 'pwt-codebook.Rd').write_text('\n'.join(line.rstrip() for line in codebook.splitlines()) + '\n')
    provenance = {**manifest, 'codebook_copy': 'Trailing line whitespace stripped; original input checksum verified before normalization.', 'countries': COUNTRIES, 'panel_years': [1995, 2019],
        'comparison_periods': PERIODS, 'country_years': len(panel),
        'numerator': GDP + '; maps to PWT rgdpna, real GDP at constant2017 national prices. Used for within-country growth, not international productivity levels.',
        'denominator': 'Number of people in work (persons engaged) × annual working hours per worker; OWID units already absolute, no extra million factor.',
        'growth': '100*((P_end/P_start)**(1/(end-start))-1), geometric annualized growth; later minus earlier gives percentage points.',
        'selection': 'Eight illustrative advanced economies with complete inputs; not random, representative, or a world/OECD aggregate.',
        'vintage': 'OWID title says10.0; all200 selected rows rgdpna/emp/avh separately match pinned CRAN-distributed10.01 (parent check). Original-provider identity not established.',
        'limits': ['Historical archive ending2019, not a2026nowcast.',
                   'Period choices matter; omitted2008–2009 contraction and post2019 years are not zero growth.',
                   'No causal identification, new weighting, interpolation, country averaging, or paper replication.',
                   'Paper fulltexts, publisher/DOI identity, corrections/retractions and current provider releases remain unverified where blocked.']}
    (OUT / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    page = ROOT / 'src/content/docs/productivity/slowdown.md'
    if page.exists():
        table = '| Country | 1995–2007 | 2010–2019 | Change (percentage points) |\n'
        table += '| --- | ---: | ---: | ---: |\n'
        for row in growth:
            table += (f"| {row['country']} | {row['growth_1995_2007_percent']:.2f}% | "
                      f"{row['growth_2010_2019_percent']:.2f}% | {row['difference_percentage_points']:+.2f} |\n")
        before, rest = page.read_text().split('<!-- BEGIN GROWTH TABLE -->')
        _, after = rest.split('<!-- END GROWTH TABLE -->')
        page.write_text(before + '<!-- BEGIN GROWTH TABLE -->\n' + table + '<!-- END GROWTH TABLE -->' + after)
    print(f'Wrote {len(panel)} country-years and {len(growth)} growth comparisons.')


if __name__ == '__main__':
    main()
