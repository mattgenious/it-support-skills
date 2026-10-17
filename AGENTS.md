# Library ownership

Canonical skills live in skills/<os>/<area>/<task>/SKILL.md. Cross-platform task
owners live in skills/shared/<task>/SKILL.md. OS SKILL.md files route only; an area
such as performance is not a skill. Each task has a concrete trigger and result.
Optional references, scripts and behavioral tests belong beside their task owner.
Do not create empty areas or invent capability merely to fill the tree.

plugins/it-support/skills is generated flat discovery output for harnesses. Edit
canonical owners, run python scripts/package_skills.py then scripts/validate.py.
Route across OS boundaries through relative links, never separately maintained
copies. Preserve public URLs only where needed; renamed initial skill paths are
listed in the root README migration table.

Write original vendor-neutral guidance; publish no customer data, credentials or
private infrastructure. Distinguish source-backed hypotheses from verified fixes.
A skill supplies judgment, not authority to change a machine.
