import importlib.util,pathlib,unittest
spec=importlib.util.spec_from_file_location('install',pathlib.Path(__file__).with_name('install.py')); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class MigrationTests(unittest.TestCase):
    def test_only_exact_legacy_search_path_removed(self):
        old="import sys\nsys.path.insert(0, '/root/.openclaw/workspace/ai-hedge-fund')\nsys.path.insert(0, '/another/path')\nsecret = 'private-value'\nimport tushare as ts\n"
        new=m.remove_legacy_path(old,pathlib.Path('/root/.openclaw/workspace/ai-hedge-fund'))
        self.assertEqual(new,"import sys\nsys.path.insert(0, '/another/path')\nsecret = 'private-value'\nimport tushare as ts\n")
    def test_no_rewrite_unrelated_file(self):
        text="import sys\n# retain formatting\nx = 1\n"
        self.assertEqual(m.remove_legacy_path(text,pathlib.Path('/legacy')),text)
    def test_roots_include_scoped_imports(self):
        self.assertEqual(m.roots('import json, os\ndef x():\n import pandas as pd\n from tushare.stock import cons\n'),['json','os','pandas','tushare'])
if __name__=='__main__': unittest.main()
