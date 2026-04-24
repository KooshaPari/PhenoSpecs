# Changelog

All notable changes to this project will be documented in this file.

## 📚 Documentation
- Docs: add README/SPEC/PLAN (`2beb700`)
## ✨ Features
- Feat(specs): add Queris and Cursora specs from scaffold repos

Extracted from deleted scaffold repos:
- Queris: Database abstraction layer specs (83KB) -> specs/storage/queris/
- Cursora: Pagination utility specs -> specs/platform/cursora/

These repos were scaffold-only with zero implementation. Specs preserved for future reference. (`592c7f2`)
- Feat: add 3 ADRs - Hexagonal Architecture, NATS/JetStream, Property-Based Testing (`a309861`)
- Feat: populate with specs from AgilePlus and initial ADRs (`53eff65`)
## 🔨 Other
- Chore(governance): adopt standard CLAUDE.md + AGENTS.md + worklog (wave-2) (`503ec96`)
- Add phenoForge specs to platform/build-system/ (`31b669a`)
- Reorganize specs into domain structure: crypto/, platform/, sdks/ (`2669c46`)
- Archive: move Flowra docs to HexaKit proper

Flowra documentation has been integrated directly into HexaKit:
- Removed Flowra/ directory from archive (5,419 lines)
- Content now lives in KooshaPari/HexaKit/Flowra/
- Updated README.md to reflect new location

The Flowra submodule has been replaced with actual files in HexaKit. (`180f059`)
- Archive: preserve documentation from deprecated repos (agent-wave, Flowra)

- Add agent-wave documentation (AGENTS.md, SPEC.md, CLAUDE.md, docs/)
- Add Flowra documentation (SPEC.md, PLAN.md, CHARTER.md, ADR.md, PRD.md)
- Add archive README explaining provenance

These repos were archived on GitHub; content preserved in PhenoSpecs
for historical reference before local deletion. (`43d4677`)
- Chore: migrate patching SOTA research from archived phenotype-patch (`b264061`)
- Add archived project specs: Portalis, Guardis, Datamold (`1778e13`)
- Chore: migrate research docs from archived repos

- Flagward: feature flag SOTA, patterns, storage/eval/audit/realtime ADRs
- Seedloom: secrets management SOTA research

These archives had no implementation, only documentation worth preserving. (`3c859c4`)
- Chore: add AgilePlus scaffolding (`d1a2370`)
- Ci(legacy-enforcement): add legacy tooling anti-pattern gate (WARN mode)

Adds legacy-tooling-gate.yml monitoring per CLAUDE.md Technology Adoption Philosophy.

Refs: phenotype/repos/tooling/legacy-enforcement/ (`b1726bf`)
- Chore: add untracked patterns/specs (`772865c`)
- Initial commit: PhenoSpecs specification registry (`af6608e`)