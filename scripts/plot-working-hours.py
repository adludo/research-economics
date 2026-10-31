#!/usr/bin/env python3
"""Render working-hours charts from the checked-in CSVs; no network access needed."""
import csv
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/working-hours'
OUT = ROOT / 'public/charts/working-hours'
COUNTRIES = ['Australia', 'United States', 'United Kingdom', 'France',
             'Germany', 'Japan', 'South Korea', 'China',
             'India', 'Brazil', 'Mexico', 'South Africa']
BLUE, GREEN, ORANGE = '#155e75', '#087f5b', '#b45309'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#cbd5e1', 'axes.labelcolor': '#334155',
                     'text.color': '#0f172a', 'xtick.color': '#475569',
                     'ytick.color': '#475569', 'svg.fonttype': 'none',
                     'svg.hashsalt': 'research-economics-working-hours'})


def load(name):
    series = {}
    with (DATA / name).open() as file:
        for row in csv.DictReader(file):
            if row['annual_hours']:
                series.setdefault(row['country'], {})[int(row['year'])] = float(row['annual_hours'])
    return series


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f'{name}.svg', facecolor='white', metadata={'Date': None})
    fig.savefig(OUT / f'{name}.png', dpi=170, facecolor='white')
    plt.close(fig)


def panels(series, countries, historical=False):
    rows = (len(countries) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(12, rows * 2.35 + 1.5))
    fig.subplots_adjust(left=.07, right=.97, bottom=.105, top=.89, hspace=.65, wspace=.26)
    for ax, country in zip(axes.flat, countries):
        values = series[country]
        if historical:
            years = sorted(values)
            ax.plot(years, [values[y] for y in years], color=BLUE, marker='o', markersize=3, linewidth=1.8)
            ax.set_xlim(1865, 2005)
            ax.set_xticks([1870, 1930, 2000])
            ax.set_ylim(0, 4000)
            ax.yaxis.set_major_locator(MultipleLocator(1000))
        else:
            years = list(range(1970, 2020))
            # NaNs leave gaps instead of interpolating or substituting zero.
            ax.plot(years, [values.get(y, float('nan')) for y in years], color=BLUE, linewidth=2)
            ax.set_xlim(1968, 2021)
            ax.set_xticks([1970, 1990, 2010, 2019])
            ax.tick_params(axis='x', labelsize=9)
            ax.set_ylim(0, 3000)
            ax.yaxis.set_major_locator(MultipleLocator(1000))
        ax.set_title(country, loc='left', fontsize=12, fontweight='bold', pad=8)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:,.0f}'))
        ax.grid(axis='y', color='#e2e8f0', linewidth=.7)
        ax.set_axisbelow(True)
        last = max(values)
        ax.annotate(f'{values[last]:,.0f}', (last, values[last]), xytext=(-3, 8),
                    textcoords='offset points', ha='right', fontsize=10, color=BLUE)
    for ax in list(axes.flat)[len(countries):]:
        ax.set_visible(False)
    if historical:
        title = 'Working hours declined across this historical sample'
        subtitle = 'Annual hours • all 14 economies • selected observations, 1870–2000'
        footer = ('Source: Huberman & Minns (2007), via OWID archive. Historical definitions and sources change over time.\n'
                  'Dots are observations; connecting lines are guides, not annual estimates. Identical axes in every panel.')
        name = 'historical-trends'
    else:
        title = 'Working-hours trends differ across countries'
        subtitle = 'Annual hours per worker • 12 selected economies • 1970–2019, where available'
        footer = ('Source: Penn World Table 10.0, via OWID archive. Identical axes; labels show final observed hours (2019).\n'
                  'Missing years remain gaps. South Africa starts in 2001 and has no 2015 value. Selection is not a world average.')
        name = 'country-trends'
    fig.suptitle(title, x=.07, y=.977, ha='left', fontsize=19, fontweight='bold')
    fig.text(.07, .94, subtitle, fontsize=12, color='#475569')
    fig.text(.07, .024, footer, fontsize=10, color='#475569', linespacing=1.6)
    save(fig, name)


def changes(series):
    values = sorted((100 * (series[c][2019] / series[c][1990] - 1), c)
                    for c in COUNTRIES if 1990 in series[c] and 2019 in series[c])
    fig, ax = plt.subplots(figsize=(11, 7.5))
    fig.subplots_adjust(left=.19, right=.94, bottom=.16, top=.82)
    ax.barh([c for _, c in values], [v for v, _ in values],
            color=[GREEN if v < 0 else ORANGE for v, _ in values], height=.65)
    ax.invert_yaxis()
    ax.axvline(0, color='#64748b', linewidth=1)
    ax.set_xlim(-33, 15)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:g}%'))
    ax.grid(axis='x', color='#e2e8f0')
    ax.set_axisbelow(True)
    ax.set_xlabel('Change in annual hours per worker, 1990–2019', labelpad=12)
    for i, (value, _) in enumerate(values):
        ax.text(value + (-.6 if value < 0 else .6), i, f'{value:+.1f}%',
                ha='right' if value < 0 else 'left', va='center', fontsize=11)
    fig.suptitle('A common period shows declines and increases', x=.07, y=.96,
                 ha='left', fontsize=18, fontweight='bold')
    fig.text(.07, .905, '11 selected economies with observations in both 1990 and 2019', fontsize=12, color='#475569')
    fig.text(.07, .035,
             'Source: PWT 10.0, via OWID archive. Change = 100 × (2019 hours / 1990 hours − 1).\n'
             'South Africa is excluded because 1990 is unavailable. This is not a full-sample country ranking.',
             fontsize=10, color='#475569', linespacing=1.6)
    save(fig, 'change-1990-2019')
    return values


def main():
    pwt, historical = load('pwt-hours.csv'), load('historical-hours.csv')
    panels(pwt, COUNTRIES)
    values = changes(pwt)
    panels(historical, sorted(historical), historical=True)
    table = '| Country | Annual hours, 1990 | Annual hours, 2019 | Change |\n| --- | ---: | ---: | ---: |\n'
    for value, country in values:
        table += f'| {country} | {pwt[country][1990]:,.0f} | {pwt[country][2019]:,.0f} | {value:+.1f}% |\n'
    page = ROOT / 'src/content/docs/data/working-hours.md'
    text = page.read_text()
    start, end = '<!-- BEGIN CHART CHANGE TABLE -->', '<!-- END CHART CHANGE TABLE -->'
    before, rest = text.split(start)
    _, after = rest.split(end)
    page.write_text(before + start + '\n' + table + end + after)
    for value, country in values:
        print(f'{country}: {value:+.1f}% (1990–2019)')
    print('Wrote three charts, each as SVG and PNG.')


if __name__ == '__main__':
    main()
