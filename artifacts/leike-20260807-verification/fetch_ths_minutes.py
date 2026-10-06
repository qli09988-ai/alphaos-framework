import os, sys, json, pathlib, logging, contextlib, signal, time
from datetime import datetime
from zoneinfo import ZoneInfo
P=pathlib.Path(__file__).resolve().parent
OUT=P/'minute_evidence'
OUT.mkdir(exist_ok=True)
SDK=P.parent/'ths-validation/sdk-source/thsdk-1.7.18'
sys.path.insert(0,str(SDK))
sys.dont_write_bytecode=True
for k in ('THS_USERNAME','THS_PASSWORD','THS_MAC'):os.environ.pop(k,None)
os.chdir(OUT)
logging.disable(logging.CRITICAL)
TZ=ZoneInfo('Asia/Shanghai')
@contextlib.contextmanager
def quiet():
    sys.stdout.flush();sys.stderr.flush()
    out,err=os.dup(1),os.dup(2)
    with open(os.devnull,'w') as sink:
        os.dup2(sink.fileno(),1);os.dup2(sink.fileno(),2)
        try:yield
        finally:
            os.dup2(out,1);os.dup2(err,2);os.close(out);os.close(err)
def timeout(*args):raise TimeoutError()
signal.signal(signal.SIGALRM,timeout)
def emit(obj):print(json.dumps(obj,ensure_ascii=False,default=str),flush=True)
def category(err):
    s=str(err).lower()
    if any(x in s for x in ['权限','permission','授权']):return 'permission_required'
    if any(x in s for x in ['登录','login','auth','账户','account','password']):return 'authentication_failed'
    return 'sdk_error_redacted'
log=[]
try:
    signal.alarm(45)
    with quiet():
        from thsdk import THS
        client=THS()
        result=client.connect(max_retries=1)
    signal.alarm(0)
    status=dict(method='connect',guest_only=True,ok=bool(result),captured_at=datetime.now(TZ).isoformat(),error=None if result else category(result.error))
    log.append(status);emit(status)
    if not result:sys.exit(2)
    with quiet():result=client.search_symbols('雷科防务')
    matches=[r for r in (result.data or []) if r.get('THSCODE','').startswith(('USHA','USZA'))]
    emit(dict(method='search_symbols',matches=matches))
    assert len(matches)==1 and matches[0]['THSCODE']=='USZA002413'
    start=datetime(2026,8,7,9,0,tzinfo=TZ);end=datetime(2026,8,7,15,30,tzinfo=TZ)
    tasks=[('ths_1m',lambda:client.klines('USZA002413',interval='1m',start_time=start,end_time=end,adjust='')),
           ('ths_5m',lambda:client.klines('USZA002413',interval='5m',start_time=start,end_time=end,adjust='')),
           ('ths_min_snapshot',lambda:client.min_snapshot('USZA002413',date='20260807'))]
    for name,fn in tasks:
        try:
            signal.alarm(35)
            with quiet():response=fn()
            signal.alarm(0)
            data=response.data if response and isinstance(response.data,list) else []
            record=dict(source='thsdk 1.7.18 public guest market data',method=name,symbol='USZA002413',requested_date='2026-08-07',adjust='unadjusted',captured_at=datetime.now(TZ).isoformat(),ok=bool(response),error=None if response else category(response.error),data=data)
            (OUT/(name+'.json')).write_text(json.dumps(record,ensure_ascii=False,default=str,indent=2))
            summary={k:v for k,v in record.items() if k!='data'};summary.update(rows=len(data),first=data[:1],last=data[-1:]);log.append(summary);emit(summary)
        except Exception as e:
            signal.alarm(0);record=dict(method=name,error_type=type(e).__name__,captured_at=datetime.now(TZ).isoformat());log.append(record);emit(record)
except Exception as e:
    signal.alarm(0);record=dict(method='initialization',error_type=type(e).__name__,captured_at=datetime.now(TZ).isoformat());log.append(record);emit(record)
finally:
    (OUT/'ths_attempt_log.json').write_text(json.dumps(log,ensure_ascii=False,default=str,indent=2))
    if 'client' in globals():
        with quiet():client.disconnect()
