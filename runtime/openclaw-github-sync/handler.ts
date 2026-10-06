import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const run = promisify(execFile);
const marker = '<!-- ALPHAOS_GITHUB_RUNTIME -->';
export default async function handler(event: any) {
  if (event.type !== 'agent' || event.action !== 'bootstrap') return;
  const workspace = event.context?.workspaceDir;
  const files = event.context?.bootstrapFiles;
  if (!workspace || !Array.isArray(files)) return;
  let status: any = { state: 'UNAVAILABLE', error: 'sync did not complete' };
  try {
    const script = path.join(path.dirname(fileURLToPath(import.meta.url)), 'sync.py');
    const result = await run('/usr/bin/python3', [script, '--workspace', workspace], {timeout: 45000, maxBuffer: 65536});
    status = JSON.parse(result.stdout.trim());
  } catch (err: any) {
    try { status = JSON.parse(String(err.stdout).trim()); } catch {}
    console.error('[alphaos-github-sync]', status.state);
  }
  const available = status.state === 'CURRENT' || status.state === 'STALE_LAST_GOOD';
  const instruction = `${marker}
# AlphaOS GitHub Runtime
Framework sync state: ${status.state}; commit: ${status.commit || 'MISSING'}; checked_at: ${status.checked_at || 'MISSING'}.
${available ? `Use the complete verified snapshot at ${status.path}. Before AlphaOS analysis read alphaos_core_spec.md, alphaos_personal_policy.md, alphaos_usage_protocol.md and HANDOFF_RUNTIME_v0.1.md there. Read status/case/backlog when relevant. Cite this framework commit in Decision Snapshots. ${status.state === 'STALE_LAST_GOOD' ? 'Latest approved version could not be checked: disclose stale status and last success time '+(status.last_success_at || 'MISSING')+'.' : ''}` : 'No verified framework is available. Report MISSING and do not claim AlphaOS compliance or infer rules from memory.'}
For AlphaOS decisions, alphaos_core_spec.md is the sole Core authority. trading-framework-current.md, old PDFs and chat memories are historical and cannot override approved AlphaOS rules. Preserve those files.
Core and Personal Policy snapshots are read-only by governance: AI may propose changes but may not self-approve or silently mutate Core. This is not an OS security sandbox. Write runtime records/case findings under alphaos-runtime/, never upload private records automatically. Missing is Missing. Risk numbers require deterministic Risk Engine; if unavailable, report MISSING, do not invent sizing. Keep Proposed/Testing separate from Approved. No trades are authorized by this integration.
<!-- /ALPHAOS_GITHUB_RUNTIME -->\n`;
  let agents = files.find((f: any) => f.name === 'AGENTS.md');
  if (!agents) { agents = {name:'AGENTS.md', path:path.join(workspace,'AGENTS.md'), missing:false, content:''}; files.unshift(agents); }
  const old = (agents.content || '').replace(/<!-- ALPHAOS_GITHUB_RUNTIME -->[\s\S]*?<!-- \/ALPHAOS_GITHUB_RUNTIME -->\s*/g, '');
  agents.content = instruction + old;
  agents.missing = false;
}
