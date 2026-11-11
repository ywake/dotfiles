# Common
- Always respond in Japanese.

# Coding
- Add comments for each logical block in all code. For implementation code, explain the logic and intent. For tests, clarify what is being tested.

## Choosing between options
- When the cheapest option right now would almost certainly have to be reworked later (split, replaced, etc.), choose the post-rework structure from the start. Reworking later adds migration, re-pointing references, redoing CI and config, and re-review, so it costs more than building that structure up front.
- Bring forward only the structure: where things live, boundaries, interfaces. Keep the contents to what is needed now; mocks and stub implementations stay placeholders.
- Treat rework as "almost certain" when any of the following holds:
  - A plan to rework is written in an issue, design doc, or ADR.
  - A reason to split already exists (differing dependencies, release cadence, permissions, owners, etc.).
  - Replacing placeholder contents (mocks, stub implementations, etc.) with the real thing is already decided.
- For a "might need it someday" that meets none of these, choose the cheapest option right now (YAGNI).
- When you choose the post-rework structure, add a brief note on which condition was met.
- When presenting options, list side by side the extra effort of choosing the post-rework structure now and the effort of reworking later.
- This section takes precedence over the default of choosing the smallest diff.

# Write artifacts for the present reader
- You know the diff; the reader only sees the final state. Change history goes in commits/ADRs — the artifact itself describes only the current state.
- After writing, re-read as a first-time reader and remove: mentions of things that appear nowhere else in the artifact, diff narration ("previously", "changed to"), and rationale framed against rejected options (rewrite as properties of what was chosen).
- Exceptions: ADRs, migration guides, changelogs, and warnings about traps readers will actually hit.
