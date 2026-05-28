# Archived Repository Documentation

This directory contains documentation from deprecated/archived repositories that have been preserved for reference.

## Contents

### agent-wave/
Documentation from `KooshaPari/agent-wave` - an AI-powered agentic workflow system.
- **Status**: Archived on GitHub
- **Content**: AGENTS.md (110KB), SPEC.md, ADR.md, CLAUDE.md, docs/
- **Preserved**: 2026-04-05

### Flowra
Documentation from `KooshaPari/Flowra` - a workflow automation platform concept.
- **Status**: ✅ **MOVED** to [HexaKit/Flowra/](https://github.com/KooshaPari/HexaKit/tree/main/Flowra)
- **Content**: SPEC.md (96KB), PLAN.md (45KB), CHARTER.md, ADR.md, PRD.md
- **Integrated**: 2026-04-05 (removed from archive, now in HexaKit proper)

## Archival entry template

Use this format when preserving documentation for repos or repo areas that are archived, deprecated, or moved:

```md
### <repo-or-area>/
Documentation from `KooshaPari/<repo>`.

- **Status**: Archived | Moved | Deprecated
- **Source**: `KooshaPari/<repo>`
- **Preserved**: YYYY-MM-DD
- **Replacement / Destination**: `<target repo or path>`
- **Content**: `SPEC.md, PLAN.md, ADR.md, docs/`
- **Notes**: `<short rationale or migration note>`
```

## Notes

These repositories were deprecated as part of the Phenotype ecosystem consolidation:
- `agent-wave` → Concepts integrated into AgilePlus agents
- `Flowra` → Reactive data flow concepts moved to HexaKit
- `forgecode` → Rust source code moved to HexaKit/forgecode-fork/

When adding a new archive entry, include the source repo, preservation date, and the current replacement or destination so future triage can trace the migration path.

The documentation is preserved here for historical reference and potential future reuse.
