import datetime,importlib.util,pathlib,unittest
s=importlib.util.spec_from_file_location('query',pathlib.Path(__file__).with_name('query.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def test_failed_feed_with_no_articles_is_visible(self):
  snapshot={'feeds':[{'id':'r','name':'Reddit','state':'ERROR','error':'HTTP_429'}],'items':[]}
  out=m.health(snapshot);self.assertEqual(out['feeds'][0]['name'],'Reddit');self.assertEqual(out['feeds'][0]['error'],'HTTP_429');self.assertEqual(out['feeds'][0]['stored_items'],0)
 def test_filters_window_future_missing_and_deduplicates(self):
  at=datetime.datetime(2026,10,6,7,tzinfo=datetime.timezone.utc)
  items=[]
  for n,d,u in [('a','2026-10-06T06:00:00+00:00','same'),('b','2026-10-06T05:00:00+00:00','same'),('old','2025-01-01T00:00:00+00:00','old'),('future','2026-10-07T00:00:00+00:00','future'),('missing',None,'missing')]: items.append({'id':n,'published_at':d,'link':u,'title':'AI story','feed_id':'x'})
  out=m.news({'items':items,'feeds':[]},at=at);self.assertEqual(out['matching_unique_count'],1);self.assertEqual(out['items'][0]['id'],'a')
 def test_search_is_not_topic_inference(self):
  at=datetime.datetime(2026,10,6,7,tzinfo=datetime.timezone.utc)
  item={'id':'x','published_at':'2026-10-06T06:00:00+00:00','title':'Some unrelated crime news'}
  self.assertEqual(m.news({'items':[item]},search='AI',at=at)['returned_count'],0)
if __name__=='__main__': unittest.main()
