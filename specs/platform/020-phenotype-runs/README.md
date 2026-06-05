# phenotype-runs

Universal CI/job observability substrate for the Phenotype org.

**Source repo:** https://github.com/KooshaPari/phenotype-runs
**Status:** scaffold (source repo README only — no SPEC.md authored yet)
**Steward:** spec-gov domain
**Number:** 020

## Summary

- **What:** Centralized run/observability substrate that ingests CI job events from
  every Phenotype repo (GitHub Actions + Temporal workflows + ad-hoc agent runs)
  and exposes a single queryable timeline.
- **Why today:** Each repo currently rolls its own logging; cross-repo traceability
  requires a shared run store. phenotype-runs is the canonical surface.
- **How it fits:** Sits next to phenotype-gates (which decides *whether* a run
  proceeds) — runs is the system of record for *what actually happened*; gates
  consumes the run stream as audit input.
- **Sub-domain:** platform / CI & workflow observability
- **Consumers (planned):** AgilePlus (story evidence), Tracera (TraceLinks),
  phenotype-dep-guard (failed-run gating), PhenoObservability (telemetry fan-in).

## Full Specification

> The source repo (KooshaPari/phenotype-runs) currently contains only a
> one-line README. The full SPEC.md must be authored in the source repo
> before this entry can be promoted from `scaffold` → `specified`. Once
> authored, link it here.
