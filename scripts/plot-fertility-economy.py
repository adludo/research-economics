#!/usr/bin/env python3
"""Plot matched historical fertility, GDP/person and working hours; no network needed."""
import csv
import json
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import FuncFormatter, MultipleLocator, FixedLocator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/fertility-economy'
OUT = ROOT / 'public/charts/fertility-economy'
PROVENANCE = json.loads((DATA / 'provenance.json').read_text())
COUNTRIES = PROVENANCE['selection']
FIRST, LAST = PROVENANCE['period']
ARCHIVE = 'https://github.com/owid/owid-datasets/tree/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#cbd5e1', 'text.color': '#0f172a',
                     'xtick.color': '#475569', 'ytick.color': '#475569',
                     'svg.fonttype': 'none', 'svg.hashsalt': 'fertility-economy-v1'})


def load():
    result = {}
    with (DATA / 'selected-country-years.csv').open() as file:
        for r in csv.DictReader(file):
            year = int(r['year'])
            if not FIRST <= year <= LAST:
                raise ValueError('Year outside historical plotting window')
            values = {key: float(r[key]) for key in
                      ['tfr_births_per_woman', 'gdp_per_person_2017_ppp', 'annual_hours_per_worker']}
            country = result.setdefault(r['country'], {})
            if year in country:
                raise ValueError('Duplicate plotted country-year')
            country[year] = values
    if set(result) != set(COUNTRIES):
        raise ValueError('Plot sample differs from provenance')
    return result


def source_footer(fig):
    # Source references are part of every exported SVG AND PNG, not just page captions.
    fig.text(.075, .079, 'Fertility: Gapminder v12 via OWID; GDP/hours: OWID PWT archive (label 10.0; values match CRAN 10.01).', fontsize=8.5, color='#475569')
    fig.text(.075, .058, 'Retrieved from: ' + ARCHIVE, fontsize=8, color='#475569', url=ARCHIVE)
    fig.text(.075, .037, 'Source CSVs: ', fontsize=8.5, color='#475569')
    fig.text(.16, .037, 'Gapminder fertility', fontsize=8.5, color='#155e75',
             url=PROVENANCE['sources']['gapminder.csv']['url'])
    fig.text(.31, .037, 'PWT GDP / population / hours', fontsize=8.5, color='#155e75',
             url=PROVENANCE['sources']['pwt.csv']['url'])
    fig.text(.075, .017, f"Retrieved {PROVENANCE['retrieved_date_utc']}; {FIRST}–{LAST} historical estimates only. Forecasts from 2015 excluded. Descriptive, not causal.", fontsize=8.5, color='#475569')


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f'{name}.svg', facecolor='white', metadata={'Date': None})
    fig.savefig(OUT / f'{name}.png', dpi=170, facecolor='white')
    plt.close(fig)


def runs(values):
    # Split at actual missing years; no connection or interpolation over absent rows.
    groups = []
    for year in sorted(values):
        if not groups or year != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(year)
    return groups


def relationship(series, field, name, title, xlabel, logarithmic):
    fig, axes = plt.subplots(4, 3, figsize=(12, 12.5))
    fig.subplots_adjust(left=.075, right=.97, bottom=.16, top=.85, hspace=.55, wspace=.24)
    norm = Normalize(FIRST, LAST)
    fig.suptitle(title, x=.075, y=.977, ha='left', fontsize=18, fontweight='bold')
    fig.text(.075, .941, '12 selected economies • same-year complete observations • first/last years labelled', fontsize=11, color='#475569')
    fig.text(.075, .883, 'Vertical axis: total fertility rate (births per woman)', fontsize=10, color='#475569')
    bar_ax = fig.add_axes([.66, .895, .28, .012])
    bar = fig.colorbar(ScalarMappable(norm=norm, cmap='viridis'), cax=bar_ax, orientation='horizontal', ticks=[FIRST, 1990, LAST])
    bar.set_label('Calendar year', fontsize=9, labelpad=1)
    bar.ax.tick_params(labelsize=9)
    for ax, country in zip(axes.flat, COUNTRIES):
        values = series[country]
        years = sorted(values)
        for group in runs(values):
            ax.plot([values[y][field] for y in group],
                    [values[y]['tfr_births_per_woman'] for y in group],
                    color='#94a3b8', linewidth=1, zorder=1)
        ax.scatter([values[y][field] for y in years],
                   [values[y]['tfr_births_per_woman'] for y in years],
                   c=years, norm=norm, cmap='viridis', s=12, zorder=2)
        ax.set_title(country, loc='left', fontsize=11, fontweight='bold')
        ax.set_ylim(0, 7)
        ax.yaxis.set_major_locator(MultipleLocator(2))
        if logarithmic:
            ax.set_xscale('log')
            ax.set_xlim(1000, 100000)
            ax.xaxis.set_major_locator(FixedLocator([1000, 10000, 100000]))
            ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:g}k'))
            ax.minorticks_off()
        else:
            ax.set_xlim(0, 3200)
            ax.xaxis.set_major_locator(FixedLocator([0, 1000, 2000, 3000]))
        ax.grid(color='#e2e8f0', linewidth=.6)
        ax.set_axisbelow(True)
        for year, offset, ha in [(years[0], (-4, 9), 'right'), (years[-1], (4, -11), 'left')]:
            ax.annotate(str(year), (values[year][field], values[year]['tfr_births_per_woman']),
                        xytext=offset, textcoords='offset points', ha=ha, fontsize=8,
                        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .8, 'pad': .5})
    fig.text(.52, .117, xlabel, ha='center', fontsize=11)
    source_footer(fig)
    save(fig, name)


def time_paths(series):
    examples = ['South Korea', 'China', 'Germany', 'United States']
    variables = [
        ('tfr_births_per_woman', 'Total fertility rate\n(births per woman)', '#087f5b'),
        ('gdp_per_person_2017_ppp', 'Real GDP per person\n(2017 PPP $, log scale)', '#155e75'),
        ('annual_hours_per_worker', 'Annual market hours\nper worker', '#b45309'),
    ]
    fig, axes = plt.subplots(3, 4, figsize=(14, 10.5))
    fig.subplots_adjust(left=.09, right=.975, bottom=.17, top=.86, hspace=.38, wspace=.26)
    fig.suptitle('Different time paths behind the relationships', x=.075, y=.975, ha='left', fontsize=19, fontweight='bold')
    fig.text(.075, .93, 'Four illustrative economies • separate units and common scales within each row • 1970–2014', fontsize=11, color='#475569')
    for col, country in enumerate(examples):
        values = series[country]
        for row, (field, label, color) in enumerate(variables):
            ax = axes[row, col]
            for group in runs(values):
                ax.plot(group, [values[y][field] for y in group], color=color, linewidth=2)
            ax.set_xlim(1968, 2016)
            ax.set_xticks([1970, 1990, 2014])
            ax.grid(color='#e2e8f0', linewidth=.6)
            ax.set_axisbelow(True)
            if row == 0:
                ax.set_title(country, loc='left', fontweight='bold', fontsize=12)
                ax.set_ylim(0, 7)
            elif row == 1:
                ax.set_yscale('log')
                ax.set_ylim(1000, 100000)
                ax.yaxis.set_major_locator(FixedLocator([1000, 10000, 100000]))
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:g}k'))
                ax.minorticks_off()
            else:
                ax.set_ylim(0, 3200)
                ax.set_xlabel('Year')
            if col == 0:
                ax.set_ylabel(label, labelpad=12)
    source_footer(fig)
    save(fig, 'country-time-paths')


def main():
    series = load()
    relationship(series, 'gdp_per_person_2017_ppp', 'fertility-gdp',
                 'Fertility and GDP per person: country paths',
                 'Real GDP per person (2017 PPP international dollars; logarithmic scale)', True)
    relationship(series, 'annual_hours_per_worker', 'fertility-hours',
                 'Fertility and working hours: country paths',
                 'Annual market hours per worker (linear scale)', False)
    time_paths(series)
    print('Wrote three source-referenced charts, each in SVG and PNG.')


if __name__ == '__main__':
    main()
