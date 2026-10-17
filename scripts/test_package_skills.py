"""Protect flattened cross-owner routing and byte-exact task license delivery."""
import unittest
from pathlib import Path
from unittest.mock import patch
import package_skills


class PackagingContractTests(unittest.TestCase):
    def test_routes_flatten_while_task_assets_and_notices_survive(self):
        root = Path(__file__).resolve().parents[1]
        router = root / 'skills/windows/SKILL.md'
        task = root / 'skills/windows/printing/diagnose-print-failure/SKILL.md'
        shared = root / 'skills/shared/diagnose-network-path/SKILL.md'
        license_file = task.parent / 'LICENSE.upstream'
        provenance = task.parent / 'SOURCE.md'
        owners = {'route-windows-support': router,
                  'diagnose-windows-print-failure': task,
                  'diagnose-network-path': shared}
        texts = {
            router: 'Route [print](./printing/diagnose-print-failure/SKILL.md)',
            task: 'Use [network](../../../shared/diagnose-network-path/SKILL.md) and [source](SOURCE.md)',
            shared: 'Network owner',
        }
        notice = b'MIT notice\r\nCopyright\r\n'
        assets = {license_file: notice, provenance: b'[License](LICENSE.upstream)\n'}

        with patch.object(Path, 'read_text', lambda p, **kw: texts[p]), \
             patch.object(Path, 'read_bytes', lambda p: assets[p]), \
             patch.object(Path, 'rglob', lambda p, pattern: [q for q in [task, shared, *assets] if q.parent == p]), \
             patch.object(Path, 'is_file', return_value=True):
            actual = package_skills.packaged_files(owners)

        self.assertEqual(len(actual), 5)
        self.assertEqual(actual['diagnose-windows-print-failure/LICENSE.upstream'], notice)
        self.assertEqual(actual['diagnose-windows-print-failure/SOURCE.md'], assets[provenance])
        self.assertIn(b'(../diagnose-network-path/SKILL.md)', actual['diagnose-windows-print-failure/SKILL.md'])
        self.assertIn(b'(SOURCE.md)', actual['diagnose-windows-print-failure/SKILL.md'])
        self.assertIn(b'(../diagnose-windows-print-failure/SKILL.md)', actual['route-windows-support/SKILL.md'])


if __name__ == '__main__':
    unittest.main()
