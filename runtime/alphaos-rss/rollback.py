#!/usr/bin/env python3
import argparse,json,pathlib,shutil,subprocess
p=argparse.ArgumentParser(); p.add_argument('--backup',required=True); a=p.parse_args()
home=pathlib.Path.home()/'.openclaw'; b=pathlib.Path(a.backup).resolve()
if not b.is_relative_to((home/'backups').resolve()): raise SystemExit('Invalid backup path')
r=json.loads((b/'receipt.json').read_text())
subprocess.run(['systemctl','--user','disable','--now','alphaos-rss.timer'],check=False)
subprocess.run(['systemctl','--user','stop','alphaos-rss.service'],check=False)
# Do not overwrite a new replacement framework during restoration.
for e in r['moves']:
    if pathlib.Path(e['source']).exists() and pathlib.Path(e['destination']).exists(): raise SystemExit('Restore conflict: '+e['source'])
for e in reversed(r['moves']):
    source=pathlib.Path(e['source']); dest=pathlib.Path(e['destination'])
    if dest.exists(): source.parent.mkdir(parents=True,exist_ok=True); shutil.move(str(dest),str(source))
reverted=b/'reverted-current'; reverted.mkdir(exist_ok=True)
for name in r['created']:
    p=pathlib.Path(name)
    if p.exists() and p!=pathlib.Path(__file__):
        dest=reverted/name.lstrip('/'); dest.parent.mkdir(parents=True,exist_ok=True); shutil.move(str(p),str(dest))
for name,saved in r['saved'].items():
    p=pathlib.Path(name)
    if p.exists():
        dest=reverted/name.lstrip('/'); dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dest)
    p.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(saved,p)
subprocess.run(['systemctl','--user','daemon-reload'],check=True)
subprocess.run(['systemctl','--user','restart','openclaw-gateway.service'],check=True)
print('ROLLBACK_COMPLETE; previous files restored, replaced runtime files preserved in',reverted)
