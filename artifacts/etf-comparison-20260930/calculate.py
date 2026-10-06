import pathlib,json,re,datetime,math,statistics,csv
P=pathlib.Path(__file__).resolve().parent
D={};N={};summary={};verification={}
for c,nfile in [('159039','nav_js_a'),('159559','nav_js_b')]:
 s=(P/(nfile+'.txt')).read_text(encoding='utf-8-sig');a=json.loads(re.search(r'var Data_netWorthTrend\s*=\s*(.*?);',s).group(1));N[c]={datetime.datetime.fromtimestamp(x['x']/1000,datetime.timezone(datetime.timedelta(hours=8))).date().isoformat():x['y'] for x in a}
 print(c,'navs',len(N[c]),list(N[c].items())[-2:]);
for c in ['159039','159559','980022']:
 a=json.loads((P/(c+'_eastmoney.txt')).read_text())['data']['klines'];r=[x.split(',') for x in a];D[c]={x[0]:dict(date=x[0],open=float(x[1]),close=float(x[2]),high=float(x[3]),low=float(x[4]),volume_lots=float(x[5]),amount=float(x[6]),pct=float(x[8]),vendor_turnover=float(x[10])) for x in r if x[0]<='2026-09-29'}
 if c!='980022':
  t=json.loads((P/(c+'_tencent.txt')).read_text())['data']['sz'+c]['day'];diff=[]
  for x in t:
   if x[0] not in D[c]:continue
   d=D[c][x[0]]
   if any(abs(float(x[i])-d[k])>1e-7 for i,k in [(1,'open'),(2,'close'),(3,'high'),(4,'low')]):diff.append([x[0],x[1:5],[d[k] for k in ['open','close','high','low']]])
  verification[c]={'overlap':len([x for x in t if x[0] in D[c]]),'ohlc_differences':diff}
official_index=json.loads((P/'index_history_full.txt').read_text())['data']['data']
idxdiff=[]
for row in official_index:
 if row[0] not in D['980022']: continue
 d=D['980022'][row[0]]
 if abs(d['close']-row[5])>0.00501: idxdiff.append([row[0],d['close'],row[5]])
 d.update(close=row[5],high=row[2],open=row[3],low=row[4])
verification['980022']={'source':'CNI official daily history','close_differences_beyond_rounding':idxdiff,'overlap':len(official_index)}
for c in ['159039','159559']:
 shares={x[0]:float(x[3]) for x in json.loads((P/'shares_szse.json').read_text()) if x[1]==c}; flows={x.split(',')[0]:float(x.split(',')[1]) for x in json.loads((P/(c+'_flow.txt')).read_text())['data']['klines']};ds=sorted(shares);out=[]
 for i,date in enumerate(ds[1:],1):
  d=D[c][date].copy();nav=N[c][date];d.update(nav=nav,shares=shares[date],share_delta=shares[date]-shares[ds[i-1]]);d.update(aum=d['shares']*nav,estimated_net_subscription=d['share_delta']*nav,premium_pct=(d['close']/nav-1)*100,turnover_pct=d['volume_lots']*100/d['shares']*100,main_flow=flows.get(date));out.append(d)
 with (P/(c+'_20days.csv')).open('w') as f:w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
 (P/(c+'_20days.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2))
 summary[c]={'shares_start':shares[ds[0]],'shares_end':shares[ds[-1]],'shares_change':shares[ds[-1]]-shares[ds[0]],'net_sub_est':sum(d['estimated_net_subscription'] for d in out),'main_flow':sum(d['main_flow'] for d in out),'subscription_positive_days':sum(d['share_delta']>0 for d in out),'subscription_negative_days':sum(d['share_delta']<0 for d in out),'main_positive_days':sum(d['main_flow']>0 for d in out),'aum_end':out[-1]['aum'],'mean_turnover':statistics.mean(d['turnover_pct'] for d in out),'mean_abs_premium':statistics.mean(abs(d['premium_pct']) for d in out),'max_abs_premium':max(abs(d['premium_pct']) for d in out),'nav_return20':(N[c][ds[-1]]/N[c][ds[0]]-1)*100}
 print('\n'+c+' DAILY');print('\n'.join('|'+ '|'.join([d['date'][5:],f"{d['close']:.3f}",f"{d['pct']:+.2f}",f"{d['amount']/1e4:.2f}",f"{d['turnover_pct']:.2f}",f"{d['shares']/1e8:.6f}",f"{d['share_delta']/1e4:+.0f}",f"{d['aum']/1e8:.4f}",f"{d['estimated_net_subscription']/1e4:+.2f}",f"{d['premium_pct']:+.3f}",f"{d['main_flow']/1e4:+.2f}"])+'|' for d in out))
metrics=[]
for n in [20,60,120]:
 for c in ['159039','159559','980022']:
  dates=sorted(D[c]);dates=dates[-n-1:]
  if len(dates)<n+1:continue
  prices=[D[c][d]['close'] for d in dates];ret=[b/a-1 for a,b in zip(prices,prices[1:])];peak=prices[0];mdd=0
  for v in prices:peak=max(peak,v);mdd=min(mdd,v/peak-1)
  obj={'code':c,'days':n,'start':dates[0],'end':dates[-1],'price_return':(prices[-1]/prices[0]-1)*100,'vol_ann':statistics.stdev(ret)*math.sqrt(252)*100,'mdd':mdd*100,'avg_amount':statistics.mean(D[c][d]['amount'] for d in dates[1:])}
  if c in N and all(d in N[c] for d in dates):
   navs=[N[c][d] for d in dates];nr=[b/a-1 for a,b in zip(navs,navs[1:])];ir=[D['980022'][b]['close']/D['980022'][a]['close']-1 for a,b in zip(dates,dates[1:])];diff=[a-b for a,b in zip(nr,ir)];obj.update(nav_return=(navs[-1]/navs[0]-1)*100,nav_te=statistics.stdev(diff)*math.sqrt(252)*100,nav_mean_abs_td=statistics.mean(abs(v) for v in diff)*100,index_return=(D['980022'][dates[-1]]['close']/D['980022'][dates[0]]['close']-1)*100)
  metrics.append(obj)
summary['metrics']=metrics;summary['verification']=verification
for n in [20,60]:
 dates=sorted(D['159039'])[-n-1:];r=[]
 for c in ['159039','159559']:r.append([N[c][b]/N[c][a]-1 for a,b in zip(dates,dates[1:])])
 summary['nav_corr_'+str(n)]=statistics.correlation(*r)
(P/'calculations.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False,indent=2))
