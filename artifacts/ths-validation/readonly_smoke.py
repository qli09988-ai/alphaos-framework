"""Minimal guest-only market-data checks; no account or trading APIs."""
import os, sys, json, time, logging, contextlib, argparse, statistics
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo
os.environ.pop('THS_USERNAME', None)
os.environ.pop('THS_PASSWORD', None)
os.environ.pop('THS_MAC', None)
sys.dont_write_bytecode = True
logging.disable(logging.CRITICAL)
TZ = ZoneInfo('Asia/Shanghai')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--symbol', default='鲁信创投')
parser.add_argument('--method', choices=['all','klines','depth','tick_level1','intraday_data','big_order_flow','call_auction','call_auction_anomaly'], default='all')
parser.add_argument('--include-data', action='store_true')
args=parser.parse_args()

def emit(d):
    print(json.dumps(d, ensure_ascii=False, default=str), flush=True)
@contextlib.contextmanager
def quiet():
    sys.stdout.flush(); sys.stderr.flush()
    out, err = os.dup(1), os.dup(2)
    with open(os.devnull,'w') as sink:
        os.dup2(sink.fileno(),1); os.dup2(sink.fileno(),2)
        try: yield
        finally:
            os.dup2(out,1); os.dup2(err,2); os.close(out); os.close(err)
def error_class(error):
    s=str(error).lower()
    if any(x in s for x in ['权限','permission','授权']):return 'permission_required'
    if any(x in s for x in ['登录','login','auth','账户','account','password']):return 'authentication_failed'
    if any(x in s for x in ['timeout','超时']):return 'timeout'
    return 'sdk_error_redacted'
with quiet():
    from thsdk import THS
    import importlib.metadata
emit({'stage':'environment','sdk':importlib.metadata.version('thsdk'),'time':datetime.now(TZ).isoformat(),'auth_mode':'guest_only'})
try:
    with quiet(): client=THS()
    t=time.monotonic()
    with quiet(): result=client.connect(max_retries=1)
    emit({'stage':'connect','ok':bool(result),'elapsed_seconds':round(time.monotonic()-t,3),'error_category':None if result else error_class(result.error)})
    if not result:sys.exit(2)
    # Resolve one intended A-share via the documented discovery method.
    with quiet(): result=client.search_symbols(args.symbol)
    rows=result.data if result and isinstance(result.data,list) else []
    candidates=[r for r in rows if r.get('THSCODE','').startswith(('USHA','USZA'))]
    emit({'stage':'search_symbols','ok':bool(result),'matches':candidates})
    if len(candidates)!=1:sys.exit(3)
    code=candidates[0]['THSCODE']
    cases=[('klines',lambda:client.klines(code,interval='1m',count=3)),('depth',lambda:client.depth(code)),('tick_level1',lambda:client.tick_level1(code)),('intraday_data',lambda:client.intraday_data(code)),('big_order_flow',lambda:client.big_order_flow(code)),('call_auction',lambda:client.call_auction(code)),('call_auction_anomaly',lambda:client.call_auction_anomaly(code[:4]))]
    for name,fn in cases:
        if args.method not in ('all',name):continue
        emit({'stage':'request','method':name,'requested_at':datetime.now(TZ).isoformat()})
        t=time.monotonic()
        try:
            with quiet(): response=fn()
            data=response.data
            rows=data if isinstance(data,list) else [data] if isinstance(data,dict) else []
            fields=sorted({str(k) for r in rows if isinstance(r,dict) for k in r})
            times=[r.get('时间') for r in rows if isinstance(r,dict) and r.get('时间') is not None]
            def dt(value):
                if isinstance(value,datetime):return value.astimezone(TZ)
                if isinstance(value,(int,float)) and 946684800<value<4102444800:return datetime.fromtimestamp(value,TZ)
                return None
            timestamps=[t for t in (dt(v) for v in times) if t is not None]
            ordered=sorted(set(timestamps))
            gaps=[(b-a).total_seconds() for a,b in zip(ordered,ordered[1:])]
            invalid=[]
            for i,row in enumerate(rows):
                if not isinstance(row,dict):continue
                for field,value in row.items():
                    if isinstance(value,(int,float)) and value in (4294967295,2147483648):invalid.append({'row':i,'field':field})
            questionable_fields=['委托买入价','委托卖出价'] if name=='big_order_flow' else []
            def clean(row):
                if not isinstance(row,dict):return row
                return {k:None if k in questionable_fields or (isinstance(v,(int,float)) and v in (4294967295,2147483648)) else v for k,v in row.items()}
            result={'stage':'response','method':name,'ok':bool(response),'rows':len(rows),'elapsed_seconds':round(time.monotonic()-t,3),'received_at':datetime.now(TZ).isoformat(),'fields':fields,'time_first':times[0] if times else None,'time_last':times[-1] if times else None,'latest_market_time':max(timestamps).isoformat() if timestamps else None,'timestamp_gap_mode_seconds':Counter(gaps).most_common(3),'timestamp_gap_median_seconds':statistics.median(gaps) if gaps else None,'invalid_value_count':len(invalid),'invalid_fields':dict(Counter(v['field'] for v in invalid)),'unverified_fields_excluded':questionable_fields,'sample':[clean(row) for row in rows[-1:]] if response else [],'error_category':None if response else error_class(response.error)}
            if args.include_data and response:result['data']=[clean(row) for row in rows]
            emit(result)
        except Exception as e:
            emit({'stage':'response','method':name,'ok':False,'exception_type':type(e).__name__,'elapsed_seconds':round(time.monotonic()-t,3)})
        time.sleep(.5)
finally:
    if 'client' in globals():
        with quiet():client.disconnect()
