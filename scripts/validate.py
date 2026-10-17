"""Check canonical placement, exact generated discovery and marketplace targets."""
import json,re
from pathlib import Path
from package_skills import ROOT,sources,rendered
owners=sources();assert len(owners)==11
out=ROOT/'plugins/it-support/skills'
assert {p.parent.name for p in out.glob('*/SKILL.md')}==set(owners)
for name,p in owners.items():
 text=p.read_text();assert text.startswith('---\n')
 assert re.search(r'^description: .+',text,re.M)
 rel=p.relative_to(ROOT/'skills').parts
 assert rel[0] in ('shared','windows','linux','macos')
 assert len(rel)==2 if name.startswith('route-') else len(rel)==3 if rel[0]=='shared' else len(rel)==4
 assert (out/name/'SKILL.md').read_text()==rendered(p,owners), 'Generated skill drift: '+name
 assert str(p.relative_to(ROOT)).replace('\\','/') in (ROOT/'README.md').read_text()
for p in ROOT.rglob('marketplace.json'):
 for item in json.loads(p.read_text())['plugins']:
  source=item['source'];assert (ROOT/(source if isinstance(source,str) else source['path'])).is_dir()
for p in (ROOT/'plugins/it-support').rglob('plugin.json'):
 base=p.parent.parent if p.parent.name.startswith('.') else p.parent
 assert (base/json.loads(p.read_text())['skills']).is_dir()
assert (ROOT/'LICENSE').read_text().startswith('MIT License')
print('Validated 8 task skills, 3 routers and exact generated marketplace packaging.')
