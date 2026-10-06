#!/usr/bin/env python3
"""Small complete views over the authoritative snapshot; no LLM inference."""
import argparse, datetime, hashlib, json, pathlib, shutil, subprocess
DEFAULT=pathlib.Path('/root/.openclaw/workspace')
MARKER='<!-- ALPHAOS_RSS_QUERY -->'
INSTRUCTION='''<!-- ALPHAOS_RSS_QUERY -->
For RSS health/news verification use `python3 scripts/alphaos_rss_query.py health` or `python3 scripts/alphaos_rss_query.py news --hours 24 --limit 20` (optional `--search TERM`) rather than reading a huge snapshot into the prompt. The helper reads the entire authoritative snapshot and emits a bounded view. Health includes all configured feeds including failed feeds with zero items. Never infer configured-source absence from health.json grep or article absence. Use `python3 scripts/alphaos_rss_query.py audit` for exact current filesystem evidence; do not claim all Skills are absent from a partial listing. Health/legacy filesystem audits and article relevance are distinct. Report uncertainty rather than inventing counts. Never write an uncorrected acceptance report into memory.
<!-- /ALPHAOS_RSS_QUERY -->
'''
def current(): return datetime.datetime.now(datetime.timezone.utc)
def parsed(value):
    if not value: return None
    try:
        d=datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
        return d if d.tzinfo else None
    except (ValueError,AttributeError): return None

def health(snapshot,at=None):
    at=at or current(); completed=parsed(snapshot.get('completed_at'))
    summaries=[]
    for f in snapshot.get('feeds',[]):
        items=[i for i in snapshot.get('items',[]) if i.get('feed_id')==f['id']]
        dates=[d for i in items if (d:=parsed(i.get('published_at'))) is not None]
        last=max(dates) if dates else None
        summaries.append({**f,'stored_items':len(items),'latest_published_at':last.isoformat() if last else None,'latest_age_hours':round((at-last).total_seconds()/3600,2) if last else None,'missing_publication_dates':len(items)-len(dates),'future_dated_items':sum(d>at for d in dates)})
    return {'read_scope':'entire_snapshot','run_id':snapshot.get('run_id'),'state':snapshot.get('state'),'completed_at':snapshot.get('completed_at'),'collection_age_minutes':round((at-completed).total_seconds()/60,2) if completed else None,'configured_feeds':snapshot.get('configured_feeds'),'successful_feeds':snapshot.get('successful_feeds'),'failed_feeds':snapshot.get('failed_feeds'),'stored_item_count':len(snapshot.get('items',[])),'feeds':summaries,'note':'Retrieval success is distinct from publication freshness. Missing dates are null, not guessed.'}

def news(snapshot,hours=24,limit=20,search=None,at=None):
    at=at or current(); start=at-datetime.timedelta(hours=hours)
    statuses={f['id']:f for f in snapshot.get('feeds',[])}
    items=[]
    for i in snapshot.get('items',[]):
        published=parsed(i.get('published_at'))
        if published is None or not start<=published<=at: continue
        if search and search.casefold() not in (i.get('title','')+' '+i.get('description','')).casefold(): continue
        f=statuses.get(i.get('feed_id'),{})
        items.append({'id':i['id'],'source':i.get('source'),'title':i.get('title'),'link':i.get('link'),'published_at':published.isoformat(),'last_seen_at':i.get('last_seen_at'),'feed_fetch_state':f.get('state','MISSING'),'evidence_type':i.get('evidence_type','MISSING')})
    items.sort(key=lambda i:i['published_at'],reverse=True)
    unique=[]; seen=set()
    for i in items:
        identity=i.get('link') or i['id']
        if identity in seen: continue
        seen.add(identity); unique.append(i)
    return {'read_scope':'entire_snapshot','run_id':snapshot.get('run_id'),'state':snapshot.get('state'),'completed_at':snapshot.get('completed_at'),'window_start':start.isoformat(),'window_end':at.isoformat(),'search':search,'matching_unique_count':len(unique),'returned_count':min(limit,len(unique)),'items':unique[:limit],'note':'Sorted by publication time; no automatic financial/technology relevance classification. Source failures and collection age must be checked with health.'}

def audit(workspace):
    candidates=['trading-framework-current.md','盘感系统.pdf','盘感系统_final.pdf','盘感系统_v2.pdf','ai-hedge-fund','JusticePlutus','skills/justice-plutus']
    skilldir=workspace/'skills'
    result={'workspace':str(workspace),'legacy_path_exists':{n:(workspace/n).exists() for n in candidates},'skill_names':sorted(p.name for p in skilldir.iterdir() if p.is_dir() and (p/'SKILL.md').exists()) if skilldir.exists() else []}
    config=workspace/'.clawhub/lock.json'
    if config.exists(): result['justice_registry_entry_present']='justice-plutus' in json.loads(config.read_text()).get('skills',{})
    status=workspace/'alphaos-framework/status.json'
    result['framework_status']=json.loads(status.read_text()) if status.exists() else 'MISSING'
    return result

def install(workspace):
    import re
    script=workspace/'scripts/alphaos_rss_query.py'
    agents=workspace/'AGENTS.md'; skill=workspace/'skills/alphaos-rss/SKILL.md'
    if not agents.exists() or not skill.exists(): raise SystemExit('Expected AlphaOS RSS installation missing; stopped')
    backup=workspace.parent/'backups'/('alphaos-rss-query-'+current().strftime('%Y%m%dT%H%M%SZ')); backup.mkdir(parents=True,mode=0o700)
    for path in (agents,skill,script):
        if path.exists(): shutil.copy2(path,backup/path.name)
    try:
        script.parent.mkdir(exist_ok=True); shutil.copy2(__file__,script)
        for path in (agents,skill):
            content=re.sub(r'<!-- ALPHAOS_RSS_QUERY -->[\s\S]*?<!-- /ALPHAOS_RSS_QUERY -->\s*','',path.read_text())
            # Keep Skill YAML frontmatter in first position for discovery.
            if path==skill and content.startswith('---\n'):
                boundary=content.find('\n---',4)
                if boundary<0: raise ValueError('Unexpected Skill frontmatter')
                end=boundary+4; content=content[:end]+'\n\n'+INSTRUCTION+content[end:]
            else: content=INSTRUCTION+'\n'+content
            path.write_text(content)
        subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True)
        subprocess.run(['systemctl','--user','is-active','openclaw-gateway.service'],check=True)
    except Exception:
        for path in (agents,skill): shutil.copy2(backup/path.name,path)
        if (backup/script.name).exists(): shutil.copy2(backup/script.name,script)
        print('INSTALL_FAILED; prompt files restored; backup:',backup); raise
    print('QUERY_INSTALLED; persona/Skill instructions preserved; backup:',backup)
    print(json.dumps(audit(workspace),ensure_ascii=False,indent=2))
    print(json.dumps(health(json.loads((workspace/'alphaos-runtime/rss/snapshot.json').read_text())),ensure_ascii=False,indent=2))

def main():
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['health','news','audit','install']); p.add_argument('--workspace',type=pathlib.Path,default=DEFAULT); p.add_argument('--hours',type=float,default=24); p.add_argument('--limit',type=int,default=20); p.add_argument('--search'); a=p.parse_args()
    if not 0<a.hours<=24*365 or not 1<=a.limit<=50: raise SystemExit('Invalid hours/limit')
    if a.mode=='install': install(a.workspace); return
    if a.mode=='audit': result=audit(a.workspace)
    else:
        snapshot=json.loads((a.workspace/'alphaos-runtime/rss/snapshot.json').read_text())
        result=health(snapshot) if a.mode=='health' else news(snapshot,a.hours,a.limit,a.search)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
