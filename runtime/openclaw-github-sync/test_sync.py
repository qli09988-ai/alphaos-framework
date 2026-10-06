import hashlib, importlib.util, json, pathlib, tempfile, unittest
spec = importlib.util.spec_from_file_location('sync', pathlib.Path(__file__).with_name('sync.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.ws = pathlib.Path(self.tmp.name)
        self.data = {n: ('fixture '+n).encode() for n in m.FILES}
        self.manifest = dict(schema_version=1, repository=m.REPO, approval_status='Human Approved', framework_version='v0.1', commit='a'*40, files={n:m.digest(d) for n,d in self.data.items()})
    def tearDown(self): self.tmp.cleanup()
    def fetch(self, url):
        return json.dumps(self.manifest).encode() if url==m.MANIFEST else self.data[url.rsplit('/',1)[1]]
    def test_success_and_idempotence(self):
        self.assertEqual(m.sync(self.ws,self.fetch)['state'],'CURRENT')
        target=(self.ws/'alphaos-framework/current').resolve()
        self.assertEqual(m.sync(self.ws,self.fetch)['path'],str(target))
        self.assertEqual(len(list((self.ws/'alphaos-framework/releases').iterdir())),1)
    def test_failure_does_not_switch_current(self):
        good=m.sync(self.ws,self.fetch)['path']; self.manifest['commit']='b'*40
        self.data['README.md']=b'corrupt'
        s=m.sync(self.ws,self.fetch)
        self.assertEqual(s['state'],'STALE_LAST_GOOD'); self.assertEqual(s['path'],good)
        self.assertEqual(s['commit'],'a'*40)
    def test_network_failure_without_snapshot(self):
        def fail(url): raise OSError('offline')
        self.assertEqual(m.sync(self.ws,fail)['state'],'UNAVAILABLE')
    def test_tampered_cache_is_not_fallback(self):
        s=m.sync(self.ws,self.fetch); (pathlib.Path(s['path'])/'README.md').write_text('tampered')
        def fail(url): raise OSError('offline')
        self.assertEqual(m.sync(self.ws,fail)['state'],'UNAVAILABLE')
    def test_path_traversal_and_unapproved_rejected(self):
        self.manifest['files']['../evil']='0'*64
        self.assertEqual(m.sync(self.ws,self.fetch)['state'],'UNAVAILABLE')
        del self.manifest['files']['../evil']; self.manifest['approval_status']='Testing'
        self.assertEqual(m.sync(self.ws,self.fetch)['state'],'UNAVAILABLE')
if __name__=='__main__': unittest.main()
