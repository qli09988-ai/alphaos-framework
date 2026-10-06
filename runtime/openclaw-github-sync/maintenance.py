#!/usr/bin/env python3
"""Reversible legacy-framework archive and privacy-preserving RSS diagnostics."""
import argparse, ast, datetime, json, pathlib, re, shutil, subprocess
CANDIDATES = ['trading-framework-current.md','盘感系统.pdf','盘感系统_final.pdf','盘感系统_v2.pdf','ai-hedge-fund','JusticePlutus']

def text_files(workspace):
    for p in workspace.rglob('*'):
        rel=p.relative_to(workspace)
        if rel.parts[0] in CANDIDATES or any(x in rel.parts for x in ('.git','node_modules','venv','.venv','__pycache__','memory','reports','alphaos-framework')): continue
        if p.is_file() and p.suffix in ('.py','.sh','.json','.service') and p.stat().st_size<2_000_000: yield p

def blockers(workspace):
    result={n:[] for n in CANDIDATES}
    files=list(text_files(workspace))
    for root in (pathlib.Path('/root/.config/systemd/user'),pathlib.Path('/etc/systemd/system')):
        if root.exists(): files.extend(p for p in root.rglob('*.service') if p.is_file() and p.stat().st_size<100000)
    config=pathlib.Path('/root/.openclaw/openclaw.json')
    if config.exists(): files.append(config)
    cron=subprocess.run(['crontab','-l'],capture_output=True,text=True).stdout
    sources=[('crontab',cron)]
    for p in files:
        try: sources.append((str(p),p.read_text(errors='replace')))
        except OSError: pass
    for p in pathlib.Path('/proc').glob('[0-9]*/cmdline'):
        try:
            cmd=p.read_bytes().replace(b'\x00',b' ').decode(errors='replace')
            sources.append(('process '+p.parent.name,cmd))
        except OSError: pass
    for location,text in sources:
        for n in CANDIDATES:
            if n in text and 'maintenance.py' not in location: result[n].append(location)
    return result

def rss_report(workspace):
    print('\nRSS_DIAGNOSTICS:')
    for name in ('rss_monitor.py','rss_monitor.log','rss_state.json','rss_alerts.json','rss_feeds.txt'):
        p=workspace/name
        if p.exists(): print(name,'bytes=',p.stat().st_size,'mtime_utc=',datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat())
    p=workspace/'rss_monitor.py'
    if p.exists():
        tree=ast.parse(p.read_text())
        print('IMPORTS:',sorted({n.names[0].name for n in ast.walk(tree) if isinstance(n,ast.Import)}|{n.module or '' for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)}))
        print('FUNCTIONS:',[n.name for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))])
        print('CALLS:',sorted({ast.unparse(n.func) for n in ast.walk(tree) if isinstance(n,ast.Call)}))
        paths=sorted({n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str) and re.fullmatch(r'[\w./-]+\.(?:json|txt|log|py)',n.value)})
        print('FILE_REFERENCES:',paths)
        print('HAS_WHILE_LOOP:',any(isinstance(n,ast.While) for n in ast.walk(tree)))
    cron=subprocess.run(['crontab','-l'],capture_output=True,text=True).stdout
    print('RSS_CRON_ENTRY_COUNT:',sum('rss' in l.lower() for l in cron.splitlines() if l.strip() and not l.lstrip().startswith('#')))
    processes=[]
    for p in pathlib.Path('/proc').glob('[0-9]*/cmdline'):
        try:
            args=p.read_bytes().split(b'\x00')
            if any(b'rss_monitor' in a for a in args): processes.append(p.parent.name)
        except OSError: pass
    print('RSS_MONITOR_PROCESS_IDS:',processes)
    for p in text_files(workspace):
        if p.name in ('rss_monitor.py','maintenance.py'): continue
        try:
            text=p.read_text(errors='replace')
            found=[n for n in ('rss_alerts.json','rss_state.json','rss_feeds.txt','rss_monitor.py') if n in text]
            if found: print('RSS_CONSUMER:',str(p.relative_to(workspace)),found)
        except OSError: pass
    p=workspace/'rss_monitor.log'
    if p.exists():
        text=p.read_text(errors='replace')[-200000:]
        print('RECENT_LOG_HTTP_CODES:',{c:len(re.findall(r'\b'+c+r'\b',text)) for c in ('400','401','403','404','429','500','502','503')})

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--apply',action='store_true'); parser.add_argument('--restore'); args=parser.parse_args()
    workspace=pathlib.Path('/root/.openclaw/workspace')
    archive_root=pathlib.Path('/root/.openclaw/legacy-archives')
    if args.restore:
        archive=pathlib.Path(args.restore).resolve()
        if not archive.is_relative_to(archive_root.resolve()): raise SystemExit('Invalid archive')
        receipt=json.loads((archive/'receipt.json').read_text())
        if any((workspace/n).exists() for n in receipt['moved']): raise SystemExit('Restore would overwrite an existing file; stopped')
        for n in receipt['moved']: shutil.move(str(archive/n),str(workspace/n))
        print('RESTORED:',receipt['moved']); return
    refs=blockers(workspace)
    print('LEGACY_REFERENCE_CHECK:')
    for n in CANDIDATES: print(n, 'BLOCKED: '+', '.join(refs[n]) if refs[n] else 'no detected runtime references')
    rss_report(workspace)
    if not args.apply: print('READ_ONLY; use --apply to archive eligible items'); return
    archive=archive_root/datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    archive.mkdir(parents=True,mode=0o700)
    receipt={'moved':[],'blocked':refs,'workspace':str(workspace)}
    (archive/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
    for n in CANDIDATES:
        p=workspace/n
        if not p.exists() or refs[n]: continue
        if p.is_symlink(): print('SKIPPED_SYMLINK:',n); continue
        # Record intent before each reversible move to retain a recovery trail.
        receipt['pending']=n
        (archive/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
        shutil.move(str(p),str(archive/n)); receipt['moved'].append(n); receipt.pop('pending',None)
        (archive/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
    print('\nARCHIVE_COMPLETE:',receipt['moved']); print('ARCHIVE_PATH:',archive)
    print('RESTORE: python3 /root/alphaos-maintenance.py --restore '+str(archive))
    print('RSS, persona, memory, credentials, portfolio, skills, configuration, schedules and AlphaOS remain unchanged.')
if __name__=='__main__': main()
