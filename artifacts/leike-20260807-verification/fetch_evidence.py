import concurrent.futures
import datetime as dt
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
base = 'https://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.002413&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'
urls = {
    'eastmoney_daily_unadjusted': base + '&klt=101&fqt=0&beg=20260720&end=20260924',
    'eastmoney_daily_qfq': base + '&klt=101&fqt=1&beg=20260720&end=20260924',
    'sohu_daily': 'https://q.stock.sohu.com/hisHq?code=cn_002413&start=20260720&end=20260924&stat=1&order=A&period=d&rt=json',
    'eastmoney_1min_aug07': base + '&klt=1&fqt=0&beg=20260807&end=20260807&lmt=1000',
    'eastmoney_5min_aug07': base + '&klt=5&fqt=0&beg=20260807&end=20260807&lmt=1000',
    'tencent_daily': 'https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sz002413,day,2026-07-20,2026-09-24,100,qfq',
}

def fetch(item):
    name, url = item
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    p = subprocess.run(['curl', '-L', '--max-time', '25', '-sS', url], capture_output=True)
    path = ROOT / (name + '.json')
    path.write_bytes(p.stdout)
    result = dict(id=name,url=url,started_at=started,captured_at=dt.datetime.now(dt.timezone.utc).isoformat(),returncode=p.returncode,bytes=len(p.stdout),sha256=hashlib.sha256(p.stdout).hexdigest(),file=path.name)
    try:
        data = json.loads(p.stdout.decode('utf-8' if name != 'sohu_daily' else 'gb18030'))
        if name.startswith('eastmoney'):
            rows = (data.get('data') or {}).get('klines', [])
            result.update(rows=len(rows),first=rows[:1],last=rows[-1:])
        elif name == 'sohu_daily':
            result.update(rows=len(data[0]['hq']))
        else:
            result.update(data_keys=list(data.get('data',{}).get('sz002413',{})))
    except Exception as e:
        result['parse_error']=type(e).__name__
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    manifest = list(pool.map(fetch,urls.items()))
(ROOT/'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
