# AlphaOS RSS Runtime and guarded legacy retirement

This package implements a data adapter and engineering integration only. It does not modify frozen Core/Personal Policy or add investment rules. Target: the inspected Ubuntu 24.04/OpenClaw 2026.3.8 deployment, /root/.openclaw/workspace, existing user Gateway service.

## Evidence and scope

Server results on 2026-10-06 showed old RSS outputs dated 2026-08-03, no RSS monitor process and no user-crontab RSS entry. The supplied monitor parses RSS2 only, runs once, and writes an empty alerts list when no new alerts were obtained. Some historical requests returned HTTP404. Existing report/long-term-pool scripts read rss_alerts.json. OpenClaw's separate scheduled jobs may also call scripts; their presence must be checked by the installer before retiring dependencies.

Old trading-framework-current.md and three 盘感 PDFs were previously archived outside the workspace. ai-hedge-fund has four known sys.path.insert references; JusticePlutus is exposed through skills/justice-plutus. No claim is made that all other installed skills are AlphaOS-compatible.

## Adapter behavior

collector.py accepts the existing local rss_feeds.txt (name,URL CSV format), fetches configured endpoints concurrently and parses RSS2/Atom/RSS1. It does not invent replacement feeds or fetch article bodies. Article text is untrusted data. It records original/normalized publication timestamps, fetch/last-seen time, per-source health, source identity, links and adapter provenance. Missing publication dates remain null/MISSING. Collection freshness is distinct from publication freshness.

alphaos-runtime/rss/snapshot.json is an atomic, authoritative bundle of health, sources and up to 2,000 items. Earlier items are retained on failures; configured/failed source state must be checked before use. health.json/context.md are summaries and contain run_id for reconciliation. States are HEALTHY, PARTIAL or UNAVAILABLE. A source fetch succeeding does not prove the publisher is current or the article's claim is true.

rss_alerts.json remains a compatibility list for existing consumers: only entries observed from successful sources in this run are included, using the existing tag vocabulary/routing weights extracted locally from the old monitor. Those keywords/scores are not new investment rules or Risk Engine values. On total failure the compatibility list is empty to avoid relabeling old alerts as fresh; the full last-good archive stays in snapshot.json. Legacy report scripts do not acquire AlphaOS certification merely by reading this list. News-dependent AlphaOS reasoning must check health/provenance and confirm fundamental/event facts using official materials under frozen Core.

## Installation

The pinned installer verifies component hashes and existing OpenClaw/workspace/service identity. It backs up changed scripts, AGENTS.md, RSS outputs and runtime files locally. No server code, feeds, credentials, portfolio, memory or news is uploaded.

For each of the four known reports, it removes only the exact obsolete sys.path.insert statement if Python module resolution before/after matches and no imported module is missing. It does not execute report logic, rewrite credentials, install packages, or change report heuristics. If dependency resolution differs/misses, that migration is blocked and reported. Remaining active/config/schedule/skill references block repository archival. The JusticePlutus repo and corresponding callable Skill are archived together only when there are no outside references. Archive paths and remaining skill names are reported for further review. A block means cleanup is incomplete, not permission to force removal.

A wrapper replaces rss_monitor.py so old invocation paths use the new collector. A short RSS read/freshness instruction is prepended to AGENTS.md without replacing persona/memory. A dedicated alphaos-rss Skill describes evidence boundaries. The existing Gateway restarts to refresh Skill discovery.

A user systemd oneshot service and timer collect every 15 minutes. No Feishu messages, trades or background LLM decisions are sent. The 15-minute interval and 45-minute collection freshness guard are engineering defaults, not approved investment parameters. They can be adjusted as Runtime configuration. No custom failure-count/24-hour notification policy is introduced.

The first collection reports per-feed host/name/status (no endpoint query/credentials), so failures remain visible. If all sources fail the timer still installs for retries, but RSS acceptance is UNAVAILABLE and needs source repair. HTTP404 endpoints are not automatically replaced. Existing unrelated schedules remain unchanged. Installer rejects an existing AlphaOS RSS installation rather than overwrite it.

## Acceptance and rollback

Verify timer enabled/active, next trigger, Gateway active, actual health/snapshot and source successes, then start a fresh Feishu/OpenClaw session and request news with publication/source/freshness reporting. Do not claim success from installation alone. Source repairs and remaining legacy dependencies require follow-up if reported.

The backup contains rollback.py and receipt.json. The printed rollback command disables/stops the RSS timer/service, restores moved repositories/Skill and backed-up files, preserves replaced runtime files in a reverted-current directory, reloads units and restarts Gateway. Restore conflicts stop instead of overwriting new repositories. Snapshot/prompt files created by this change are archived on rollback. Use promptly if needed: later edits to affected files are preserved in reverted-current but replaced by pre-install versions.

## Tests

Nine local unit tests pass: RSS/Atom parsing, date/provenance handling, deduplication, partial/all-source failures, last-good retention and compatibility filtering, missing-date handling, invalid/entity-bearing feeds, no-source health, and precise/idempotent search-path migration. Actual server package resolution, timer loading, source reachability and Feishu model adherence remain deployment acceptance checks.
