#!/usr/bin/env python3
"""Render leisure-source examples, coverage, and nonquantitative reading guides."""
import csv
import json
import math
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/leisure-surveys'
OUT = ROOT / 'public/charts/leisure-surveys'
PROVENANCE = json.loads((DATA / 'provenance.json').read_text())
DIAGRAMS = json.loads((DATA / 'measurement-diagrams.json').read_text())
ARCHIVE = 'https://github.com/owid/owid-datasets/tree/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets'
INK, MUTED = '#102a43', '#52667a'
COLORS = ['#087e8b', '#6554a4', '#bb641c', '#00795e', '#b64164', '#3c71b5']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#cbd5e1', 'text.color': INK,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'svg.fonttype': 'none', 'svg.hashsalt': 'leisure-surveys-v1'})


def load(name):
    with (DATA / name).open() as file:
        return list(csv.DictReader(file))


def title(fig, heading, subtitle):
    fig.suptitle(heading, x=.08, y=.97, ha='left', fontsize=18, fontweight='bold')
    fig.text(.08, .917, subtitle, color=MUTED, fontsize=10.5)


def style(ax):
    ax.grid(color='#e2e8f0', linewidth=.6)
    ax.set_axisbelow(True)


def footer(fig, key, source, limit):
    fig.text(.08, .085, source, fontsize=8, color=MUTED,
             url=PROVENANCE['sources'][key + '.csv']['url'])
    fig.text(.08, .059, 'Retrieved from: ' + ARCHIVE, fontsize=7.4, color=MUTED, url=ARCHIVE)
    fig.text(.08, .033, 'Retrieved 2026-11-02 • ' + limit, fontsize=8, color=MUTED)
    fig.text(.08, .009, 'Archived illustration; original-provider agreement and current releases unverified. Descriptive, not causal.',
             fontsize=8, color=MUTED)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / f'{name}.svg'
    fig.savefig(svg, facecolor='white', metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    fig.savefig(OUT / f'{name}.png', dpi=170, facecolor='white')
    plt.close(fig)


def consecutive(values):
    groups = []
    for value in sorted(values):
        if not groups or value != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(value)
    return groups


def atus():
    data = load('atus-social-time.csv')
    companies = ['alone', 'children', 'coworkers', 'family', 'friends', 'partner']
    fig, axes = plt.subplots(3, 2, figsize=(12, 10.5))
    fig.subplots_adjust(left=.08, right=.96, top=.82, bottom=.19, hspace=.5, wspace=.22)
    title(fig, 'ATUS: who Americans spend time with',
          'Age profiles pooled over 2009–2019 • minutes per day • not leisure-only time')
    for ax, company, color in zip(axes.flat, companies, COLORS):
        values = {int(r['age']): float(r['minutes_per_day']) for r in data if r['company'] == company}
        for group in consecutive(values):
            line, = ax.plot(group, [values[a] for a in group], color=color,
                            linewidth=1.8, marker='o', markersize=2)
            line.set_gid(f'atus-{company}-{group[0]}')
        ax.set_title('Alone' if company == 'alone' else 'With ' + company, loc='left', fontweight='bold')
        ax.set_xlim(14, 86)
        ax.set_ylim(0, 600)
        ax.set_xticks([15, 35, 55, 75, 85])
        ax.yaxis.set_major_locator(MultipleLocator(200))
        ax.set_xlabel('Respondent age label (years)')
        ax.set_ylabel('Minutes per day')
        style(ax)
    fig.text(.08, .137, 'Company categories overlap. These are different age groups, not people followed as they grow older.',
             fontsize=10, color=MUTED)
    footer(fig, 'atus', 'Source: BLS ATUS Who File, OWID weighted estimates pooled over 2009–2019.',
           'Year encodes age; 80/85 labels retained, top-coding unverified. Missing age labels remain gaps.')
    save(fig, 'atus-social-time')


def mtus():
    data = load('mtus-coverage.csv')
    countries = sorted({r['country'] for r in data})
    fig, ax = plt.subplots(figsize=(12, 9.5))
    fig.subplots_adjust(left=.19, right=.96, top=.83, bottom=.21)
    title(fig, 'MTUS: country-year coverage in the public archive',
          '89 rows across 16 countries • dots show available archive entries, not minutes of leisure')
    for index, country in enumerate(countries):
        years = sorted(int(r['survey_year']) for r in data if r['country'] == country)
        points = ax.scatter(years, [index] * len(years), color=COLORS[0], s=30)
        points.set_gid('mtus-' + country.replace(' ', '-'))
    ax.set_yticks(range(len(countries)), countries)
    ax.invert_yaxis()
    ax.set_xlim(1955, 2015)
    ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010])
    ax.set_xlabel('Country-year label in the archived extract')
    style(ax)
    footer(fig, 'mtus', 'Source: MTUS, attributed to Gershuny and Fisher (2013), via OWID; processed sample ages 21–65.',
           'Coverage only. Positive-report averaging and normalization prevent a valid summed leisure total.')
    save(fig, 'mtus-coverage')


def hetus():
    data = load('hetus-leisure.csv')
    countries = sorted({r['country'] for r in data})
    fig, ax = plt.subplots(figsize=(12, 11))
    fig.subplots_adjust(left=.19, right=.95, top=.82, bottom=.19)
    title(fig, 'HETUS: leisure, social, and associative life',
          'Population time-spent estimates • minutes per day • country labels in alphabetical order')
    for wave, color in [(2000, COLORS[1]), (2010, COLORS[0])]:
        selected = [r for r in data if int(r['wave_label']) == wave]
        points = ax.scatter([float(r['leisure_minutes_per_day']) for r in selected],
                            [countries.index(r['country']) for r in selected],
                            color=color, s=42, label=f'Wave label {wave}')
        points.set_gid(f'hetus-wave-{wave}')
    ax.set_yticks(range(len(countries)), countries)
    ax.invert_yaxis()
    maximum = max(float(r['leisure_minutes_per_day']) for r in data)
    ax.set_xlim(0, max(480, math.ceil(maximum / 60) * 60))
    ax.xaxis.set_major_locator(MultipleLocator(120))
    ax.set_xlabel('Minutes per average day')
    ax.legend(loc='lower right', frameon=True)
    style(ax)
    footer(fig, 'hetus', 'Source: Eurostat HETUS waves 1/2 via OWID; population Time spent column, not Participation time.',
           '2000/2010 are wave labels, not verified fieldwork years. Archive normalized to 1,440 minutes/day.')
    save(fig, 'hetus-leisure')


def finland():
    data = load('finland-free-time.csv')
    fig, ax = plt.subplots(figsize=(12, 7.5))
    fig.subplots_adjust(left=.10, right=.95, top=.80, bottom=.24)
    title(fig, 'Statistics Finland: free time in survey-labelled years',
          'All-sex, men, and women series • minutes per average day • population age coverage unverified')
    for sex, color in zip(['all', 'men', 'women'], COLORS):
        selected = sorted((r for r in data if r['sex'] == sex), key=lambda r: int(r['year']))
        line, = ax.plot([int(r['year']) for r in selected],
                        [float(r['free_time_minutes_per_day']) for r in selected],
                        color=color, marker='o', linewidth=2, label='All sexes' if sex == 'all' else sex.title())
        line.set_gid('finland-' + sex)
    ax.set_xlim(1977, 2011)
    ax.set_xticks([1979, 1987, 1999, 2009])
    ax.set_ylim(0, 480)
    ax.set_ylabel('Minutes per day')
    ax.set_xlabel('Year label in archive (lines are visual guides)')
    ax.legend(loc='lower left', frameon=False, ncol=3)
    style(ax)
    footer(fig, 'finland', 'Source: Statistics Finland time-use surveys, via OWID; Free time category copied unchanged.',
           'Only four labelled survey dates; no intermediate annual estimates or second normalization added.')
    save(fig, 'finland-free-time')


def historical():
    data = load('historical-definitions.csv')
    labels = ['Measure 1: activity-based', 'Measure 2: adds sleep / personal care',
              'Measure 3: adds primary / educational care', 'Measure 4: residual of total work']
    fig, axes = plt.subplots(2, 2, figsize=(12, 9.5))
    fig.subplots_adjust(left=.08, right=.95, top=.80, bottom=.20, hspace=.4, wspace=.22)
    title(fig, 'Historical US diaries: the leisure definition matters',
          'Aguiar–Hurst (2006) working-paper archive • supplied “All individuals” series • not a current AHTUS extract')
    for measure, ax, label, color in zip(range(1, 5), axes.flat, labels, COLORS):
        selected = sorted((r for r in data if int(r['measure']) == measure), key=lambda r: int(r['year']))
        line, = ax.plot([int(r['year']) for r in selected], [float(r['hours_per_week']) for r in selected],
                        color=color, marker='o', linewidth=2)
        line.set_gid(f'historical-measure-{measure}')
        ax.set_title(label, loc='left', fontsize=10.5, fontweight='bold')
        ax.set_ylim(0, 140)
        ax.set_xlim(1962, 2006)
        ax.set_xticks([1965, 1985, 2003])
        ax.set_xlabel('Survey-year label (lines are visual guides)')
        ax.set_ylabel('Hours per week')
        style(ax)
    footer(fig, 'historical', 'Source: OWID archive attributed to Aguiar and Hurst (2006); definitions from archived field metadata.',
           'Sample age exclusions unverified. 2003 childcare coding differs. Not a final-paper replication.')
    save(fig, 'historical-definitions')


def diagram(key):
    item = DIAGRAMS[key]
    fig, ax = plt.subplots(figsize=(12, 5.8))
    fig.subplots_adjust(left=.05, right=.97, bottom=.30, top=.77)
    fig.suptitle(item['title'], x=.08, y=.955, ha='left', fontsize=17, fontweight='bold')
    fig.text(.08, .865, 'Measurement diagram • no empirical quantities or time shares are plotted', color=MUTED, fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    count = len(item['nodes'])
    gap = .035
    width = (.9 - (count - 1) * gap) / count
    for index, label in enumerate(item['nodes']):
        x = .05 + index * (width + gap)
        box = FancyBboxPatch((x, .25), width, .48,
                             boxstyle='round,pad=.012,rounding_size=.025',
                             edgecolor=COLORS[index], facecolor='#f1f5f9', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + width / 2, .49, label, ha='center', va='center', fontsize=11, color=INK)
        if key == 'ahtus' and index < count - 1:
            ax.annotate('', xy=(.05 + (index + 1) * (width + gap) - .01, .49), xytext=(x + width + .01, .49),
                        arrowprops={'arrowstyle': '->', 'color': MUTED, 'lw': 1.3})
    fig.text(.08, .24, item['note'], fontsize=10, color=MUTED)
    fig.text(.08, .18, item['limit'], fontsize=9, color=MUTED)
    fig.text(.08, .115, 'Guide reference: ' + item['source_url'], fontsize=8.5, color=MUTED, url=item['source_url'])
    fig.text(.08, .064, 'Basis: this wiki’s source guide; original-provider definitions/access could not be verified (HTTP 403).',
             fontsize=8.5, color=MUTED)
    fig.text(.08, .022, 'Prepared 2026-11-02 • Conceptual illustration; no current provider data downloaded for this diagram.',
             fontsize=8.5, color=MUTED)
    save(fig, key + '-measurement')


def main():
    atus()
    diagram('ahtus')
    mtus()
    hetus()
    diagram('oecd')
    finland()
    historical()
    print('Wrote seven section figures (five data/coverage graphs, two conceptual diagrams), SVG and PNG.')


if __name__ == '__main__':
    main()
