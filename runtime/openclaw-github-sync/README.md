# AlphaOS OpenClaw GitHub integration

Target inspected on 2026-10-06: Ubuntu 24.04, OpenClaw 2026.3.8, Node 22.22.1, Python 3.12.3, user service openclaw-gateway.service, workspace /root/.openclaw/workspace.

This operational package adds no investment rules and does not modify frozen documents. The runtime branch carries an approved-release manifest. It currently pins framework commit c9c676f9127a4c57ba90c7dfdf501015f802fed9, on freeze/alphaos-v0.1. The repository main branch is not the framework entry point.

## Behavior

Before agent bootstrap, a native hook reads the public GitHub manifest, validates its repository/status/paths and fetches nine documents at the manifest's exact commit. SHA256 verification precedes an atomic switch of alphaos-framework/current. Verified snapshots stay under alphaos-framework/releases. status.json records CURRENT, STALE_LAST_GOOD or UNAVAILABLE and timestamps. A stale snapshot is disclosed; an invalid local snapshot is never used as fallback.

The hook prepends a short authority/version/path instruction to the in-memory AGENTS.md bootstrap. Existing AGENTS/SOUL/TOOLS/USER/MEMORY files remain unchanged. Documents are available for task-specific reading rather than all being injected into the prompt. Actual model adherence and successful production hook loading require server/new-session acceptance checks.

Governance read-only is not a root-user security boundary. SHA256 detects divergence from the manifest, not malicious changes by repository writers. Approval declarations are maintained by the human-approved release process; AI cannot approve its own framework updates. For strict isolation use a separate OS identity or sandbox in a later runtime change after inspecting requirements.

No credentials are required to read this public repository. No server documents, portfolio data, cookies, private records or configuration are uploaded. Runtime records belong in alphaos-runtime/. The existing trading-framework-current.md and PDFs are retained as historical material.

## Installation and rollback

Download install.py from an exact published runtime commit, inspect it if desired, and run with --commit set to that same commit. The installer checks the inspected version/workspace/service, backs up configuration and relevant workspace documents locally, verifies downloaded runtime file hashes, requires a successful initial framework sync, enables the hook and restarts the existing user Gateway service. Installation errors restore the saved configuration. An existing hook is never overwritten.

After installation run openclaw hooks info alphaos-github-sync, openclaw hooks check, systemctl --user is-active openclaw-gateway.service, and read alphaos-framework/status.json. Then start a new OpenClaw conversation and ask it to read and report the exact framework commit, sole Core file, personal policy separation, and risk-engine missing behavior before accepting deployment.

The installer prints a rollback command. Rollback removes only this hook configuration entry, preserves unrelated later settings, archives the disabled hook into the backup, and restarts the service. Snapshot caches/runtime records remain available. Persona/memory files were never changed.

## Future approved versions

After Human Approval, publish a complete framework commit, update approved_release.json with that immutable commit and the nine document hashes, and commit the manifest to runtime/openclaw-github-sync. OpenClaw fetches it during the next agent bootstrap. A running conversation may retain previous context; verify version in a fresh conversation after releases. This is event-triggered synchronization, not a background polling schedule. Runtime code upgrades require an explicit reviewed installation; the hook does not execute new code from a moving branch.

No Core changes, new research, trading actions, Risk Engine implementation, OpenClaw upgrades or Feishu plugin repairs are included.

## Validation

Five Python tests pass for atomic activation, repeated sync, corrupted remote content, unavailable network, tampered local fallback, path traversal and unapproved manifest rejection. Node hook tests pass for content preservation, idempotence, authority injection, unavailable status and ignored unrelated events. Local hook tests used Node 24; actual Node 22/OpenClaw loader acceptance remains a server check.
