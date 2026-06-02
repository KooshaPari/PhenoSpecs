# PhenoSpecs - Specification Registry

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Legacy Tooling Gate](https://github.com/KooshaPari/PhenoSpecs/actions/workflows/legacy-tooling-gate.yml/badge.svg)](https://github.com/KooshaPari/PhenoSpecs/actions/workflows/legacy-tooling-gate.yml)
[![Specs](https://img.shields.io/badge/spec-markdown-blue.svg)](https://commonmark.org)

**Unified specification registry for the Phenotype ecosystem.**

This repository serves as the **central source of truth** for design specifications, requirements documents, ADRs, and API contracts across all Phenotype projects.

## The 4-role spec/governance spine

PhenoSpecs is the **ADRs / contracts** member of a four-repo spine. Each repo owns one role; they reference each other rather than maintaining competing copies.

| Repo | Role | Owns |
|------|------|------|
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | **INDEX** | Canonical ecosystem map ([ECOSYSTEM_MAP.md](https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md)) + dependency graph |
| **PhenoSpecs** (this repo) | **ADRs / contracts** | Architecture Decision Records (canonical home: [`adrs/`](adrs/)), API contracts, specs |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | **CONVENTIONS** | Patterns, methodologies — how we build |
| [phenotype-org-governance](https://github.com/KooshaPari/phenotype-org-governance) | **ENFORCEMENT** | Reusable policy workflows + `deny.toml`/license baseline |

When two documents disagree, authority follows role. `registry.yaml` here is the spec↔implementation traceability index, not the ecosystem index — `ECOSYSTEM_MAP.md` is.

---

## Quick Start

```bash
# Find a spec
ls specs/auth/                    # Auth domain specs
ls specs/crypto/                  # Crypto domain specs

# Read the registry
cat registry.yaml                 # See all registered specs

# Link to implementation
spec-links check                  # Verify spec-to-code traceability
```

---

## Registry Structure

| Directory | Purpose | Contents |
|-----------|---------|----------|
| `specs/` | Domain specifications | Feature specs by domain (auth, crypto, caching, etc.) |
| `adrs/` | Architecture decisions | ADRs in MADR format |
| `openapi/` | API contracts | OpenAPI 3.1 specifications |
| `integrations/` | Integration specs | Cross-system integration specifications |
| `registry.yaml` | Index | Central registry linking all specs to implementations |

---

## Usage

### For Developers

1. **Before implementing**: Check if spec exists in `specs/<domain>/`
2. **Before deciding**: Check `adrs/` for prior architecture decisions
3. **Before integrating**: Check `openapi/` for API contracts
4. **Traceability**: Use `spec-links` to verify spec-to-code linkage

### For Spec Authors

```bash
# Create new spec
spec-new create specs/<domain>/<feature-name>

# This creates:
#   specs/<domain>/<feature-name>/
#   ├── spec.md          # Feature specification
#   ├── frd.md           # Functional requirements
#   └── plan.md          # Implementation plan
```

---

## Connection to Implementations

Specs in this registry link to actual code via:

1. **Traceability macros** in code (Rust: `#[trace_fr(...)]`, Go: `// FR: ...`)
2. **Registry entries** in `registry.yaml` mapping specs to repos
3. **catalog-info.yaml** in each repo referencing specs

---

## Registry Index

See [registry.yaml](./registry.yaml) for complete index with:
- Spec ID → File path
- Domain classification
- Implementation repo links
- Status (draft | specified | implementing | implemented)

---

## Governance

- **New specs**: Must follow [kitty-spec format](https://github.com/KooshaPari/AgilePlus/tree/main/kitty-specs)
- **Updates**: Require ADR if architectural impact
- **Deprecation**: Move to `archive/` with migration guide
- **Traceability**: All specs must link to at least one implementation

---

## Links

- [AgilePlus CLI](https://github.com/KooshaPari/AgilePlus) - Spec-driven development
- [HexaKit](https://github.com/KooshaPari/HexaKit) - Templates
- [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) - Patterns & guidelines

## License

MIT — see [LICENSE](./LICENSE).

---

## Rich Media Stubs

<!-- RICH-MEDIA-STUB type="annotated-screenshot" subject="PhenoSpecs quickstart — first spec registered in the registry" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *Annotated screenshot of PhenoSpecs after registering the first product spec.*
<!-- END-RICH-MEDIA-STUB -->

<!-- RICH-MEDIA-STUB type="recording-gif" subject="ADR workflow — draft → review → decided" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *GIF of the ADR lifecycle from draft through to decided status.*
<!-- END-RICH-MEDIA-STUB -->

<!-- RICH-MEDIA-STUB type="recording-mp4" subject="Spec-driven development — spec → ADR → API contract flow" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *Video of the spec-driven development E2E flow: create spec, define ADR, export API contract.*
<!-- END-RICH-MEDIA-STUB -->

<!-- RICH-MEDIA-STUB type="annotated-screenshot" subject="PhenoSpecs architecture — unified specification registry layers" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *Annotated architecture diagram of the unified specification registry.*
<!-- END-RICH-MEDIA-STUB -->
