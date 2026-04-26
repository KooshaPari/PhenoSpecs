# AGENTS.md — PhenoSpecs

Unified specification registry for the Phenotype ecosystem — central source of truth for design specs, requirements, ADRs, and API contracts.

## Repository identity

- Documentation-only registry (no code build).
- Canonical index: `registry.yaml` (root).
- Catalog metadata: `catalog-info.yaml` (Backstage-style).
- Top-level docs: `SPEC.md`, `PRD.md`, `ADR.md`, `PLAN.md`, `CHARTER.md`, `RESEARCH.md`.

## Layout (verified from root listing)

| Directory      | Purpose |
|----------------|---------|
| `specs/`       | Domain feature specs (auth, crypto, caching, …) |
| `adrs/`, `adr/`| Architecture Decision Records (MADR format) |
| `docs/`        | Long-form documentation |
| `research/`    | Research notes |
| `archive/`     | Retired specs |
| `worklog.md`   | Running worklog |

## Build & test

No build. Validation is markdown + registry consistency:

```bash
# Browse specs and the registry
ls specs/
cat registry.yaml
```

Spec-link tooling (`spec-links`, `spec-new`) is referenced in the README but lives in sibling Phenotype repos — install separately.

## Governance

- Triple license: MIT / Apache-2.0 (`LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT`).
- Charter: `CHARTER.md`. Security: `SECURITY.md`. Contributing: `CONTRIBUTING.md`.
- Versioning: see `VERSION`.

## Commit & branch convention

- Conventional Commits (`docs:` is the dominant type for spec changes).
- Branch: `<type>/<topic>` (e.g. `docs/auth-spec-v2`).
- PRs to `main` only; specs in `archive/` are immutable.

## Agent guardrails

- Never edit files under `archive/`.
- Spec changes MUST update `registry.yaml` to keep the central index accurate.
