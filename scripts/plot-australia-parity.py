#!/usr/bin/env python3
"""Reproduce two age/parity/state graphs from a checksum-pinned Census archive."""
import csv,hashlib,json,io,os,argparse
from pathlib import Path
from urllib.request import urlopen
os.environ.setdefault('MPLCONFIGDIR','/tmp/research-economics-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'public/data/australia-family-jobs'
OUT=ROOT/'public/charts/australia-family-jobs'
STATES=['New South Wales','Victoria','Queensland','South Australia','Western Australia','Tasmania','Northern Territory','Australian Capital Territory']
AGES=['25-29','30-34','35-39','40-44','45-49','50-54','55-59']
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'australia-parity-v1','font.family':'DejaVu Sans','font.size':10})
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input-cache',type=Path);a=p.parse_args()
 spec=json.loads((DATA/'graph-sources.json').read_text())
 b=a.input_cache.read_bytes() if a.input_cache else urlopen(spec['url'],timeout=60).read()
 assert hashlib.sha256(b).hexdigest()==spec['sha256']
 raw=list(csv.DictReader(io.StringIO(b.decode()),delimiter='\t'))
 selected=[];lookup={}
 for state in STATES:
  for age in AGES:
   r=[x for x in raw if x['STE_NAME21']==state and x['Age5yr']==age]
   assert len(r)==8 and {x['ChildrenEverBorn'] for x in r}=={'','0','1','2','3','4','5','6'}
   v={x['ChildrenEverBorn']:int(x['females']) for x in r};total=sum(v.values());stated=total-v['']
   lookup[state,age]=v
   selected.append({'state':state,'age':age,**{('not_stated' if k=='' else 'births_'+('6_plus' if k=='6' else k)):v[k] for k in ['0','1','2','3','4','5','6','']},'total_cells':total,'stated_total':stated,'two_plus_pct_stated':100*sum(v[k] for k in ['2','3','4','5','6'])/stated})
 DATA.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
 (DATA/'parity-source.tsv').write_bytes(b)
 with (DATA/'parity-summary.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(selected[0]),lineterminator='\n');w.writeheader();w.writerows(selected)
 def footer(fig):
  fig.text(.08,.105,'ABS Census 2021 G28 • retrieved from github.com/HughParsonage/Census2021.DataPack • revision 2cb8412',fontsize=8,url=spec['url'])
  fig.text(.08,.075,'STE__Age5yr_ChildrenEverBorn.tsv • Retrieved 11 November 2026 • Original ABS agreement unverified',fontsize=8)
  fig.text(.08,.045,'Downloads, definitions and exact retrieval URL: /data/australia-families-jobs/#graphs-of-available-joint-data',fontsize=8,url='/data/australia-families-jobs/#graphs-of-available-joint-data')
 def save(fig,name):
  footer(fig);fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor='white')
  q=OUT/(name+'.svg');q.write_text('\n'.join(x.rstrip() for x in q.read_text().splitlines())+'\n')
  fig.savefig(OUT/(name+'.png'),dpi=150,facecolor='white');plt.close(fig)
 fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.23,right=.88,bottom=.23,top=.81)
 fig.suptitle('Women reporting at least two children ever born, 2021',x=.08,y=.96,ha='left',fontsize=18,fontweight='bold')
 fig.text(.08,.895,'Share among women stating a child count • Age at Census, not age at birth • Not resident family size',fontsize=10)
 mat=np.array([[next(r['two_plus_pct_stated'] for r in selected if r['state']==s and r['age']==age)for age in AGES]for s in STATES])
 im=ax.imshow(mat,vmin=0,vmax=100,cmap='Blues',aspect='auto');ax.set_yticks(range(8),STATES);ax.set_xticks(range(7),AGES);ax.set_xlabel('Age group (years)')
 for i in range(8):
  for j in range(7):ax.text(j,i,f'{mat[i,j]:.1f}%',ha='center',va='center',color='white' if mat[i,j]>55 else '#102a43',fontsize=9)
 fig.colorbar(im,ax=ax,pad=.025,label='% of women with stated child count');save(fig,'two-plus-by-age-state')
 fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.23,right=.97,bottom=.23,top=.75)
 fig.suptitle('Children ever born to women aged 45–49, 2021',x=.08,y=.96,ha='left',fontsize=18,fontweight='bold')
 fig.text(.08,.895,'All women in this age group, including not stated • Women, including zero births • Not a count of resident children',fontsize=10)
 left=np.zeros(8)
 for k,label,color in zip(['0','1','2','3','4','5','6',''],['0','1','2','3','4','5','6+','Not stated'],['#e4eaf1','#94bfd1','#087e8b','#3859a8','#7660a5','#bd6a84','#d88b38','#b8b8b8']):
  vals=np.array([100*lookup[s,'45-49'][k]/sum(lookup[s,'45-49'].values())for s in STATES]);ax.barh(range(8),vals,left=left,label=label,color=color);left+=vals
 ax.set_yticks(range(8),STATES);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('Share of women in age/state group (%)');ax.legend(title='Children ever born',ncol=8,loc='lower center',bbox_to_anchor=(.5,1.02),frameon=False,fontsize=9)
 save(fig,'parity-45-49')
 print('56 complete age/state groups; 448 source cells; two figures')
if __name__=='__main__':main()
