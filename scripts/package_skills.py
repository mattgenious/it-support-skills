"""Generate flat harness skills from OS-first canonical owners. No hand-edited copies."""
import re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sources():
 result={}
 for p in sorted((ROOT/'skills').rglob('SKILL.md')):
  name=re.search(r'^name: ([a-z0-9-]+)$',p.read_text(),re.M).group(1)
  if name in result: raise ValueError('Duplicate skill name: '+name)
  result[name]=p
 return result
def rendered(p,owners):
 text=p.read_text()
 def link(m):
  dest=(p.parent/m.group(2)).resolve()
  for name,owner in owners.items():
   if owner.resolve()==dest:return '['+m.group(1)+'](../'+name+'/SKILL.md)'
  raise ValueError('Unresolved skill link: '+m.group(2))
 return re.sub(r'\[([^]]+)\]\(([^)]+SKILL\.md)\)',link,text)
def generate():
 owners=sources();out=ROOT/'plugins/it-support/skills'
 if out.exists():shutil.rmtree(out)
 for name,p in owners.items():
  target=out/name/'SKILL.md';target.parent.mkdir(parents=True)
  target.write_text(rendered(p,owners),encoding='utf-8')
 print('Generated',len(owners),'flat harness skills.')
if __name__=='__main__':generate()
