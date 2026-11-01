#!/usr/bin/env python3
"""Render recent fertility/income and weekly working-hours figures offline."""
import csv
import json
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import FixedLocator, FuncFormatter, MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/recent-economy'
OUT = ROOT / 'public/charts/recent-economy'
PROVENANCE = json.loads((DATA / 'provenance.json').read_text())
COUNTRIES = PROVENANCE['selection']
RECENT = PROVENANCE['recent_hours_codes']
TFR, GDP, HOURS = 'tfr_births_per_woman', 'gdp_per_person_2021_ppp', 'weekly_hours_per_employed_person'
INK, MUTED, TEAL = '#102a43', '#52667a', '#087e8b'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#cbd5e1', 'text.color': INK,
                     'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.labelcolor': INK, 'svg.fonttype': 'none',
                     'svg.hashsalt': 'recent-economy-v1'})


def load():
    series = {code: {} for code in COUNTRIES}
    with (DATA / 'country-years.csv').open() as file:
        for row in csv.DictReader(file):
            code, year = row['code'], int(row['year'])
            if year in series[code]:
                raise ValueError('Duplicate country-year')
            series[code][year] = {k: float(row[k]) if row[k] else None for k in (TFR, GDP, HOURS)}
    return series


def runs(years):
    groups = []
    for year in sorted(years):
        if not groups or year != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(year)
    return groups


def style(ax):
    ax.grid(color='#e2e8f0', linewidth=.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)


def heading(fig, title, subtitle):
    fig.suptitle(title, x=.075, y=.975, ha='left', fontsize=19, fontweight='bold')
    fig.text(.075, .937, subtitle, fontsize=10.5, color=MUTED)


def footer(fig, include_wdi=True, include_hours=True):
    lines = []
    if include_wdi:
        lines.append(('World Bank WDI: SP.DYN.TFRT.IN (fertility); NY.GDP.PCAP.PP.KD (constant 2021 PPP GDP/person).',
                      PROVENANCE['sources']['fertility.csv']['url']))
        lines.append(('Retrieved from github.com/open-numbers/ddf--world_bank--world_development_indicators • revision 4252d91',
                      PROVENANCE['sources']['gdp.csv']['url']))
    if include_hours:
        lines.append(('ILOSTAT: HOW_TEMP_SEX_ECO_NB • total sexes, all economic activities • weekly hours actually worked per employed person.',
                      PROVENANCE['sources']['ilo-metadata.csv']['url']))
        lines.append(('Retrieved from github.com/open-numbers/ddf--ilo--ilostat • revision c4dd68c • country titles link to raw hours CSVs.',
                      'https://github.com/open-numbers/ddf--ilo--ilostat/tree/c4dd68c687df8162835e1684cffec8723b19eee8'))
    lines.append((f"Retrieved {PROVENANCE['retrieved_date_utc']} • Published estimates, not uniform survey observations • Descriptive, not causal.", None))
    for index, (label, url) in enumerate(lines):
        fig.text(.075, .018 + (len(lines) - index - 1) * .019, label,
                 fontsize=8, color=MUTED, url=url)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f'{name}.svg', facecolor='white', metadata={'Date': None})
    svg = OUT / f'{name}.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    fig.savefig(OUT / f'{name}.png', dpi=170, facecolor='white')
    plt.close(fig)


def country_title(ax, code, hours=False):
    label = ax.set_title(COUNTRIES[code], loc='left', fontweight='bold', fontsize=11)
    if hours:
        label.set_url(PROVENANCE['sources'][f'hours-{code}.csv']['url'])


def relationship(series, field, codes, name):
    is_gdp = field == GDP
    first = 1990 if is_gdp else 2000
    nrows = len(codes) // 3
    fig, axes = plt.subplots(nrows, 3, figsize=(12, 3 * nrows + 1.7))
    fig.subplots_adjust(left=.075, right=.965, bottom=.20 if is_gdp else .23,
                        top=.85 if is_gdp else .82, hspace=.55, wspace=.25)
    heading(fig, 'Fertility and GDP per person' if is_gdp else 'Fertility and weekly working hours',
            f'{len(codes)} selected countries • {first}–2024 published estimates • colours follow calendar years')
    fig.text(.075, .895, 'Vertical axis: total fertility rate (births per woman)', fontsize=10, color=MUTED)
    norm = Normalize(first, 2024)
    cax = fig.add_axes([.70, .903, .25, .01])
    bar = fig.colorbar(ScalarMappable(norm=norm, cmap='viridis'), cax=cax,
                       orientation='horizontal', ticks=[first, (first + 2024) // 2, 2024])
    bar.ax.tick_params(labelsize=8)
    for ax, code in zip(axes.flat, codes):
        values = series[code]
        years = [y for y, row in values.items() if y >= first and row[field] is not None and row[TFR] is not None]
        for group in runs(years):
            line, = ax.plot([values[y][field] for y in group], [values[y][TFR] for y in group],
                            color='#a3b4c2', linewidth=1, zorder=1)
            line.set_gid(f'path-{code}-{group[0]}')
        points = ax.scatter([values[y][field] for y in years], [values[y][TFR] for y in years],
                            c=years, norm=norm, cmap='viridis', s=15, zorder=2)
        points.set_gid(f'points-{code}')
        country_title(ax, code, not is_gdp)
        ax.set_ylim(0, 5 if is_gdp else 4)
        ax.yaxis.set_major_locator(MultipleLocator(1))
        if is_gdp:
            ax.set_xscale('log')
            ax.set_xlim(1000, 100000)
            ax.xaxis.set_major_locator(FixedLocator([1000, 10000, 100000]))
            ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:g}k'))
            ax.minorticks_off()
        else:
            ax.set_xlim(0, 60)
            ax.xaxis.set_major_locator(MultipleLocator(20))
        for year, offset, align in [(years[0], (-3, 9), 'right'), (years[-1], (3, -12), 'left')]:
            ax.annotate(str(year), (values[year][field], values[year][TFR]), xytext=offset,
                        textcoords='offset points', fontsize=8, ha=align,
                        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .85, 'pad': 1})
        style(ax)
    label = 'Real GDP per person (constant 2021 PPP international dollars; log scale)' if is_gdp else 'Mean weekly hours actually worked per employed person (linear scale)'
    fig.text(.52, .155, label, ha='center', fontsize=10.5)
    footer(fig, include_hours=not is_gdp)
    save(fig, name)


def working_hours(series):
    fig, axes = plt.subplots(3, 3, figsize=(12, 10.5))
    fig.subplots_adjust(left=.075, right=.965, bottom=.18, top=.86, hspace=.5, wspace=.25)
    heading(fig, 'Weekly working hours through 2024',
            'Nine selected countries • common scales • dots mark available years • gaps remain empty')
    for ax, code in zip(axes.flat, RECENT):
        values = series[code]
        years = [y for y, row in values.items() if row[HOURS] is not None]
        for group in runs(years):
            line, = ax.plot(group, [values[y][HOURS] for y in group], color=TEAL,
                            marker='o', markersize=3, linewidth=1.8)
            line.set_gid(f'hours-{code}-{group[0]}')
        country_title(ax, code, True)
        ax.set_xlim(1999, 2027)
        ax.set_ylim(0, 60)
        ax.set_xticks([2000, 2010, 2024])
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.annotate(f"{values[2024][HOURS]:.1f}", (2024, values[2024][HOURS]),
                    xytext=(4, 5), textcoords='offset points', fontsize=9, color=TEAL, fontweight='bold')
        if code in RECENT[:3]:
            ax.set_xlabel('')
        if code == RECENT[3]:
            ax.set_ylabel('Weekly hours per employed person', labelpad=13)
        style(ax)
    fig.text(.52, .125, 'Year • national sources and survey coverage can change; no annual-hours conversion',
             ha='center', fontsize=10, color=MUTED)
    footer(fig, include_wdi=False)
    save(fig, 'working-hours')


def time_paths(series):
    examples = ['kor', 'deu', 'usa', 'ind']
    variables = [(TFR, 'Total fertility rate\n(births per woman)', '#087e8b'),
                 (GDP, 'GDP per person\n(2021 PPP $, log scale)', '#5364a5'),
                 (HOURS, 'Weekly hours per\nemployed person', '#bd6a2c')]
    fig, axes = plt.subplots(3, 4, figsize=(14, 11.3))
    fig.subplots_adjust(left=.09, right=.97, bottom=.21, top=.86, hspace=.4, wspace=.27)
    heading(fig, 'Fertility, income, and working time: country paths',
            'Four illustrative countries • 2000–2024 • separate units and common scales within each row')
    for col, code in enumerate(examples):
        values = series[code]
        for row, (field, label, color) in enumerate(variables):
            ax = axes[row, col]
            years = [y for y, r in values.items() if y >= 2000 and r[field] is not None]
            for group in runs(years):
                line, = ax.plot(group, [values[y][field] for y in group], color=color,
                                marker='o', markersize=2, linewidth=1.7)
                line.set_gid(f'{field}-{code}-{group[0]}')
            if row == 0:
                country_title(ax, code, True)
            if field == GDP:
                ax.set_yscale('log')
                ax.set_ylim(2000, 100000)
                ax.yaxis.set_major_locator(FixedLocator([2000, 10000, 100000]))
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:g}k'))
                ax.minorticks_off()
            else:
                ax.set_ylim(0, 5 if field == TFR else 60)
            ax.set_xlim(1999, 2025)
            ax.set_xticks([2000, 2010, 2024])
            if col == 0:
                ax.set_ylabel(label, labelpad=12)
            style(ax)
    fig.text(.52, .145, 'Each row uses its own available years; India’s hours begin in 2018.',
             ha='center', fontsize=10, color=MUTED)
    footer(fig)
    save(fig, 'country-time-paths')


def main():
    series = load()
    relationship(series, GDP, list(COUNTRIES), 'fertility-gdp')
    relationship(series, HOURS, RECENT, 'fertility-hours')
    working_hours(series)
    time_paths(series)
    print('Wrote four charts in SVG and PNG, each with retrieval references.')


if __name__ == '__main__':
    main()
