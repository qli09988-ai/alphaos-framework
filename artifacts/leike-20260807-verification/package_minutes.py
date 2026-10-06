import csv, datetime as dt, hashlib, io, json, pathlib, zipfile
from decimal import Decimal as D
P=pathlib.Path(__file__).resolve().parent
M=P/'minute_evidence'
TZ=dt.timezone(dt.timedelta(hours=8))
a_doc=json.loads((M/'ths_1m_aug07.json').read_text());a=a_doc['data']
b_doc=json.loads((M/'ths_5m_aug07.json').read_text());b=b_doc['data']
c=json.loads((M/'sina_5m_aug07.json').read_text())
s_doc=json.loads((M/'ths_min_snapshot.json').read_text());s=s_doc['data']
def grid(start,end,step):
    out=[];v=dt.datetime.fromisoformat('2026-08-07T'+start)
    end=dt.datetime.fromisoformat('2026-08-07T'+end)
    while v<=end:out.append(v.strftime('%H:%M'));v+=dt.timedelta(minutes=step)
    return out
expected1=grid('09:30','11:30',1)+grid('13:01','15:00',1)
expected5=grid('09:35','11:30',5)+grid('13:05','15:00',5)
assert [x['时间'][11:16] for x in a]==expected1
assert [x['时间'][11:16] for x in b]==expected5
assert [x['day'][11:16] for x in c]==expected5
assert len(a)==241 and len(b)==len(c)==48
assert [dt.datetime.fromtimestamp(x['时间'],TZ).strftime('%H:%M') for x in s]==expected1
for rows in (a,b):
    for x in rows:
        assert x['最低价']<=min(x['开盘价'],x['收盘价'])<=max(x['开盘价'],x['收盘价'])<=x['最高价']
        assert x['成交量']>=0 and x['总金额']>=0
        assert all(v not in [4294967295,2147483648] for v in x.values() if isinstance(v,(int,float)))
    assert [rows[0]['开盘价'],max(x['最高价'] for x in rows),min(x['最低价'] for x in rows),rows[-1]['收盘价']]==[8.69,9.52,8.52,9.17]
previous='09:29'
for x in b:
    end=x['时间'][11:16];group=[r for r in a if previous<r['时间'][11:16]<=end];previous=end
    agg={'开盘价':group[0]['开盘价'],'最高价':max(r['最高价'] for r in group),'最低价':min(r['最低价'] for r in group),'收盘价':group[-1]['收盘价'],'成交量':sum(r['成交量'] for r in group),'总金额':sum(r['总金额'] for r in group)}
    assert all(x[k]==v for k,v in agg.items())
v=amt=0
for x,y in zip(a,s):
    v+=x['成交量'];amt+=x['总金额']
    assert (x['收盘价'],v,amt)==(y['价格'],y['成交量'],y['总金额'])
diff=[]
for x,y in zip(b,c):
    deltas={}
    for k,f in [('开盘价','open'),('最高价','high'),('最低价','low'),('收盘价','close'),('成交量','volume'),('总金额','amount')]:
        n=D(str(x[k]))-D(y[f])
        if n:deltas[f]={'ths':str(x[k]),'sina':y[f],'ths_minus_sina':str(n)}
    if deltas:diff.append({'time':x['时间'],'differences':deltas})
(M/'cross_source_differences.json').write_text(json.dumps(diff,ensure_ascii=False,indent=2))
price_fields={'open','high','low','close'}
price_diff_rows=sum(bool(price_fields.intersection(x['differences'])) for x in diff)
max_price_diff=max(abs(D(z['ths_minus_sina'])) for x in diff for k,z in x['differences'].items() if k in price_fields)
sina_v=sum(D(x['volume']) for x in c);sina_a=sum(D(x['amount']) for x in c)
verification={'date':'2026-08-07','timezone':'Asia/Shanghai','ths_1m_rows':241,'ths_5m_rows':48,'sina_5m_rows':48,'ths_snapshot_rows':241,'missing_expected_times':0,'duplicate_times':0,'ohlc_invariant_errors':0,'sentinel_errors':0,'ths_1m_to_5m_differences':0,'ths_snapshot_cumulative_differences':0,'daily_ohlc':[8.69,9.52,8.52,9.17],'ths_volume_shares':v,'ths_amount_cny':amt,'sina_volume_shares':str(sina_v),'sina_amount_cny':str(sina_a),'cross_source_price_diff_rows':price_diff_rows,'cross_source_max_price_diff':str(max_price_diff),'sina_volume_shortfall_pct':str((D(v)-sina_v)/D(v)*100),'sina_amount_shortfall_pct':str((D(amt)-sina_a)/D(amt)*100),'zero_volume_minutes':[r['时间'] for r in a if r['成交量']==0]}
(M/'minute_verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2))
def save_csv(name,fields,rows):
    out=io.StringIO();w=csv.writer(out,lineterminator='\n');w.writerow(fields);w.writerows(rows);(M/name).write_text(out.getvalue())
fields=['time_Asia_Shanghai','open_CNY','high_CNY','low_CNY','close_CNY','volume_shares','amount_CNY']
for name,rs in [('ths_1m_aug07.csv',a),('ths_5m_aug07.csv',b)]:
    save_csv(name,fields,[[x['时间']]+[f"{x[k]:.2f}" for k in ['开盘价','最高价','最低价','收盘价']]+[x['成交量'],x['总金额']] for x in rs])
save_csv('sina_5m_aug07.csv',fields,[[x['day']+'+08:00']+[x[k] for k in ['open','high','low','close','volume','amount']] for x in c])
save_csv('ths_snapshot_aug07.csv',['time_Asia_Shanghai','price_CNY','cumulative_volume_shares','cumulative_amount_CNY','outer_volume_raw','inner_volume_raw'],[[dt.datetime.fromtimestamp(x['时间'],TZ).isoformat(),x['价格'],x['成交量'],x['总金额'],x['外盘成交量'],x['内盘成交量']] for x in s])
events=[x for x in a if x['时间'][11:16] in ['14:10','14:15','14:16','14:20','14:24','14:25','14:26','14:31','14:40','14:55','15:00']]
event_table='| K线时间标签 | 开 | 高 | 低 | 收 | 成交量（股） |\n|---|---:|---:|---:|---:|---:|\n'
for x in events:event_table+='| '+' | '.join([x['时间'][11:16]]+[f"{x[k]:.2f}" for k in ['开盘价','最高价','最低价','收盘价']]+[str(x['成交量'])])+' |\n'
five_table='| K线时间标签 | 开 | 高 | 低 | 收 | 成交量（股） | 成交额（元） |\n|---|---:|---:|---:|---:|---:|---:|\n'
for x in b:five_table+='| '+' | '.join([x['时间'][11:16]]+[f"{x[k]:.2f}" for k in ['开盘价','最高价','最低价','收盘价']]+[str(x['成交量']),str(x['总金额'])])+' |\n'
supp=f'''# 雷科防务2026-08-07历史分钟数据补充核验（v2）

**FACT：本轮已取得覆盖全天的1分钟、5分钟记录，原报告“完整分钟数据MISSING”状态被本补充取代。** 采用同花顺行情经社区SDK thsdk 1.7.18游客接口取得的241条1分钟记录和48条5分钟记录；另取得新浪48条5分钟记录、同花顺241条累计分时记录。通过时段覆盖、日线汇总及同源一致性检查，可用于本次分钟级结构核验；不等于交易所逐笔认证，也不宣称跨源逐条完全一致。

## FACT｜来源、抓取、单位与完整性

- 同花顺1分钟：`klines(USZA002413, interval=1m, adjust='')`，抓取{a_doc['captured_at']}。
- 同花顺5分钟：`klines(USZA002413, interval=5m, adjust='')`，抓取{b_doc['captured_at']}。
- 同花顺历史分时：`min_snapshot(USZA002413, date=20260807)`，抓取{s_doc['captured_at']}。此表成交量/金额为累计值，不能再次按行相加；内外盘字段保留原值但不用于本次判断。
- [SDK包版本与来源](https://pypi.org/project/thsdk/1.7.18/)。这是社区SDK访问的行情，不将SDK文档等同于交易所说明。
- [新浪5分钟原始请求](https://quotes.sina.cn/cn/api/jsonp_v2.php/=/CN_MarketDataService.getKLineData?symbol=sz002413&scale=5&ma=no&datalen=1970)，抓取2026-09-27T20:19:47+08:00。[AKShare对应接口说明](https://akshare.akfamily.xyz/data/stock/stock.html#id13)。保留未复权原始返回，未执行调整。
- 日期均严格筛选2026-08-07，时区Asia/Shanghai，价格元/股；**分钟成交量单位为股，日线表单位为手**；分钟成交额元。同花顺价格不复权。
- 1分钟时间标签：09:30—11:30共121条，13:01—15:00共120条，合计241条；含09:30开盘时点记录。5分钟09:35—11:30、13:05—15:00，各24条，合计48条。时间戳唯一，预期网格无缺失。14:59成交量为0，原样保留，不视为漏行。
- SDK日期参数没有把返回范围严格限制为单日：1分钟原返12,050条、5分钟9,936条，已按返回时间戳本地筛出目标日。打包与交接仅含目标日数据，未把其他日期混入分析。

## CALCULATION｜一致性检查与明确差异

1. 同花顺1分钟和5分钟各自汇总得到开8.69、高9.52、低8.52、收9.17，与腾讯/搜狐日线一致。
2. 同花顺1分钟归并5分钟，48组OHLCV及成交额**全部一致**；09:30开盘记录纳入第一组。1分钟累计量额、每分钟收盘价与241条历史分时记录**全部一致**。这些是同源检查，不是三份独立证据。
3. 同花顺全天量166,164,370股，折1,661,643.70手，与日线显示1,661,644手的整数舍入一致；总金额1,492,756,000元，与搜狐149,275.61万元相差100元。不要把供应商显示精度提升为元级无误。
4. 新浪5分钟完整48条，汇总OHLC同样为8.69/9.52/8.52/9.17，9.52也位于14:20标签的5分钟K线。
5. **跨源并非逐条一致：**48条中33条至少一个OHLC字段不同，最大价差0.02元；成交量47条不同，成交额48条不同。新浪全天量166,104,168股，比同花顺少60,202股（约{verification['sina_volume_shortfall_pct'][:7]}%）；金额1,492,242,134.9144元，比同花顺少513,865.0856元（约{verification['sina_amount_shortfall_pct'][:7]}%）。差异原因未获供应商解释，不擅自归因为复权、竞价或延迟。主分析统一使用同花顺，新浪仅用于交叉印证整体形态、时段和日内极值；逐条差异另附JSON。

## FACT｜关键分钟路径（采用供应商K线时间标签）

{event_table}
时间标签按供应商bar标记读取；14:20分钟K线包含最高9.52，不代表成交恰好发生在14:20:00，更不能给出秒级峰值时间。

## CALCULATION｜由分钟数据支持的结构

- 14:15标签的分钟K线首次覆盖并收于9.18上方：高9.27、收9.22；14:16收9.36。9.18没有阻止这一轮向上穿越。
- 14:20标签的分钟K线冲至全天高9.52，收9.49；随后14:21—14:24分钟收盘依次为9.44、9.37、9.32、9.22，回到9.10—9.25带内。14:20与14:24的标签相差4分钟，不将其写成秒级精确回落耗时。
- 14:25回升收9.27，14:26收9.19；14:31低9.14、收9.16。之后14:40与14:45的5分钟收盘均9.23，15:00收9.17。回落路径包含反弹，不是从最高点一路单调下跌。
- 高点9.52至最终9.17回落3.68%，与日线一致。分时记录不能证明9.18价位的真实挂单卖压、成交密集程度或参与者意图。

## INFERENCE｜对9.18假设的修正

结论仍为 **PARTIALLY SUPPORTED**。9.10—9.25可作为历史候选参考带；8/06、8/10的日内受阻线索仍在。但8/07更准确的表述是：**午后穿越9.18并上冲9.52，随后回落至9.18附近震荡，收9.17。** 9.18在当日既被向上穿越，又成为回落后的价格附近区域，不能把它单独描述成当天上冲无法越过的硬压力线。

## MISSING EVIDENCE｜仍未解决的部分

MISSING：峰值逐笔成交的秒级时间、逐笔全量成交/委托与撤单、9.18价位实际停留时长/成交密集度、两家分钟数据差异的官方解释，以及同花顺1分钟逐条对应的第二家独立1分钟源。完整分钟记录已取得，以上剩余缺口不能混写成“分钟数据全缺失”。

## FACT｜来源尝试记录

原服务器连接无法用现有认证进入，因此未在远程执行SDK；改用本地已有1.7.18组件游客模式成功。未读取用户交易账户。首轮东方财富分钟请求为空响应；本轮使用同花顺及新浪成功取得目标日数据后，已无需依赖该失败接口。未付费购买数据。

## FACT｜全天同花顺5分钟明细

{five_table}
完整241条1分钟、48条同花顺5分钟、48条新浪5分钟、241条累计分时均另附CSV与原始目标日JSON；检查结果`minute_verification.json`；逐条差异`cross_source_differences.json`。无插值、无人工补K线、无跨源平均。
'''
(P/'雷科防务_0807分钟数据补充核验.md').write_text(supp)
main=P/'雷科防务_9.18压力假设核验.md'
baseline=P/'雷科防务_9.18压力假设核验_v1_分钟补查前.md'
if not baseline.exists():baseline.write_text(main.read_text())
original=baseline.read_text()
begin=original.index('## MISSING EVIDENCE｜历史分钟结构')
end=original.index('## INFERENCE｜为何仅为PARTIALLY SUPPORTED',begin)
replacement='''## FACT / MISSING EVIDENCE｜分钟数据状态更新（v2）

2026-09-27第二轮已取得同花顺全天241条1分钟、48条5分钟和241条累计分时，以及新浪48条5分钟。原“完整分钟序列MISSING”已解除。网格完整；同花顺分钟汇总与日线OHLC一致，同源1分合5分及累计分时均对齐。跨源33/48条5分OHLC存在最多0.02元差异，已逐条记录。

14:15标签分钟K线首次覆盖并收在9.18上方；14:20标签分钟K线高9.52；14:24收9.22，14:31收9.16，最终收9.17。应描述为“向上穿越9.18后冲至9.52，再回落至9.18附近”。标签时刻不等于峰值成交秒级时刻。

详见同目录《雷科防务_0807分钟数据补充核验.md》和minute_evidence内完整目标日数据。MISSING仍包括逐笔成交/委托、峰值秒级时刻、真实价位成交密集度及跨源差异原因。

'''
updated=original[:begin]+replacement+original[end:]
updated=updated.replace('缺少完整分钟数据，无法识别卖压的具体位置与持续性；','已取得完整分钟记录，但缺少逐笔/委托证据，无法确认9.18卖压的具体位置与持续性；')
updated=updated.replace('# 雷科防务（002413）9.18元附近压力假设核验','# 雷科防务（002413）9.18元附近压力假设核验（v2：已补分钟数据）',1)
main.write_text(updated)
names=[main.name,'雷科防务_0807分钟数据补充核验.md','daily_verified.csv','verification.json','source_manifest.json','tencent_daily_unadjusted.json','tencent_daily.json','sohu_daily.json']
names+=['minute_evidence/'+n for n in ['ths_1m_aug07.csv','ths_5m_aug07.csv','sina_5m_aug07.csv','ths_snapshot_aug07.csv','ths_1m_aug07.json','ths_5m_aug07.json','sina_5m_aug07.json','ths_min_snapshot.json','ths_attempt_log.json','sina_manifest.json','minute_verification.json','cross_source_differences.json']]
manifest={'created_at':dt.datetime.now(TZ).isoformat(),'scope':'002413 history verification; minute rows limited to 2026-08-07','files':[{'file':n,'bytes':(P/n).stat().st_size,'sha256':hashlib.sha256((P/n).read_bytes()).hexdigest()} for n in names]}
(P/'交接包_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
zip_path=P/'AlphaOS_雷科0807_日线与分钟完整证据包_v2.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for n in names+['交接包_manifest.json']:z.write(P/n,n)
prompt='''用户要求补查分钟数据并将具体数据全部打包交给「AlphaOS的chat窗口」审阅。本消息是对之前报告的v2补充交接：现已取得全天分钟记录，请以本消息替代原报告“分钟数据MISSING”的状态。结论仍为PARTIALLY SUPPORTED，不给买卖建议、不自动写Core。

交接为可直接读取的全文：更新后Markdown主报告、分钟补充报告、全部目标日CSV和完整校验/差异JSON。无需访问发送方本地文件即可审阅。原始目标日JSON与文件哈希另有本地ZIP留档；本消息提供其数值内容与来源信息。特别注意：分钟量单位为股，日线量单位为手；snapshot是累计量额；同源一致性不等于独立来源认证；跨源33/48条5分OHLC最多差0.02元，不能说逐条完全一致。请审阅并纠正原先将9.18视作8/07最高价的前提。

'''
prompt+='--- 主报告v2 Markdown全文 ---\n'+updated+'\n--- 分钟补充Markdown全文 ---\n'+supp
for name in ['ths_1m_aug07.csv','ths_5m_aug07.csv','sina_5m_aug07.csv','ths_snapshot_aug07.csv']:
    prompt+='\n\n--- 数据文件：'+name+'（全量） ---\n```csv\n'+(M/name).read_text()+'```\n'
for name in ['minute_verification.json','cross_source_differences.json']:
    prompt+='\n\n--- '+name+' ---\n```json\n'+(M/name).read_text()+'\n```\n'
(P/'发送至AlphaOS_chat_完整交接正文_v2.md').write_text(prompt)
print(json.dumps(verification,ensure_ascii=False,indent=2))
print('handoff_characters',len(prompt),'zip_bytes',zip_path.stat().st_size)
