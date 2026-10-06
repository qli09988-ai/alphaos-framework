import {mkdtemp,readFile,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
const dir=await mkdtemp(path.join(tmpdir(),'alphaos-hook-test-'));
try {
  await writeFile(path.join(dir,'handler.ts'),await readFile(new URL('./handler.ts',import.meta.url)));
  await writeFile(path.join(dir,'sync.py'),`import json\nprint(json.dumps({'state':'CURRENT','commit':'${'a'.repeat(40)}','path':'/test/snapshot','checked_at':'fixture'}))\n`);
  const {default:handler}=await import(pathToFileURL(path.join(dir,'handler.ts')));
  const agents={name:'AGENTS.md',content:'Existing persona and instructions',missing:false};
  const event={type:'agent',action:'bootstrap',context:{workspaceDir:'/test/workspace',bootstrapFiles:[agents]}};
  await handler(event);
  assert(agents.content.includes('Existing persona and instructions'));
  assert(agents.content.includes('/test/snapshot'));
  assert(agents.content.includes('sole Core authority'));
  await handler(event);
  assert.equal(agents.content.split('<!-- ALPHAOS_GITHUB_RUNTIME -->').length,2);
  await writeFile(path.join(dir,'sync.py'),`print('{"state":"UNAVAILABLE"}')\nraise SystemExit(1)\n`);
  await handler(event); assert(agents.content.includes('No verified framework is available'));
  assert(!agents.content.includes('/test/snapshot'));
  const before=agents.content;
  await handler({...event,type:'message',action:'received'}); assert.equal(agents.content,before);
  console.log('PASS: bootstrap preserves content, injects authority, is idempotent, handles unavailable, ignores other events.');
} finally { await rm(dir,{recursive:true,force:true}); }
