#!/usr/bin/env python3
"""Pinned installer for the inspected Ubuntu/OpenClaw 2026.3.8 deployment."""
import argparse, datetime, hashlib, json, pathlib, shutil, subprocess, tempfile, urllib.request
REPO='qli09988-ai/alphaos-framework'
EXPECTED = {'sync.py': '526355af935c803c021134448b6331e5bd7a9053cd1d287cb2cc4cd029fd3f03', 'handler.ts': '12235db84461434f3a54a5da3ea8840297fcb3f1338b2d65ed1b620bd834455b', 'HOOK.md': 'c2ca70c49d7af66a5600f6898e550b3475f0eff8672b71e24d4fc581cf9d5cc8', 'rollback.py': '349954640b416f8fe7a29cdd22264e81b974c18de680b9a75394ed98346aadcb'}

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--commit',required=True); args=parser.parse_args()
    import re
    if not re.fullmatch('[0-9a-f]{40}',args.commit): raise SystemExit('Invalid installer commit')
    version=subprocess.check_output(['openclaw','--version'],text=True)
    if '2026.3.8' not in version: raise SystemExit('This installer requires the inspected OpenClaw 2026.3.8; recheck deployment first.')
    home=pathlib.Path.home()/'.openclaw'; config=home/'openclaw.json'
    cfg=json.loads(config.read_text()); workspace=pathlib.Path(cfg.get('agents',{}).get('defaults',{}).get('workspace',str(home/'workspace'))).expanduser()
    if str(workspace) != '/root/.openclaw/workspace': raise SystemExit('Unexpected workspace; recheck deployment first.')
    hook=workspace/'hooks/alphaos-github-sync'
    if hook.exists(): raise SystemExit('Hook already exists; do not overwrite. Inspect existing installation first.')
    subprocess.run(['systemctl','--user','is-active','--quiet','openclaw-gateway.service'],check=True)
    backup=home/'backups'/('alphaos-github-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    backup.mkdir(parents=True,mode=0o700)
    shutil.copy2(config,backup/'openclaw.json')
    for name in ('AGENTS.md','SOUL.md','TOOLS.md','MEMORY.md','USER.md','IDENTITY.md','BOOTSTRAP.md','trading-framework-current.md'):
        if (workspace/name).is_file(): shutil.copy2(workspace/name,backup/name)
    print('BACKUP:',backup,flush=True)
    try:
        with tempfile.TemporaryDirectory() as tmp:
            staging=pathlib.Path(tmp)
            for name,expected in EXPECTED.items():
                url=f'https://raw.githubusercontent.com/{REPO}/{args.commit}/runtime/openclaw-github-sync/{name}'
                with urllib.request.urlopen(url,timeout=20) as response: data=response.read(1000000)
                if hashlib.sha256(data).hexdigest()!=expected: raise RuntimeError('Installer hash mismatch: '+name)
                (staging/name).write_bytes(data)
            subprocess.run(['/usr/bin/python3',str(staging/'sync.py'),'--workspace',str(workspace)],check=True,timeout=60)
            state=json.loads((workspace/'alphaos-framework/status.json').read_text())
            if state['state']!='CURRENT': raise RuntimeError('First installation requires CURRENT sync')
            hook.parent.mkdir(exist_ok=True)
            shutil.copytree(staging,hook)
        (workspace/'alphaos-runtime').mkdir(exist_ok=True)
        subprocess.run(['openclaw','hooks','enable','alphaos-github-sync'],check=True,timeout=60)
        subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True,timeout=30)
        subprocess.run(['systemctl','--user','is-active','openclaw-gateway.service'],check=True)
        print('INSTALL_COMPLETE; verify hook and new-session behavior before acceptance.')
        print('FRAMEWORK_STATUS:',json.dumps(state))
    except Exception:
        shutil.copy2(backup/'openclaw.json',config)
        if hook.exists(): shutil.move(str(hook),str(backup/'failed-hook'))
        subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=False,timeout=30)
        print('INSTALL_FAILED; original configuration restored. Backup:',backup)
        raise
    print('ROLLBACK: python3 '+str(hook/'rollback.py')+' --backup '+str(backup))
if __name__=='__main__': main()
