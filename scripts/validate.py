"""Check canonical placement, exact generated discovery and marketplace targets."""
import json,re
from pathlib import Path
from package_skills import ROOT,sources,rendered
owners=sources();assert owners, 'No canonical skills found'
out=ROOT/'plugins/it-support/skills'
os_names={'windows','linux','macos'}
routers={name:p for name,p in owners.items() if len(p.relative_to(ROOT/'skills').parts)==2}
assert {p.parent.name for p in routers.values()}==os_names, 'Each OS needs exactly one router'
assert set(routers)=={'route-'+os+'-support' for os in os_names}, 'Unexpected router name'
assert {p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()}=={name+'/SKILL.md' for name in owners}, 'Generated discovery differs from canonical owners'
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for name,p in owners.items():
 text=p.read_text(encoding='utf-8');assert text.startswith('---\n')
 assert re.search(r'^description: .+',text,re.M)
 rel=p.relative_to(ROOT/'skills').parts
 assert rel[0] in os_names|{'shared'}, 'Unknown OS/owner: '+str(p)
 if name in routers:
  assert len(rel)==2, 'Router must live directly below its OS'
 elif rel[0]=='shared':
  assert len(rel)==3 and rel[1]==name, 'Shared tasks need one named owner'
 else:
  assert len(rel)==4 and not name.startswith('route-'), 'OS tasks need area/task placement'
 assert (out/name/'SKILL.md').read_text(encoding='utf-8')==rendered(p,owners), 'Generated skill drift: '+name
 assert p.relative_to(ROOT).as_posix() in readme, 'README missing owner: '+name
 for dest in re.findall(r'\[[^]]+\]\(([^)]+)\)',text):
  if '://' not in dest and not dest.startswith('#'):
   assert (p.parent/dest.split('#')[0]).is_file(), 'Missing local reference: '+dest
for p in ROOT.rglob('marketplace.json'):
 for item in json.loads(p.read_text(encoding='utf-8'))['plugins']:
  source=item['source'];assert (ROOT/(source if isinstance(source,str) else source['path'])).is_dir()
versions=set()
for p in (ROOT/'plugins/it-support').rglob('plugin.json'):
 base=p.parent.parent if p.parent.name.startswith('.') else p.parent
 descriptor=json.loads(p.read_text(encoding='utf-8'))
 assert (base/descriptor['skills']).is_dir()
 versions.add(descriptor['version'])
assert len(versions)==1, 'Harness plugin versions differ'
assert (ROOT/'LICENSE').read_text(encoding='utf-8').startswith('MIT License')
print(f'Validated {len(owners)-len(routers)} task skills, {len(routers)} routers and exact generated marketplace packaging (version {versions.pop()}).')
