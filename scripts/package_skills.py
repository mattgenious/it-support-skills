"""Generate flat harness skills from OS-first canonical owners. No hand-edited copies."""
import re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sources():
 result={}
 for p in sorted((ROOT/'skills').rglob('SKILL.md')):
  name=re.search(r'^name: ([a-z0-9-]+)$',p.read_text(encoding='utf-8'),re.M).group(1)
  if name in result: raise ValueError('Duplicate skill name: '+name)
  result[name]=p
 return result
def rendered(p,owners):
 text=p.read_text(encoding='utf-8')
 def link(m):
  dest=(p.parent/m.group(2)).resolve()
  for name,owner in owners.items():
   if owner.resolve()==dest:return '['+m.group(1)+'](../'+name+'/SKILL.md)'
  raise ValueError('Unresolved skill link: '+m.group(2))
 return re.sub(r'\[([^]]+)\]\(([^)]+SKILL\.md)\)',link,text)
def packaged_files(owners):
 """Render owners and retain task-local references, scripts and license notices."""
 result={}
 for name,p in owners.items():
  result[name+'/SKILL.md']=rendered(p,owners).encode('utf-8')
  if len(p.relative_to(ROOT/'skills').parts)==2:continue
  for asset in sorted(p.parent.rglob('*')):
   if asset.is_file() and asset!=p:
    if asset.name=='SKILL.md':raise ValueError('Nested skill owner: '+str(asset))
    result[name+'/'+asset.relative_to(p.parent).as_posix()]=asset.read_bytes()
 return result

def generate():
 owners=sources();out=ROOT/'plugins/it-support/skills'
 files=packaged_files(owners)
 if out.exists():shutil.rmtree(out)
 for rel,content in files.items():
  target=out/rel;target.parent.mkdir(parents=True,exist_ok=True)
  target.write_bytes(content)
 print('Generated',len(owners),'flat harness skills with',len(files)-len(owners),'task assets.')
if __name__=='__main__':generate()
