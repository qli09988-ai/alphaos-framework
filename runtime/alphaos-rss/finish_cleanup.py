#!/usr/bin/env python3
"""Retire the remaining legacy Skill and report publisher freshness, without changing feeds."""
import argparse, csv, datetime, importlib.util, json, pathlib, shutil, subprocess, urllib.parse
W=pathlib.Path('/root/.openclaw/workspace')

def diagnostics():
    s=json.loads((W/'alphaos-runtime/rss/snapshot.json').read_text())
    now=datetime.datetime.now(datetime.timezone.utc)
    print('RSS_RUN:',s['state'],s['completed_at'])
    for f in s['feeds']:
        records=[i for i in s['items'] if i['feed_id']==f['id']]
        dates=[]
        for i in records:
            if i.get('published_at'):
                try: dates.append(datetime.datetime.fromisoformat(i['published_at']))
                except ValueError: pass
        latest=max(dates) if dates else None
        print(json.dumps({'feed':f['name'],'fetch_state':f['state'],'stored_items':len(records),'dated_items':len(dates),'missing_dates':len(records)-len(dates),'latest_published_at':latest.isoformat() if latest else 'MISSING','latest_age_hours':round((now-latest).total_seconds()/3600,1) if latest else None,'future_dated_items':sum(d>now for d in dates)},ensure_ascii=False))
    # Show the public failed feed route only if it contains no credentials/query.
    failed_names={f['name'] for f in s['feeds'] if f['state']=='ERROR'}
    for row in csv.reader((W/'rss_feeds.txt').read_text().splitlines()):
        if len(row)<2 or row[0].strip() not in failed_names: continue
        url=row[1].strip(); parsed=urllib.parse.urlsplit(url)
        public_route=url if not parsed.username and not parsed.password and not parsed.query and not parsed.fragment else 'REDACTED (inspect locally)'
        print('FAILED_FEED_ROUTE:',row[0].strip(),public_route)

def restore(archive_path):
    archive=pathlib.Path(archive_path).resolve()
    if not archive.is_relative_to((W.parent/'legacy-archives').resolve()): raise SystemExit('Invalid archive path')
    receipt=json.loads((archive/'receipt.json').read_text())
    lock=W/'.clawhub/lock.json'; current=json.loads(lock.read_text()); before=json.loads((archive/'clawhub-lock.before.json').read_text())
    if not isinstance(current.get('skills'),dict) or 'justice-plutus' in current['skills']: raise SystemExit('Registry restore conflict')
    if any(pathlib.Path(e['source']).exists() for e in receipt['moves']): raise SystemExit('File restore conflict')
    for e in receipt['moves']:
        src=pathlib.Path(e['source']); src.parent.mkdir(parents=True,exist_ok=True); shutil.move(e['destination'],str(src))
    current['skills']['justice-plutus']=before['skills']['justice-plutus']
    shutil.copy2(lock,archive/'clawhub-lock.before-restore.json')
    temp=lock.with_suffix('.alphaos-tmp'); temp.write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n'); temp.replace(lock)
    subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True)
    print('JUSTICE_RESTORED; unrelated registry entries retained.')

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--restore'); args=parser.parse_args()
    if args.restore: restore(args.restore); return
    lock=W/'.clawhub/lock.json'
    meta=json.loads(lock.read_text())
    skills=meta.get('skills') if isinstance(meta,dict) else None
    if not isinstance(skills,dict) or 'justice-plutus' not in skills:
        print('CLEANUP_STOPPED: unexpected registry layout; keys:',list(meta) if isinstance(meta,dict) else type(meta).__name__)
        diagnostics(); return
    # Reuse the installed, reviewed reference checker; only the registry metadata is exempt.
    spec=importlib.util.spec_from_file_location('rss_install','/root/alphaos-rss-install.py')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    blocked=sorted(set(module.references(W,'JusticePlutus',('skills/justice-plutus',))+module.references(W,'justice-plutus',('skills/justice-plutus',))))
    blocked=[p for p in blocked if p!=str(lock)]
    if blocked:
        print('CLEANUP_BLOCKED:',json.dumps(blocked)); diagnostics(); return
    candidates=[W/'JusticePlutus',W/'skills/justice-plutus']
    if any(p.is_symlink() for p in candidates): raise SystemExit('Unexpected symlink; inspect first')
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    archive=W.parent/'legacy-archives'/('justice-'+stamp); archive.mkdir(parents=True,mode=0o700)
    shutil.copy2(lock,archive/'clawhub-lock.before.json')
    moved=[]
    try:
        for p in candidates:
            if not p.exists(): continue
            dest=archive/p.relative_to(W); dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(p),str(dest)); moved.append({'source':str(p),'destination':str(dest)})
            (archive/'receipt.json').write_text(json.dumps({'moves':moved},indent=2))
        skills.pop('justice-plutus')
        temp=lock.with_suffix('.alphaos-tmp'); temp.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n'); temp.replace(lock)
        subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True)
        subprocess.run(['systemctl','--user','is-active','openclaw-gateway.service'],check=True)
    except Exception:
        shutil.copy2(archive/'clawhub-lock.before.json',lock)
        for e in reversed(moved):
            source=pathlib.Path(e['source']); source.parent.mkdir(parents=True,exist_ok=True); shutil.move(e['destination'],str(source))
        subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=False)
        raise
    print('JUSTICE_ARCHIVED:',json.dumps(moved)); print('REGISTRY_ENTRY_REMOVED: justice-plutus'); print('RECOVERY_ARCHIVE:',archive); print('RESTORE: python3 /root/alphaos-rss-finish.py --restore '+str(archive))
    print('REMAINING_SKILLS:',json.dumps(sorted(p.name for p in (W/'skills').iterdir() if p.is_dir() and (p/'SKILL.md').exists())))
    diagnostics()
if __name__=='__main__': main()
