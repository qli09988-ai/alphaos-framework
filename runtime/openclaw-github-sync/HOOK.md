---
name: alphaos-github-sync
description: "Verify approved AlphaOS GitHub snapshot before agent bootstrap"
metadata:
  { "openclaw": { "emoji": "🔗", "events": ["agent:bootstrap"], "requires": { "bins": ["python3"] } } }
---

Fetches the approved release manifest from the runtime branch, verifies all nine documents from one immutable commit, and atomically activates a complete snapshot. Adds authority and freshness instructions to in-memory AGENTS bootstrap content. Does not replace workspace AGENTS/SOUL/MEMORY, run trades, or push server data. On network failure a verified last-good snapshot is labeled stale; no valid snapshot means unavailable.
