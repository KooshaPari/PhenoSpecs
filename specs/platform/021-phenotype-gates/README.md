# phenotype-gates

Policy-as-code gate engine for the Phenotype org.

**Source repo:** https://github.com/KooshaPari/phenotype-gates
**Status:** scaffold (source repo README only — no SPEC.md authored yet)
**Steward:** spec-gov domain
**Number:** 021

## Summary

- **What:** Declarative policy-as-code engine that evaluates merge/CI/release
  gates across the org (license allowlists, dependency-freshness, evidence
  completeness, agent-reviewer coverage) and blocks PRs on violation.
- **Why today:** Hard rails (no-delete, protected repos, evidence-required merges)
  are enforced ad-hoc; phenotype-gates makes them declarative, testable, and
  versioned alongside the policy itself.
- **How it fits:** Pairs with phenotype-runs (system of record) — gates
  *consumes* run results + PhenoSpecs registry + dependency manifests to make
  pass/fail decisions; runs is the audit log of those decisions.
- **Sub-domain:** platform / policy & governance automation
- **Consumers (planned):** every Phenotype repo's CI, AgilePlus definition-of-done,
  Tracera evidence gates, dep-guard re-entry into the 3 delegation channels.

## Full Specification

> The source repo (KooshaPari/phenotype-gates) currently contains only a
> one-line README. The full SPEC.md must be authored in the source repo
> before this entry can be promoted from `scaffold` → `specified`. Once
> authored, link it here.
