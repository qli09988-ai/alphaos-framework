#!/usr/bin/env python3
"""Fetch an approved AlphaOS document snapshot, never merge server files."""
import argparse, concurrent.futures, fcntl, hashlib, json, os, pathlib, re, shutil, tempfile, urllib.request
from datetime import datetime, timezone
REPO = 'qli09988-ai/alphaos-framework'
MANIFEST = f'https://raw.githubusercontent.com/{REPO}/runtime/openclaw-github-sync/runtime/openclaw-github-sync/approved_release.json'
FILES = {'alphaos_core_spec.md', 'alphaos_personal_policy.md', 'alphaos_status_board.md', 'alphaos_case_lab.md', 'alphaos_backlog_changelog.md', 'alphaos_usage_protocol.md', 'README.md', 'FREEZE_v0.1.md', 'HANDOFF_RUNTIME_v0.1.md'}
def now(): return datetime.now(timezone.utc).isoformat()
def digest(data): return hashlib.sha256(data).hexdigest()
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'AlphaOS-Runtime/0.1', 'Cache-Control':'no-cache'}), timeout=12) as r:
        data = r.read(2000001)
        if len(data) > 2000000: raise ValueError('response exceeds size limit')
        return data

def validate(m):
    if m.get('schema_version') != 1 or m.get('repository') != REPO or m.get('approval_status') != 'Human Approved': raise ValueError('unapproved or unexpected manifest')
    if not re.fullmatch(r'[0-9a-f]{40}', m.get('commit','')): raise ValueError('invalid commit')
    if set(m.get('files', {})) != FILES: raise ValueError('unexpected file inventory')
    if not all(re.fullmatch(r'[0-9a-f]{64}', h) for h in m['files'].values()): raise ValueError('invalid digest')
    return m

def verify(directory):
    m = validate(json.loads((directory/'approved_release.json').read_text()))
    for name, sha in m['files'].items():
        if digest((directory/name).read_bytes()) != sha: raise ValueError('local hash mismatch: '+name)
    return m

def atomic_json(path, value):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    os.replace(tmp, path)

def sync(workspace, fetch=get):
    base = pathlib.Path(workspace)/'alphaos-framework'
    base.mkdir(parents=True, exist_ok=True)
    with (base/'.sync.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        status = {'checked_at':now(), 'repository':REPO}
        try:
            raw = fetch(MANIFEST)
            m = validate(json.loads(raw))
            releases = base/'releases'; releases.mkdir(exist_ok=True)
            target = releases/(m['commit']+'-'+digest(raw)[:16])
            if target.exists():
                try: verify(target)
                except Exception:
                    target.rename(releases/(target.name+'-quarantined-'+str(os.getpid())))
            if not target.exists():
                stage = pathlib.Path(tempfile.mkdtemp(prefix='.stage-', dir=releases))
                try:
                    def download(item):
                        name, sha = item
                        data = fetch(f'https://raw.githubusercontent.com/{REPO}/{m["commit"]}/{name}')
                        if digest(data) != sha: raise ValueError('remote hash mismatch: '+name)
                        (stage/name).write_bytes(data)
                    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
                        list(pool.map(download, m['files'].items()))
                    (stage/'approved_release.json').write_bytes(raw)
                    verify(stage)
                    stage.rename(target)
                finally:
                    if stage.exists(): shutil.rmtree(stage)
            verify(target)
            pending = base/'.current-next'
            if pending.is_symlink(): pending.unlink()
            pending.symlink_to(target.relative_to(base), target_is_directory=True)
            os.replace(pending, base/'current')
            status.update(state='CURRENT', commit=m['commit'], framework_version=m['framework_version'], last_success_at=now(), path=str(target.resolve()))
        except Exception as exc:
            status.update(state='UNAVAILABLE', error=str(exc))
            try:
                current = (base/'current').resolve(strict=True)
                if not current.is_relative_to((base/'releases').resolve()): raise ValueError('unsafe current path')
                m = verify(current)
                prior = json.loads((base/'status.json').read_text()) if (base/'status.json').exists() else {}
                status.update(state='STALE_LAST_GOOD', commit=m['commit'], framework_version=m['framework_version'], path=str(current), last_success_at=prior.get('last_success_at'))
            except Exception: pass
        atomic_json(base/'status.json', status)
        return status
if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--workspace', required=True)
    s = sync(p.parse_args().workspace)
    print(json.dumps(s, ensure_ascii=False))
    raise SystemExit(1 if s['state']=='UNAVAILABLE' else 0)
