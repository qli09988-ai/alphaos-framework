import subprocess,concurrent.futures,json,pathlib,datetime,hashlib
P=pathlib.Path(__file__).resolve().parent
urls={}
for c in ['159039','159559','980022']:
 urls[c+'_tencent']='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sz'+c+',day,2026-02-01,2026-09-30,240,'
 urls[c+'_sohu']='https://q.stock.sohu.com/hisHq?code=cn_'+c+'&start=20260201&end=20260930&stat=1&order=A&period=d&rt=json'
 urls[c+'_eastmoney']='https://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.'+c+'&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61&klt=101&fqt=0&beg=20260201&end=20260930'
 if c!='980022':
  urls[c+'_flow']='https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?lmt=140&klt=101&secid=0.'+c+'&fields1=f1,f2,f3,f7&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63'
  urls[c+'_nav']='https://api.fund.eastmoney.com/f10/lsjz?fundCode='+c+'&pageIndex=1&pageSize=200&startDate=2026-02-01&endDate=2026-09-30'
  urls[c+'_holdings']='https://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code='+c+'&topline=100&year=2026&month=6'
urls['snapshot']='https://qt.gtimg.cn/q=sz159039,sz159559,sz980022'
urls['index_method']='https://www.cnindex.com.cn/docs/gz_980022.pdf'
urls['huaan_pcf']='https://www.huaan.com.cn/etf/159039/sgshqd.jsp'
urls['jingshun_product']='https://www.igwfmc.com/main/jjcp/product/159559.html'
def fetch(kv):
 k,u=kv
 try:
  r=subprocess.run(['curl','-L','--max-time','22','-sS','-A','Mozilla/5.0','-e','https://fundf10.eastmoney.com/',u],capture_output=True)
  (P/(k+('.pdf' if k=='index_method' else '.txt'))).write_bytes(r.stdout)
  return dict(id=k,url=u,status=r.returncode,bytes=len(r.stdout),sha256=hashlib.sha256(r.stdout).hexdigest(),captured_at=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),preview=r.stdout[:150].decode('utf-8',errors='replace') if k!='index_method' else '')
 except Exception as e:return dict(id=k,url=u,error=type(e).__name__)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:res=list(pool.map(fetch,urls.items()))
(P/'manifest.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
print(json.dumps(res,ensure_ascii=False,indent=2))
