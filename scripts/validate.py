"""Validate local skill discovery, marketplace targets and packaging only."""
import json,re
from pathlib import Path
r=Path(__file__).resolve().parents[1]
root=r/'plugins/it-support'
skills=list((root/'skills').glob('*/SKILL.md'))
assert len(skills)>=6
for p in skills:
 text=p.read_text(encoding='utf-8')
 assert text.startswith('---\n')
 assert re.search(r'^name: '+re.escape(p.parent.name)+r'$',text,re.M)
 assert re.search(r'^description: .+',text,re.M)
 assert ']('+str(p.relative_to(r)).replace('\\','/')+')' in (r/'README.md').read_text()
for p in r.rglob('*.json'):
 data=json.loads(p.read_text())
 if p.name=='marketplace.json':
  for item in data['plugins']:
   source=item['source']; path=source if isinstance(source,str) else source['path']
   assert (r/path).is_dir()
 if p.name=='plugin.json': assert (p.parent/('../skills' if p.parent.name.startswith('.') else 'skills')).is_dir()
assert (r/'LICENSE').read_text().startswith('MIT License')
print(f'Validated {len(skills)} skills and all local marketplace targets.')
