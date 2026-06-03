---
id: ADR-017
title: Spec-Completion & Repo-Baseline Measurement Rubric
status: accepted
date: 2026-06-02
tags: [governance, measurement, spec, quality, traceability]
---

# ADR-017: Spec-Completion & Repo-Baseline Measurement Rubric

## Status

Accepted

## Context

The org's "done" signals were surface-level (a README header, a green CI badge) and did not reflect whether a repo actually **builds**, is **functional**, is **tested**, or whether its **spec is both SOTA and matched by the code**. Default posture is now **ASSUME-BROKEN**: a repo is presumed non-functional / spec-incomplete until measured otherwise, with proof.

This ADR defines the canonical rubric so every repo is measured the same way, the numbers are comparable across the org, and the result is enforceable (governance) and indexed (registry).

## Decision

Every repo is scored on a **Repo-Baseline** with these dimensions, each RED / YELLOW / GREEN with evidence:

| Dimension | GREEN | YELLOW | RED |
|-----------|-------|--------|-----|
| **build** | builds clean from a fresh checkout | builds with warnings | does not build |
| **functional** | a functional smoke (run/CLI/tool-call/docs-build) succeeds | partial | no runnable proof |
| **coverage** | test coverage ≥ 70% | 30–70% | < 30% or no tests |
| **lint** | linter/formatter pass-rate 100% | 1–N nits | fails / none configured |
| **spec-present** | SPEC.md (or specs/) exists and is non-stub | thin/partial | none |
| **spec-SOTA** | spec reflects current best practice + real scope | dated/partial | stale stub / aspirational |
| **code-matches-spec** | implemented surface matches the spec | drift | spec describes unbuilt system |

### Spec-completion is measured BOTH ways

1. **Spec quality** (`spec-present` + `spec-SOTA`): is the spec itself complete and state-of-the-art, not a stale stub?
2. **Spec fidelity** (`code-matches-spec`): does the code actually implement what the spec says?

A repo's **spec-completion %** = mean of the two axes, scored per the table. Both must be high to count as "spec-complete".

### Repo-Baseline % (headline number)

`baseline% = weighted mean` of the 7 dimensions (build/functional weighted highest, since assume-broken). Reported per repo as a single 0–100 with the per-dimension RED/YELLOW/GREEN breakdown + evidence link (CI run / command output). **Telemetry ≠ truth: every GREEN needs a reproducible command, not a claim.**

## Implementation

- **governance** owns the measurement mechanism: `scripts/repo-baseline.sh` emits per-repo JSON for the machine-checkable dimensions (build/functional/coverage/lint/spec-present); spec-SOTA + code-matches-spec are steward-assessed and recorded.
- **registry** indexes the aggregated result in a `STATE.md` dashboard (per-repo baseline% + dimension grid), regenerated as repos are measured.
- **PhenoHandbook** documents the bar (this rubric is the reference).
- Traceability: spec dimensions tie to FR/NFR IDs in Tracera (requirement→code→test→PR), so spec-fidelity is checkable, not asserted.

## Consequences

### Positive
- One comparable number per repo; "done" becomes measured, not surface.
- Assume-broken is operationalized — RED until proven GREEN with a command.
- Enforceable: governance can gate on baseline dimensions; registry surfaces the real org state.

### Negative
- Spec-SOTA + code-matches-spec require steward judgment (not fully automatable); mitigated by requiring an evidence note per assessment.
- Initial measurement pass is large (≈110 repos); done incrementally, highest-leverage first.

## Related

- [ADR-006](006-traceability-first-development.md) — Traceability-First Development
- [ADR-003](003-spec-driven-development.md) — Spec-Driven Development
- PhenoHandbook `patterns/spine-roles.md` — 4-role spine (registry=index, governance=enforcement)
