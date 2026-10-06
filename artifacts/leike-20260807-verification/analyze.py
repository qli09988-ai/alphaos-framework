import csv
import datetime as dt
import json
import pathlib
from decimal import Decimal as D

P = pathlib.Path(__file__).resolve().parent
sohu = json.loads((P/'sohu_daily.json').read_bytes().decode('gb18030'))[0]['hq']
tx = json.loads((P/'tencent_daily_unadjusted.json').read_text())['data']['sz002413']['day']
qfq = json.loads((P/'tencent_daily.json').read_text())['data']['sz002413']['qfqday']
assert len(sohu) == len(tx) == len(qfq) == 49
assert len({r[0] for r in tx}) == 49
assert [r[0] for r in sohu] == [r[0] for r in tx]
assert tx == qfq
rows=[]
volume_differences=[]
for s,t in zip(sohu,tx):
    assert [D(s[i]) for i in (1,2,6,5)] == [D(t[i]) for i in (1,2,3,4)]
    date,o,c,h,l,v=t[:6]
    o,c,h,l,v=map(D,(o,c,h,l,v))
    assert l <= min(o,c) <= max(o,c) <= h
    if D(s[7]) != v:
        volume_differences.append(dict(date=date,sohu_lots=s[7],tencent_lots=str(v)))
    rows.append(dict(date=date,open=o,high=h,low=l,close=c,volume_lots=v,amount_10k_cny=D(s[8]),change_pct=D(s[4].strip('%')),turnover_pct=D(s[9].strip('%'))))
for prev,r in zip(rows,rows[1:]):
    assert abs((r['close']/prev['close']-1)*100-r['change_pct']) <= D('0.0051')
with (P/'daily_verified.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
idx=next(i for i,r in enumerate(rows) if r['date']=='2026-08-07')
window=rows[idx-10:idx+11]
assert len(window)==21
lo,hi=D('9.18')*D('.99'),D('9.18')*D('1.01')
def overlap(r,a,b):return r['high']>=a and r['low']<=b
near=[r for r in rows if overlap(r,lo,hi)]
band=[r for r in rows if overlap(r,D('9.10'),D('9.25'))]
assert [r['date'] for r in near]==['2026-08-06','2026-08-07','2026-08-10']
assert near==band
def p(x):return f'{x:.2f}%'
def table(rs,full=True):
    if full:
        out=['| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量（手） | 成交额（万元） | 涨跌幅 | 换手率 |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        for r in rs:out.append('| '+ ' | '.join([r['date']]+[f"{r[k]:.2f}" for k in ['open','high','low','close']]+[f"{r['volume_lots']:.0f}",f"{r['amount_10k_cny']:.2f}",p(r['change_pct']),p(r['turnover_pct'])])+' |')
    else:
        out=['| 日期 | 最高 | 收盘 | 与9.10–9.25相交 | 收盘相对该区间 |','|---|---:|---:|---|---|']
        for r in rs:out.append(f"| {r['date']} | {r['high']:.2f} | {r['close']:.2f} | {'是' if overlap(r,D('9.10'),D('9.25')) else '否'} | {'区间内' if D('9.10')<=r['close']<=D('9.25') else '低于区间'} |")
    return '\n'.join(out)
manifest=json.loads((P/'source_manifest.json').read_text())
sources={r['id']:r for r in manifest if r['returncode']==0 and r['bytes']>0}
summary=dict(rows=49,window_start=window[0]['date'],window_end=window[-1]['date'],window_rows=21,near_band=[str(lo),str(hi)],overlap_days=[r['date'] for r in near],high_in_band_days=[r['date'] for r in rows if lo<=r['high']<=hi],close_in_band_days=[r['date'] for r in rows if lo<=r['close']<=hi],close_above_918=sum(r['close']>D('9.18') for r in rows),volume_differences=volume_differences,ohlc_mismatches=0,qfq_ohlc_mismatches=0)
(P/'verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
src_lines=[]
for key,label,role in [('tencent_daily_unadjusted','腾讯财经不复权日线','主价格及成交量'),('sohu_daily','搜狐证券日线','成交额、涨跌幅、换手率；交叉核验OHLC'),('tencent_daily','腾讯财经前复权日线','复权敏感性核验')]:
    s=sources[key];stamp=dt.datetime.fromisoformat(s['captured_at']).astimezone(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec='seconds')
    src_lines.append(f"- [{label}]({s['url']})：{role}；行情日期 2026-07-20—2026-09-24；抓取时间 {stamp}；原始文件 `{s['file']}`。")
text=f'''# 雷科防务（002413）9.18元附近压力假设核验

**INFERENCE｜结论：PARTIALLY SUPPORTED。** 9.10–9.25元附近存在同一轮行情中的受阻线索，但“2026-08-07最高价约9.18元”不符合行情记录。当天最高 **9.52元**、收盘 **9.17元**。9.18只能作为候选历史价格带的参考点，不能据此认定为经过多轮独立检验的有效压力位。

本报告只核验历史价格结构，不提供买卖建议。观察截止2026-09-24；不使用其后价格评价假设。

## FACT｜数据、来源与口径

取得2026-07-20至2026-09-24共49条日线，日期唯一、按日升序；研究对象为深圳A股雷科防务002413，不是台湾雷科6207。价格为人民币元/股；成交量为供应商显示的整数手（1手=100股），不能当作精确逐笔股数；成交额为万元，保留搜狐原始两位小数。换手率沿用供应商公布值，未用当前流通股本回推历史换手。

主价格采用腾讯 **不复权** `day`；对照腾讯 **前复权** `qfqday`，本次快照内49日OHLC完全一致。搜狐同日OHLC也全部一致。因此本区间结论不受这两个已核对口径影响；这不代表其他时期或未来重新抓取的前复权价格也必然相同。成交额和换手率不做复权。

{chr(10).join(src_lines)}
- [东方财富Choice盘中快照](https://finance.eastmoney.com/a/202608073835100044.html)：事件与发布时间2026-08-07 14:11，北京时间；检索日期2026-09-27；补充盘口点位，不能代替完整分钟序列。
- 东方财富不复权日线接口首轮也返回49条，与本报告关键OHLC一致；后续保存请求为空响应，因此不将其作为本地完整原始档案来源。失败请求的时间与状态保存在 `source_manifest.json`。

**FACT｜跨源差异。** 腾讯与搜狐的8/10成交量分别为1,320,603与1,320,604手，8/19分别为1,094,889与1,094,890手；各差1手。报告成交量统一用腾讯，未平均、未混用。两源OHLC无差异。8/07成交额使用搜狐149,275.61万元（精度100元）；首轮东方财富返回1,492,756,038.99元，与搜狐显示值相差61.01元，属于已记录的小额口径/精度差异，不能宣称元级成交额完全一致。

## FACT｜2026-08-07精确日线

{table([rows[idx]])}

前收8.69元。最高9.52元，比9.18元高0.34元；9.17元是收盘价，不是最高价。价格来源为上列腾讯不复权与搜狐日线。

## CALCULATION｜8/07冲高回落的日线证据

- 最高价相对前收涨幅：`(9.52 / 8.69 - 1) × 100 = {p((D('9.52')/D('8.69')-1)*100)}`。
- 收盘涨幅：`(9.17 / 8.69 - 1) × 100 = {p((D('9.17')/D('8.69')-1)*100)}`，与公布5.52%一致。
- 最高至收盘净回落：0.35元；以最高价为分母，`(9.52 - 9.17) / 9.52 × 100 = {p((D('9.52')-D('9.17'))/D('9.52')*100)}`。
- 上影线0.35元，占当日高低振幅1.00元的35%。收盘仍高于开盘，不能把“冲高回落”写成“当天收跌”。

## CALCULATION｜触及与站稳的统计定义

- 用户给定观察带：9.10–9.25元，边界计入。
- 9.18±1%精确区间：**9.0882–9.2718元**。按0.01元报价刻度，带内可报价9.09–9.27元；计算使用精确边界。
- “触及/接近日”按日线高低区间与观察带相交统计：`high >= 下界 且 low <= 上界`。这只是有覆盖证据的交易日数，不是逐笔成交验证的触碰次数；日线不能证明每个中间价都成交，更不能计算一天内往返次数。
- “最高落在带内”另行计数，区别于盘中越过整个带；“收盘保持在带上方”定义为收盘严格大于上界。连续至少2日收盘在带上方作为本次持续站稳检验，属于明确的分析约定，不是市场统一标准。

## FACT｜前后各10个交易日：2026-07-24—2026-08-21

{table(window,False)}

## CALCULATION｜统计结果与三天逐项核验

| 统计项 | 9.10–9.25 | 9.18±1% |
|---|---:|---:|
| 21日事件窗口内，高低区间与观察带相交的日数 | 3 | 3 |
| 全49日内，高低区间与观察带相交的日数 | 3 | 3 |
| 最高价落在观察带内的日数 | 2 | 2 |
| 最高价超过观察带上界的日数 | 1 | 1 |
| 相交日收盘低于观察带下界 | 2 | 2 |
| 相交日收盘位于观察带内 | 1 | 1 |
| 全49日收盘高于观察带上界 | 0 | 0 |
| 连续至少2日收盘高于观察带上界 | 0 | 0 |

全49日没有收盘价高于9.18元的记录。相交日为8/06、8/07、8/10，按交易日连续，合并为 **1段连续接触行情**，不能称为3轮独立回测。

| 日期 | 最高 | 收盘 | 最高至收盘回落 | 日线观察 |
|---|---:|---:|---:|---|
| 8/06 | 9.23 | 8.69 | {p((D('9.23')-D('8.69'))/D('9.23')*100)} | 最高落在带内，收于下界以下 |
| 8/07 | 9.52 | 9.17 | {p((D('9.52')-D('9.17'))/D('9.52')*100)} | 盘中超过带上界，收回带内；并非被9.18挡住未突破 |
| 8/10 | 9.21 | 9.03 | {p((D('9.21')-D('9.03'))/D('9.21')*100)} | 开盘9.17，最高落在带内，收于下界以下 |

8/11—9/24剩余33个交易日，最高价均低于9.0882元，未重新进入上述两条观察带。这意味着缺乏后来重新接近后的独立受阻样本，不能拿这些低位交易日累加“压力验证次数”。

## CALCULATION｜9/24收盘8.97距各参照价格

**FACT：** 9/24开盘8.31、最高8.97、最低8.31、收盘8.97，前收8.15，公布涨幅10.06%。按前收乘1.10并四舍五入至分得到涨停价8.97，收盘等于该价。

下表“尚需上涨”以8.97为分母；“低于参照价”以参照价为分母，二者不能混用。

| 参照价格 | 价差（元） | 从8.97尚需上涨 | 8.97低于参照价 |
|---|---:|---:|---:|
'''
for label,value in [('候选带下沿',D('9.10')),('用户参考点',D('9.18')),('候选带上沿',D('9.25')),('8/07实际高点；本49日最高',D('9.52'))]:
    text+=f"| {value:.2f}（{label}） | {value-D('8.97'):.2f} | {p((value/D('8.97')-1)*100)} | {p((1-D('8.97')/value)*100)} |\n"
text+='''
因此9/24尚未进入9.10–9.25元候选带，距离9.18为2.34%的向上价差，距离实际区间高点9.52为6.13%的向上价差。“突破9.18”与“突破8/07最高价”不是同一件事。

## MISSING EVIDENCE｜历史分钟结构

**MISSING：未获得可核验的2026-08-07完整1分钟或5分钟OHLCV序列。** 东方财富历史分钟请求返回空响应，不能把网络失败解读为当日无成交，也不能断言所有供应商都没有该历史数据。

**FACT：** 东方财富Choice发布的14:11盘口快照记录14:11:30价格8.91元、累计成交5.95亿元、换手5.32%。这只是一个局部时间片。

**MISSING EVIDENCE：** 9.52出现的准确时刻；首次或末次越过9.18的时刻；冲高后用了多少分钟回落；回落是否连续；带内停留时间、分钟成交量和盘中反复触碰次数。均不填数。日线最高至收盘回落3.68%不能替代分钟路径，也不能据此认定“尾盘跳水”或卖压集中于9.18。

## INFERENCE｜为何仅为PARTIALLY SUPPORTED

支持部分：9.23、9.21两次日内高点位于候选带，分别收至8.69、9.03；中间一天从9.52回落收9.17，且全区间无收盘超过9.18。把9.10–9.25视为需要继续验证的历史参考带有描述性依据。

不支持的具体前提：8/07的最高价不是9.18，而是9.52；该日曾超过整个候选带，因此不能说价格在9.18处始终过不去。

证据强度限制：3个接近日集中在同一轮行情，独立样本不足；缺少完整分钟数据，无法识别卖压的具体位置与持续性；日成交量也不能等同于9.18附近的成交密集度。9.52只是本观察区间的最高点，单凭该点同样不能自动认定为有效压力位。

## FACT｜完整日线附表（49条）

'''+table(rows)+'''

## CALCULATION｜复核与留档

完成检查：日期唯一且两源日期集合一致；49条OHLC跨源一致；腾讯前复权与不复权49条价格一致；最低≤开/收≤最高；7/21起48条涨跌幅与前收计算误差均在公布两位小数精度内。7/20涨跌幅保留搜狐公布值，未因窗口内缺少7/17而伪称已独立重算。

`daily_verified.csv`保存用于报告的49条数值；`verification.json`保存核验与差异；`source_manifest.json`保存请求URL、抓取时间、状态和文件哈希；原始腾讯与搜狐JSON保留于同目录。仅本报告与证据文件为本次新增，不修改AlphaOS Core或同步参考文件。
'''
(P/'雷科防务_9.18压力假设核验.md').write_text(text)
receipt={'schemaVersion':1,'items':[{'id':'leike-price-structure','title':'8/07最高9.52元；9.18附近仅有同一轮行情的受阻线索','queries':[{'id':'daily-bars','source':{'label':'腾讯财经与搜狐证券历史日线','links':[{'label':'搜狐历史行情','url':'https://q.stock.sohu.com/cn/002413/lshq.shtml'}],'metricDefinitions':[{'label':'接近交易日','definition':'日内高低区间与9.0882至9.2718元相交；不等同于盘中触碰次数。'}],'filters':['证券：002413.SZ','主价格：不复权'],'caveats':['49条日线；3个接近日属于1段连续行情。','历史完整分钟数据缺失，不能重建分钟回落路径。','搜狐与腾讯有两个日期的成交量相差1手，报告统一采用腾讯成交量。'],'evidenceFlow':[{'kind':'validation','title':'价格复核','detail':'49条OHLC在腾讯不复权与搜狐数据间一致；腾讯前复权与不复权价格亦一致。'},{'kind':'calculation','title':'历史距离','detail':'(9.18/8.97−1)×100=2.34%；(9.52/8.97−1)×100=6.13%。'}]},'reportingPeriod':'2026-07-20至2026-09-24','capturedAt':sources['tencent_daily_unadjusted']['captured_at'],'columns':['date','high','close'],'rows':[{'date':r['date'],'high':float(r['high']),'close':float(r['close'])} for r in near],'preview':{'kind':'partial','note':'展示3个与观察带相交的交易日；完整日线49条。','totalRows':49}}]}]}
(P/'sources_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('report',str(P/'雷科防务_9.18压力假设核验.md'))
