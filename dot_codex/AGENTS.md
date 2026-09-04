# Coding
- Add comments for each logical block in all code. For implementation code, explain the logic and intent. For tests, clarify what is being tested.

# Write artifacts for the present reader
- You know the diff; the reader only sees the final state. Change history goes in commits/ADRs — the artifact itself describes only the current state.
- After writing, re-read as a first-time reader and remove: mentions of things that appear nowhere else in the artifact, diff narration ("previously", "changed to"), and rationale framed against rejected options (rewrite as properties of what was chosen).
- Exceptions: ADRs, migration guides, changelogs, and warnings about traps readers will actually hit.
