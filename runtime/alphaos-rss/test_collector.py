import importlib.util, json, pathlib, tempfile, unittest, urllib.error
spec=importlib.util.spec_from_file_location('collector',pathlib.Path(__file__).with_name('collector.py')); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
RSS=b'<rss version="2.0"><channel><item><title>AI news</title><link>https://example.com/a</link><guid>a</guid><pubDate>Tue, 06 Oct 2026 03:00:00 +0000</pubDate><description>news</description></item></channel></rss>'
ATOM=b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>AI second</title><id>b</id><link href="https://example.com/b"/><updated>2026-10-06T03:00:00Z</updated></entry></feed>'
class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.w=pathlib.Path(self.tmp.name)
        (self.w/'rss_feeds.txt').write_text('First,https://example.com/rss\nSecond,https://example.com/atom\n')
        (self.w/'alphaos-runtime/rss').mkdir(parents=True)
        m.dump(self.w/'alphaos-runtime/rss/legacy-ranking.json',{'risk_tags':['AI'],'high_priority_tags':[]})
    def tearDown(self): self.tmp.cleanup()
    def fetch(self,f): return RSS if f['name']=='First' else ATOM
    def test_rss_atom_and_dedup(self):
        self.assertEqual(m.run(self.w,self.fetch)['state'],'HEALTHY')
        s=m.run(self.w,self.fetch); self.assertEqual(s['stored_item_count'],2)
        items=json.loads((self.w/'alphaos-runtime/rss/snapshot.json').read_text())['items']
        self.assertEqual({i['provenance']['format'] for i in items},{'RSS2','Atom'})
        self.assertTrue(all(i['published_at']=='2026-10-06T03:00:00+00:00' for i in items))
    def test_partial_keeps_old_records_but_only_success_is_compatible(self):
        m.run(self.w,self.fetch)
        def partial(f):
            if f['name']=='Second': raise urllib.error.HTTPError(f['url'],404,'Not Found',{},None)
            return RSS
        s=m.run(self.w,partial); self.assertEqual(s['state'],'PARTIAL'); self.assertEqual(s['stored_item_count'],2)
        self.assertEqual(s['feed_errors'][0]['error'],'HTTP_404')
        alerts=json.loads((self.w/'rss_alerts.json').read_text()); self.assertEqual(len(alerts),1)
    def test_total_failure_preserves_archive(self):
        m.run(self.w,self.fetch)
        def fail(f): raise urllib.error.URLError('offline')
        s=m.run(self.w,fail); self.assertEqual(s['state'],'UNAVAILABLE'); self.assertEqual(s['stored_item_count'],2)
        self.assertEqual(json.loads((self.w/'rss_alerts.json').read_text()),[])
        self.assertIsNotNone(s['last_success_at'])
    def test_missing_date_is_not_fetch_date(self):
        f={'id':'x','name':'X','url':'https://example.com','host':'example.com'}
        items=m.parse(b'<rss><channel><item><title>AI</title><link>/x</link></item></channel></rss>',f,m.now())
        self.assertIsNone(items[0]['published_at']); self.assertEqual(items[0]['timestamp_status'],'MISSING')
    def test_html_and_entity_feeds_rejected(self):
        f={'id':'x','name':'X','url':'https://example.com','host':'example.com'}
        for data in (b'<html/>',b'<!DOCTYPE rss><rss><channel/></rss>'):
            with self.assertRaises(ValueError): m.parse(data,f,m.now())
    def test_unconfigured_no_success_claim(self):
        (self.w/'rss_feeds.txt').write_text('bad line\n')
        s=m.run(self.w,self.fetch); self.assertEqual(s['state'],'UNAVAILABLE'); self.assertEqual(s['invalid_feed_lines'],1)
if __name__=='__main__': unittest.main()
