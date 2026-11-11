#!/usr/bin/env python3
"""Render the seven Australia figures from checked-in extracts, offline."""
import csv
import json
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', '/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/data/australia'
OUT = ROOT / 'public/charts/australia'
SOURCES = json.loads((DATA / 'sources.json').read_text())['sources']
NAMES = {'New South Wales': 'NSW', 'Victoria': 'VIC', 'Queensland': 'QLD', 'South Australia': 'SA', 'Western Australia': 'WA', 'Tasmania': 'TAS', 'Northern Territory': 'NT', 'Australian Capital Territory': 'ACT', 'Other Territories': 'Other territories'}
COLORS = ['#087e8b', '#3859a8', '#d57a25']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'text.color': '#102a43', 'axes.spines.top': False, 'axes.spines.right': False, 'axes.spines.left': False, 'svg.fonttype': 'none', 'svg.hashsalt': 'australia-v1'})

def load(name):
    return list(csv.DictReader((DATA / name).open()))

def base(title, subtitle, rows=1, height=7):
    fig, axs = plt.subplots(rows, 1, figsize=(12, height), squeeze=False)
    fig.suptitle(title, x=.08, y=.97, ha='left', fontsize=19, fontweight='bold')
    fig.text(.08, .915, subtitle, fontsize=10, color='#52667a')
    fig.subplots_adjust(left=.16, right=.96, top=.85, bottom=.20, hspace=.65)
    for ax in axs[:, 0]:
        ax.grid(axis='x', color='#e2e8f0', linewidth=.7)
        ax.set_axisbelow(True)
    return fig, list(axs[:, 0])

def footer(fig, kind, names, note):
    if kind == 'census':
        label = 'ABS Census 2021 • retrieved: github.com/HughParsonage/Census2021.DataPack • revision 2cb8412'
    elif kind == 'jobs':
        label = 'ABS employment workbook • retrieved: github.com/lehuukimlam/Aussie-Economy-Dashboard • revision c70a360'
    else:
        label = 'World Bank WDI • retrieved: github.com/open-numbers/ddf--world_bank--world_development_indicators • revision 4252d91'
    fig.text(.08, .105, label, fontsize=8, url=SOURCES[names[0]]['url'])
    fig.text(.08, .078, 'Files: ' + ', '.join(names), fontsize=8)
    fig.text(.08, .051, 'Retrieved 2026-11-11 • Original-provider agreement unverified • ' + note, fontsize=8, color='#52667a')
    fig.text(.08, .025, 'Exact retrieval URLs, checksums and downloads: /data/australia/ → Sources and reproduction', fontsize=8, url='/data/australia/#sources-and-reproduction')

def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / (name + '.svg'), facecolor='white', metadata={'Date': None})
    p = OUT / (name + '.svg')
    p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines()) + '\n')
    fig.savefig(OUT / (name + '.png'), facecolor='white', dpi=150)
    plt.close(fig)

p = load('census-population.csv')
f, (ax,) = base('Australia: population in the 2021 Census', 'Nine state/territory categories • Census count, not estimated resident population')
y = list(range(len(p)))
vals = [int(r['persons']) / 1e6 for r in p]
ax.barh(y, vals, color=COLORS[0]); ax.set_yticks(y, [NAMES[r['state']] for r in p]); ax.invert_yaxis()
ax.set_xlabel('People (millions)'); ax.set_xlim(0, max(vals) * 1.22)
for i, r in enumerate(p): ax.text(vals[i] + .06, i, f"{int(r['persons']):,}", va='center', fontsize=9)
footer(f, 'census', ['census-persons.tsv'], 'Other territories is a separate small category.')
save(f, 'population')

p = load('census-age.csv'); f, (ax,) = base('Age composition across Australia, 2021', 'Shares of the sum of age cells within each state/territory • ABS perturbation can affect totals')
left = [0.] * len(p)
for k, label, color in zip(['under_15', '15_to_64', '65_plus'], ['Under 15', '15–64', '65+'], COLORS):
    v = [100 * int(r[k]) / int(r['age_cell_total']) for r in p]
    ax.barh(y, v, left=left, label=label, color=color)
    for i, value in enumerate(v): ax.text(left[i] + value / 2, i, f'{value:.1f}%', ha='center', va='center', color='white', fontsize=9)
    left = [a+b for a,b in zip(left,v)]
ax.set_yticks(y, [NAMES[r['state']] for r in p]); ax.invert_yaxis(); ax.set_xlim(0,100); ax.set_xlabel('Share of age-cell population (%)'); ax.legend(loc='upper center', bbox_to_anchor=(.5,1.07), ncol=3, frameon=False)
footer(f, 'census', ['census-age.tsv'], 'Denominator comes from these age cells, not the separate persons table.')
save(f, 'age')

p = load('census-families.csv'); f, (ax,) = base('Families with children under 15, 2021', 'Counts of families, not counts of children • Other child age/status groups may also be present')
for offset, typ, label, color in [(-.18, 'couple', 'Couple families', COLORS[0]), (.18, 'one_parent', 'One-parent families', COLORS[1])]:
    r = [r for r in p if r['family_type'] == typ]
    ax.barh([i+offset for i in y], [int(a['families_with_under_15_children']) / 1000 for a in r], height=.34, label=label, color=color)
ax.set_yticks(y, list(NAMES.values())); ax.invert_yaxis(); ax.set_xlabel('Families (thousands)'); ax.legend(frameon=False, loc='lower right')
footer(f, 'census', ['census-families.tsv'], 'HasChild=1 only; the archived table omits couples without children.')
save(f, 'families')

annual = load('annual-indicators.csv')
def series(code):
    r = [r for r in annual if r['indicator'] == code]
    return [int(a['year']) for a in r], [float(a['value']) for a in r]

def line(ax, code, divisor=1, label=None, color=COLORS[0]):
    x, v = series(code)
    ax.plot(x, [n/divisor for n in v], label=label, color=color, linewidth=2)
    ax.scatter([x[-1]], [v[-1]/divisor], color=color, s=18)
    ax.set_xlim(2000,2026); ax.set_xticks([2000,2005,2010,2015,2020,2025]); ax.grid(axis='y', color='#e2e8f0', linewidth=.7)
    return v[-1]/divisor

f, axs = base('Australia: population and economic growth', 'Annual WDI archive values, 2000–2025 • Includes statistical estimates; no causal interpretation', rows=3, height=10)
for ax, code, div, label in zip(axs, ['sp_pop_totl', 'ny_gdp_mktp_kd', 'ny_gdp_mktp_kd_zg'], [1e6,1e9,1], ['Population (millions)', 'Real GDP (2015 US$ billions)', 'GDP growth (annual %)']):
    v = line(ax, code, div); ax.set_ylabel(label); ax.set_title(f'2025: {v:,.2f}', loc='right', fontsize=10)
axs[1].set_ylim(bottom=0); axs[0].set_ylim(bottom=0); axs[2].axhline(0,color='#52667a',linewidth=.7)
footer(f, 'wdi', ['sp_pop_totl.csv','ny_gdp_mktp_kd.csv','ny_gdp_mktp_kd_zg.csv'], 'Population estimates differ from Census counts.')
save(f, 'macro')

f, (ax,) = base('Australia: growth in broad economic sectors', 'Real value added, annual percentage change • Broad WDI sectors, not the 19 ABS industry divisions')
for code, label, color in zip(['nv_agr_totl_kd_zg','nv_ind_totl_kd_zg','nv_srv_totl_kd_zg'], ['Agriculture, forestry, fishing','Industry (including construction)','Services'], COLORS):
    line(ax, code, label=label, color=color)
ax.set_ylabel('Annual growth (%)'); ax.axhline(0,color='#52667a',linewidth=.7); ax.legend(frameon=False, fontsize=9, loc='upper center', bbox_to_anchor=(.5, 1.07), ncol=3)
footer(f, 'wdi', ['nv_agr_totl_kd_zg.csv','nv_ind_totl_kd_zg.csv','nv_srv_totl_kd_zg.csv'], 'Growth rates cannot be added to obtain GDP growth.')
save(f, 'sector-growth')

p = [r for r in load('industry-employment.csv') if r['date'] == '2025-05-01' and r['series_id'] != 'A84932381A']
p.sort(key=lambda r: float(r['employed_thousands']), reverse=True)
f, (ax,) = base('Australia: employment by industry', 'May 2025 • Seasonally adjusted employed persons • 19 industry divisions', height=10)
f.subplots_adjust(left=.37)
v = [float(r['employed_thousands']) for r in p]
ax.barh(range(19),v,color=COLORS[0]); ax.set_yticks(range(19), [r['industry'] for r in p], fontsize=9); ax.invert_yaxis(); ax.set_xlabel('Employed persons (thousands)'); ax.set_xlim(0,max(v)*1.2); ax.set_xticks([0, 500, 1000, 1500, 2000, 2500])
for i,a in enumerate(v): ax.text(a+20,i,f'{a:,.0f}',va='center',fontsize=8)
footer(f, 'jobs', ['industry-employment.xlsx'], 'People, not job positions or FTEs; adjusted divisions need not sum to the adjusted total.')
save(f, 'industry-employment')

f, axs = base('Australia: annual labour-market indicators', 'WDI / ILO modeled estimates, 2000–2025 • Two different denominators; not the monthly ABS series', rows=2, height=9)
for ax, code, label in zip(axs, ['sl_emp_totl_sp_zs','sl_uem_totl_zs'], ['Employment / population aged 15+ (%)','Unemployment / labour force (%)']):
    value=line(ax,code); ax.set_ylabel(label, fontsize=9); ax.set_title(f'2025: {value:.2f}%', loc='right', fontsize=10); ax.set_ylim(bottom=0)
footer(f, 'wdi', ['sl_emp_totl_sp_zs.csv','sl_uem_totl_zs.csv'], 'Archived ILO metadata: accessed 17 January 2026.')
save(f, 'labour-market')
