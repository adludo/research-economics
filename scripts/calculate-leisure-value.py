#!/usr/bin/env python3
"""Reproduce clearly labelled leisure-value derivations from paper calibration."""
import csv
import hashlib
import json
import math
from pathlib import Path
from urllib.request import urlopen
import argparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/leisure-value'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-source', action='store_true', help='Download and hash-check the pinned author PDF; it is not redistributed.')
    args = parser.parse_args()
    source = json.loads((DATA / 'sources.json').read_text())['sources'][0]
    if args.verify_source:
        with urlopen(source['source_url'], timeout=60) as response:
            payload = response.read()
        if hashlib.sha256(payload).hexdigest() != source['sha256']:
            raise ValueError('Source PDF checksum mismatch')
    p = json.loads((DATA / 'calibration.json').read_text())
    c, theta, epsilon, ell, time = [float(p[k]) for k in
        ['annual_consumption', 'theta', 'frisch_elasticity', 'baseline_leisure_share', 'annual_waking_hours']]
    if not (c > 0 and theta > 0 and epsilon > 0 and time > 0 and 0 < ell < 1):
        raise ValueError('Invalid calibration')
    def v(l):
        return -theta * epsilon / (1 + epsilon) * (1 - l) ** ((1 + epsilon) / epsilon)
    hourly = c * theta * (1 - ell) ** (1 / epsilon) / time
    results = []
    for hours in p['counterfactual_additional_annual_hours']:
        share = ell + hours / time
        if not ell < share < 1:
            raise ValueError('Counterfactual outside leisure domain')
        dv = v(share) - v(ell)
        results.append({'additional_annual_hours': hours, 'new_leisure_share': share,
                        'utility_gain': dv, 'local_linear_value_2012_usd': hourly * hours,
                        'exact_wtp_2012_usd': -c * math.expm1(-dv),
                        'equivalent_consumption_increase_2012_usd': c * math.expm1(dv)})
    with (DATA / 'worked-examples.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(results)
    derived = {'marginal_value_per_hour_2012_usd': hourly,
               'net_hourly_wage_from_rounded_moments_2012_usd': p['annual_earnings_for_calibration'] * (1-p['marginal_tax_rate']) / (time * (1-ell)),
               'source_sha256': source['sha256'], 'formulas':{
                   'marginal':'C*theta*(1-ell)**(1/epsilon)/H',
                   'wtp':'C*(1-exp(-(v(ell+hours/H)-v(ell))))',
                   'equivalent_consumption_increase':'C*(exp(v(ell+hours/H)-v(ell))-1)'},
               'limits':['Our algebra and static counterfactuals from rounded calibration, not published price estimates.',
                         'Hold consumption baseline and other welfare dimensions fixed; no wage-income/policy equilibrium simulated.',
                         'Money is in2012USdollars; no inflation update.',
                         'Finite WTP and equivalent consumption increase use different comparison allocations.']}
    (DATA / 'derived-values.json').write_text(json.dumps(derived,indent=2)+'\n')
    page = ROOT / 'src/content/docs/findings/leisure-value.md'
    if page.exists():
        table = '| Extra leisure | Local linear approximation | Exact WTP | Equivalent consumption increase |\n'
        table += '| --- | ---: | ---: | ---: |\n'
        for row in results:
            label = '1 hour in the year' if row['additional_annual_hours'] == 1 else '1 hour/day for 365 days'
            table += f"| {label} | ${row['local_linear_value_2012_usd']:,.2f} | ${row['exact_wtp_2012_usd']:,.2f} | ${row['equivalent_consumption_increase_2012_usd']:,.2f} |\n"
        before, rest = page.read_text().split('<!-- BEGIN VALUE TABLE -->')
        _, after = rest.split('<!-- END VALUE TABLE -->')
        page.write_text(before+'<!-- BEGIN VALUE TABLE -->\n'+table+'<!-- END VALUE TABLE -->'+after)
    print(f'Model-implied local value: ${hourly:.6f}/hour in 2012 dollars; wrote {len(results)} counterfactuals.')


if __name__ == '__main__':
    main()
