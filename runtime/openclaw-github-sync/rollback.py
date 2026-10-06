#!/usr/bin/env python3
import argparse, json, pathlib, shutil, subprocess
p=argparse.ArgumentParser(); p.add_argument('--backup',required=True); a=p.parse_args()
b=pathlib.Path(a.backup).resolve(); home=pathlib.Path.home()/'.openclaw'
if not b.is_relative_to((home/'backups').resolve()): raise SystemExit('Invalid backup path')
old=json.loads((b/'openclaw.json').read_text()); current=json.loads((home/'openclaw.json').read_text())
# Preserve unrelated settings made since installation; restore only this hook entry.
name='alphaos-github-sync'
entries=current.setdefault('hooks',{}).setdefault('internal',{}).setdefault('entries',{})
previous=old.get('hooks',{}).get('internal',{}).get('entries',{})
if name in previous: entries[name]=previous[name]
else: entries.pop(name,None)
shutil.copy2(home/'openclaw.json',b/'config-before-rollback.json')
(home/'openclaw.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
ws=pathlib.Path(current.get('agents',{}).get('defaults',{}).get('workspace',str(home/'workspace')))
hook=ws/'hooks'/name
if hook.exists(): shutil.move(str(hook),str(b/'disabled-hook'))
subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True)
print('ROLLBACK_COMPLETE; framework cache and runtime records retained; persona/memory never modified.')
