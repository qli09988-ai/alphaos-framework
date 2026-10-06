import subprocess,pathlib,concurrent.futures,json,datetime,hashlib
P=pathlib.Path(__file__).resolve().parent
urls={
'szse_daily':'https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=scsj_fund_jjgm&TABKEY=tab1&txtStart=2026-08-31&txtEnd=2026-09-29&jjlb=ETF',
'szse_daily_json':'https://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=scsj_fund_jjgm&TABKEY=tab1&txtStart=2026-08-31&txtEnd=2026-09-29&jjlb=ETF&txtDMorJC=159039',
'cnindex_js':'https://www.cnindex.com.cn/js/pages/entry-index-detail.js',
'js_pcf_js':'https://www.igwfmc.com/front/js/main/english/etfpcf.js',
'js_pcf_js2':'https://www.igwfmc.com/main/english/etfpcf.js',
'js_qreport':'https://www.igwfmc.com/main/jjcp/159559/detail.html',
'js_holding_report':'https://fundf10.eastmoney.com/jjgg_159559_3.html',
'ha_latest_report':'https://fundf10.eastmoney.com/jjgg_159039_1.html',
}
def f(x):
 k,u=x;r=subprocess.run(['curl','-L','-sS','--max-time','22','-A','Mozilla/5.0','-e','https://www.szse.cn/market/fund/volume/etf/index.html',u],capture_output=True);(P/(k+'.txt')).write_bytes(r.stdout)
 return dict(id=k,url=u,bytes=len(r.stdout),captured_at=datetime.datetime.now().isoformat(),sha256=hashlib.sha256(r.stdout).hexdigest(),preview=r.stdout[:80].decode(errors='replace'))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:res=list(ex.map(f,urls.items()))
(P/'manifest_more.json').write_text(json.dumps(res,ensure_ascii=False,indent=2));print(json.dumps(res,ensure_ascii=False))
