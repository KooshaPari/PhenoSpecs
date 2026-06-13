# Absorbed Repository Records

This directory captures the design history of KooshaPari repositories that
have been **archived and deleted** as part of the org rationalization.

## When a repo lands here

A repository is moved to this directory and then deleted from GitHub when
**all** of the following are true:

1. The repo is archived at the GitHub level (or was never active).
2. The repo has **zero source code** that consumers depend on (or
   the source has been absorbed into a canonical home).
3. The repo has **zero consumers** in the KooshaPari org (verified by
   `gh search code`).
4. The repo's npm/Cargo/PyPI package either never existed or has been
   migrated.
5. The only useful artefact is documentation (PRD, FR, ADR, etc.).

## What we preserve

For each absorbed repo, we save a single `<repo>.md` file with:

- The original purpose
- The reason for absorption
- Verbatim copies of the design documents (PRD/FR/ADR/README) in
  collapsible `<details>` blocks
- A pointer to the canonical home for any implementation work
  (typically `phenodocs/packages/design/` or the relevant PhenoSpecs spec)

## What we do NOT preserve

- Source code (move to the canonical home instead)
- CI/workflow files (the husk's lifecycle is over)
- Branch protection / governance metadata (audit log only)
- Issue / PR history (already captured in `phenotype-org-audits`)

## When NOT to absorb-and-delete

- A repo with active consumers (migrate them first)
- A repo that is the canonical home for a tool (keep it)
- A repo with a published package that real users install
  (deprecate via npm deprecation notice, then archive)

## See also

- `RATIONALIZATION_PLAN.md` (root of the org) — overall target shape
- `PhenoSpecs/specs/platform/019-private-repo-catalog/` — catalog
  of private repos and their fates
- `phenotype-org-audits/inventory/` — authoritative inventory
