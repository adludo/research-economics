#!/usr/bin/env python3
"""Render leisure and trade figures from committed aggregate extracts."""
import csv,json,os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR','/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import FuncFormatter,FixedLocator
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'public/data/topic-graphs';OUT=ROOT/'public/charts/topic-graphs'
P=json.loads((DATA/'provenance.json').read_text());ARCHIVE='https://github.com/owid/owid-datasets/tree/6155d4ca1ea14ef30e753010a25521eeb416e8a2/datasets'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#cbd5e1','svg.fonttype':'none','svg.hashsalt':'topic-graphs-v1'})
def rows(name):
 with (DATA/name).open() as f:return list(csv.DictReader(f))
def style(ax):ax.grid(color='#e2e8f0',linewidth=.7);ax.set_axisbelow(True)
def finish(fig,name,description,keys,pwt=False):
 fig.text(.09,.115,description,fontsize=9,color='#475569')
 fig.text(.09,.085,'Retrieved from: '+ARCHIVE,fontsize=7.8,url=ARCHIVE,color='#475569')
 for i,(key,label) in enumerate(keys):fig.text(.09+i*.29,.055,label,fontsize=9,url=P['sources'][key]['url'],color='#155e75')
 note='PWT archive label10.0; version discrepancy noted on page. ' if pwt else ''
 fig.text(.09,.025,f"Retrieved {P['retrieved_date_utc']}. {note}Descriptive, not causal. Lines connect observations, not added estimates.",fontsize=8,color='#475569')
 OUT.mkdir(parents=True,exist_ok=True)
 fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Date':None});fig.savefig(OUT/(name+'.png'),facecolor='white',dpi=170);plt.close(fig)
def main():
 us=rows('us-leisure.csv');groups=['Ages 14+ (total)','Ages 14-17 (total)','Ages 18-24 (total)','Ages 25-54 (total)','Ages 55-64 (total)','Ages 65+ (total)']
 fig,axes=plt.subplots(2,3,figsize=(12,8));fig.subplots_adjust(left=.09,right=.97,top=.85,bottom=.25,hspace=.48,wspace=.28)
 fig.suptitle('US leisure over a century: different age-group paths',x=.09,y=.97,ha='left',fontsize=18,fontweight='bold');fig.text(.09,.91,'Residual leisure estimates • hours per week • total-sex groups • 1900–2005',fontsize=11)
 for ax,g in zip(axes.flat,groups):
  r=sorted([x for x in us if x['group']==g],key=lambda x:int(x['year']));ax.plot([int(x['year'])for x in r],[float(x['leisure_hours_week'])for x in r],marker='o',color='#155e75',linewidth=2,markersize=3);ax.set_title(g.replace(' (total)',''),loc='left');ax.set_ylim(0,80);ax.set_xlim(1895,2010);ax.set_xticks([1900,1950,2005]);style(ax)
 finish(fig,'us-leisure','Source: Ramey & Francis (2009), via OWID. Residual subtracts work, school, home production, commuting and personal care.',[('us.csv','Ramey–Francis archive CSV')])
 n=rows('norway-leisure.csv');fig,ax=plt.subplots(figsize=(11,6.5));fig.subplots_adjust(left=.09,right=.97,top=.81,bottom=.29)
 fig.suptitle('Norway: leisure in the national time-use series',x=.09,y=.96,ha='left',fontsize=18,fontweight='bold');fig.text(.09,.89,'Minutes on an average day • recorded survey years, 1970–2010',fontsize=11)
 for sex,color,ls in [('all','#0f172a','-'),('female','#087f5b','--'),('male','#b45309','--')]:
  r=sorted([x for x in n if x['sex']==sex],key=lambda x:int(x['year']));ax.plot([int(x['year'])for x in r],[float(x['leisure_minutes_day'])for x in r],label=sex,marker='o',color=color,linestyle=ls)
 ax.set_ylim(0,480);ax.set_xticks([1970,1980,1990,2000,2010]);ax.set_ylabel('Leisure minutes/day');ax.legend(title='Source series');style(ax)
 finish(fig,'norway-leisure','Source: Statistics Norway via OWID. Archive normalizes activities to 1,440 minutes/day; age coverage not specified in metadata.',[('norway.csv','Statistics Norway archive CSV')])
 linked=rows('leisure-productivity.csv');fig,axes=plt.subplots(1,2,figsize=(12,7));fig.subplots_adjust(left=.09,right=.97,top=.80,bottom=.29,wspace=.3)
 fig.suptitle('Leisure and output per hour: two separate definitions',x=.09,y=.96,ha='left',fontsize=17,fontweight='bold');fig.text(.09,.89,'Exact-year aggregate matches • different populations and leisure units • no fitted causal effect',fontsize=10)
 for ax,c,fieldlabel in zip(axes,['Norway','United States'],['Daily leisure, minutes (national all-sex series)','Weekly residual leisure, hours (age14+)']):
  r=sorted([x for x in linked if x['country']==c],key=lambda x:int(x['year']));ax.plot([float(x['output_per_hour_2017_ppp'])for x in r],[float(x['leisure'])for x in r],marker='o',color='#155e75');ax.set_title(c,loc='left');ax.set_xlabel('Output/hour (2017 PPP international $)');ax.set_ylabel(fieldlabel);ax.set_xlim(0,120);ax.set_ylim(0,480 if c=='Norway' else 80);style(ax)
  for x in r:ax.annotate(x['year'],(float(x['output_per_hour_2017_ppp']),float(x['leisure'])),xytext=(4,5),textcoords='offset points',fontsize=8)
 finish(fig,'leisure-productivity','Sources: Norway / Ramey–Francis leisure; PWT output GDP, persons engaged, annual hours. Separate y-scales; not individual effects.',[('norway.csv','Norway leisure CSV'),('us.csv','US leisure CSV'),('pwt.csv','PWT macro CSV')],True)
 trade=rows('trade-income.csv');countries=['Australia','United States','United Kingdom','France','Japan','China','India','Brazil'];norm=Normalize(1970,2014)
 fig,axes=plt.subplots(2,4,figsize=(14,8));fig.subplots_adjust(left=.07,right=.97,top=.75,bottom=.26,wspace=.3,hspace=.45)
 fig.suptitle('Merchandise exports and income: country paths',x=.09,y=.97,ha='left',fontsize=18,fontweight='bold');fig.text(.09,.91,'Exports/GDP (%) per documented source formula • real GDP/person on log axis • 1970–2014',fontsize=11)
 cb=fig.add_axes([.69,.845,.25,.012]);fig.colorbar(ScalarMappable(norm=norm,cmap='viridis'),cax=cb,orientation='horizontal',ticks=[1970,1990,2014]).set_label('Year')
 for ax,c in zip(axes.flat,countries):
  r=sorted([x for x in trade if x['country']==c],key=lambda x:int(x['year']));x=[float(v['gdp_per_person_2017_ppp'])for v in r];y=[float(v['merchandise_exports_pct_gdp'])for v in r];ax.plot(x,y,color='#94a3b8',linewidth=1);ax.scatter(x,y,c=[int(v['year'])for v in r],norm=norm,cmap='viridis',s=10);ax.set_title(c,loc='left',fontsize=11);ax.set_xscale('log');ax.set_xlim(1000,100000);ax.set_ylim(0,60);ax.xaxis.set_major_locator(FixedLocator([1000,10000,100000]));ax.xaxis.set_major_formatter(FuncFormatter(lambda v,_:f'{v/1000:g}k'));ax.minorticks_off();style(ax)
 fig.text(.5,.205,'Horizontal: GDP/person (2017 PPP $); vertical: merchandise exports as % of source GDP',ha='center',fontsize=10)
 finish(fig,'trade-income','Sources: Fouquin & Hugot / CEPII (2016), via OWID; PWT. Export formula used despite archive column label “total trade”.',[('trade.csv','CEPII export-share CSV'),('pwt.csv','PWT macro CSV')],True)
 fig,axes=plt.subplots(2,4,figsize=(14,8));fig.subplots_adjust(left=.08,right=.97,top=.84,bottom=.25,wspace=.3,hspace=.35)
 fig.suptitle('Export shares and GDP per person through time',x=.09,y=.97,ha='left',fontsize=18,fontweight='bold');fig.text(.09,.91,'Separate units and common scales within each row • four illustrative economies',fontsize=11)
 for col,c in enumerate(['United States','France','China','India']):
  r=sorted([x for x in trade if x['country']==c],key=lambda x:int(x['year']))
  for row,key in enumerate(['merchandise_exports_pct_gdp','gdp_per_person_2017_ppp']):
   ax=axes[row,col];ax.plot([int(x['year'])for x in r],[float(x[key])for x in r],color=['#087f5b','#155e75'][row],linewidth=2);ax.set_xlim(1968,2016);ax.set_xticks([1970,1990,2014]);style(ax)
   if row==0:ax.set_ylim(0,60);ax.set_title(c,loc='left',fontsize=12)
   else:ax.set_yscale('log');ax.set_ylim(1000,100000);ax.yaxis.set_major_locator(FixedLocator([1000,10000,100000]));ax.yaxis.set_major_formatter(FuncFormatter(lambda v,_:f'{v/1000:g}k'));ax.minorticks_off()
   if col==0:ax.set_ylabel('Merchandise exports/GDP (%)'if row==0 else'GDP/person (2017 PPP $, log)')
 finish(fig,'trade-time-paths','Sources: Fouquin & Hugot / CEPII (2016), via OWID; PWT. Export share is not exports plus imports or a trade-policy measure.',[('trade.csv','CEPII export-share CSV'),('pwt.csv','PWT macro CSV')],True)
 print('Wrote five source-referenced SVG/PNG figures')
if __name__=='__main__':main()
