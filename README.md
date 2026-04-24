# PhenoSpecs — Unified Specification Registry

Central source of truth for design specifications, functional requirements, architecture decisions, and API contracts across the Phenotype ecosystem. Enables spec-driven development with full traceability from requirements to implementation.

## Overview

**PhenoSpecs** is the specification spine of the Phenotype organization. It maintains domain-organized specifications, architecture decision records (ADRs), and OpenAPI contracts that drive implementation across all Phenotype projects. Integration with AgilePlus ensures specs are linked to work packages and test traceability.

**Core Mission**: Provide a single authoritative source for specifications, decisions, and contracts while maintaining automated traceability from spec to code to test.

## Technology Stack

- **Specification Format**: Markdown + YAML (compatible with AgilePlus kitty-specs)
- **Architecture Decisions**: MADR (Markdown Architecture Decision Records)
- **API Contracts**: OpenAPI 3.1
- **Traceability**: registry.yaml with cross-repo linking
- **Integration**: AgilePlus CLI for spec synchronization
- **Tooling**: Custom spec-links validator

## Key Features

- **Domain-Organized Specs**: Auth, crypto, caching, storage, observability, plugins, etc.
- **Traceability**: Automatic linking from specs to implementation code via FR identifiers
- **Architecture Decisions**: MADR-format ADRs with status tracking (proposed/accepted/deprecated)
- **API Contracts**: OpenAPI 3.1 specifications for all REST endpoints
- **Unified Registry**: `registry.yaml` maps spec IDs to repos, docs, and status
- **Versioning**: Historical tracking of spec evolution with deprecation paths
- **Quality Gates**: Validation that all specs have >= 1 implementation link
- **Integration Hub**: Single source for AgilePlus work package creation

## Quick Start

```bash
# Navigate to repo
cd /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoSpecs

# Find a spec by domain
ls specs/auth/                    # Authentication specs
ls specs/crypto/                  # Cryptography specs
ls specs/observability/           # Observability specs

# Review the master registry
cat registry.yaml                 # All spec IDs, repos, status

# Verify spec-to-code traceability
./scripts/spec-links check       # Missing links/broken refs

# Link a new implementation
./scripts/spec-links add <SPEC-ID> --repo <REPO> --path <FILE>
```

## Project Structure

```
PhenoSpecs/
├── README.md                     # This file
├── CLAUDE.md                     # Governance guidelines
├── registry.yaml                 # Master spec registry & index
├── specs/                        # Domain-organized specifications
│   ├── auth/                    # Authentication/authorization specs
│   │   ├── oauth-oidc/
│   │   │   ├── spec.md          # Feature specification
│   │   │   ├── frd.md           # Functional requirements
│   │   │   ├── plan.md          # Implementation plan
│   │   │   └── user-journeys.md # User flows
│   │   └── jwt/
│   ├── crypto/                  # Cryptography specs
│   ├── observability/           # Tracing, metrics, logs
│   ├── storage/                 # Data persistence
│   ├── plugins/                 # Plugin system specs
│   ├── infra/                   # Infrastructure specs
│   └── integrations/            # Cross-system integration specs
├── adrs/                         # Architecture Decision Records
│   ├── ADR-001-hexagonal-arch.md
│   ├── ADR-002-plugin-system.md
│   └── ...
├── openapi/                      # OpenAPI 3.1 API contracts
│   ├── auth-api.yaml
│   ├── observability-api.yaml
│   └── ...
├── archive/                      # Deprecated/superseded specs
│   └── old-cache-strategy/
├── scripts/
│   ├── spec-links               # Spec traceability validator
│   ├── create-spec.sh           # New spec template generator
│   └── validate-specs.sh        # YAML/Markdown validation
├── docs/
│   ├── SPEC_FORMAT.md           # How to write specs
│   ├── ADR_FORMAT.md            # How to write ADRs
│   ├── TRACEABILITY.md          # FR linking guide
│   └── REGISTRY_USAGE.md        # registry.yaml reference
└── LICENSE                       # Apache 2.0
```

## Registry Structure

### `specs/<domain>/<feature>/` Directory

Each specification contains:

```
specs/auth/oauth-oidc/
├── spec.md                  # Executive summary + design overview
├── frd.md                   # Functional requirements (FR-xxx-nnn)
├── plan.md                  # Implementation phases & WBS
├── user-journeys.md         # User stories and flows
└── examples/                # Code examples & integration guides
```

### `adrs/` — Architecture Decisions

ADRs in MADR format with status tracking:

```
ADR-001-hexagonal-architecture.md
├── Status: Accepted
├── Date: 2026-01-15
├── Decision: Use hexagonal (ports & adapters) architecture
├── Consequences: clear boundaries, testability, flexibility
└── Links to affected specs: auth-*, crypto-*, storage-*
```

### `openapi/` — API Contracts

OpenAPI 3.1 specifications for REST APIs:

```yaml
openapi: 3.1.0
info:
  title: Auth API
  version: 1.0.0
paths:
  /oauth/authorize:
    post:
      operationId: authorize
      description: "Traces to: FR-AUTH-001, FR-AUTH-002"
```

### `registry.yaml` — Master Index

Master registry linking all specs:

```yaml
specs:
  SPEC-AUTH-001:
    title: "OAuth 2.0 + OIDC"
    file: specs/auth/oauth-oidc/spec.md
    frd: specs/auth/oauth-oidc/frd.md
    domain: authentication
    status: implemented
    implementations:
      - repo: AuthKit
        file: src/oauth.rs
      - repo: phenotype-auth-ts
        file: src/oauth.ts
  SPEC-CACHE-001:
    title: "Two-Tier LRU Cache"
    file: specs/storage/cache/spec.md
    status: implemented
    implementations:
      - repo: phenotype-cache-adapter
        file: src/lib.rs
```

## Spec Lifecycle

| Stage | Status | Actions |
|-------|--------|---------|
| **Planning** | Draft | Author spec, get feedback, refine |
| **Ready** | Specified | Finalize FRs, create AgilePlus work packages |
| **Active** | Implementing | Code under development, tests being written |
| **Done** | Implemented | Code merged, all tests pass, linked in registry |
| **Maintenance** | Stable | Updates via ADR when needed |
| **End-of-Life** | Deprecated | Move to archive/, create migration guide |

## Traceability: Spec → Code → Test

### In Code (Rust example)

```rust
/// Traces to: FR-AUTH-001 (OAuth token validation)
pub fn validate_token(token: &str) -> Result<Claims> {
    // Implementation
}

#[cfg(test)]
mod tests {
    #[test]
    // Traces to: FR-AUTH-001
    fn test_validate_token_success() {
        // Test code
    }
}
```

### In Code (Go example)

```go
// ValidateToken traces to FR-AUTH-001
func ValidateToken(token string) (*Claims, error) {
    // Implementation
}

func TestValidateToken(t *testing.T) {
    // Test code traces to FR-AUTH-001
}
```

### In registry.yaml

```yaml
specs:
  SPEC-AUTH-001:
    implementations:
      - repo: AuthKit
        file: src/oauth.rs
        tests:
          - test_validate_token_success
```

## Related Phenotype Projects

- **AgilePlus** — Work tracking system; creates WPs from specs
- **PhenoLibs** — Shared libraries following PhenoSpecs contracts
- **AuthKit** — Implements authentication specs
- **phenotype-cache-adapter** — Implements caching specs

## Spec Authors Guide

### Creating a New Spec

```bash
./scripts/create-spec.sh \
  --domain auth \
  --name oauth-oidc \
  --title "OAuth 2.0 + OIDC Implementation"
```

This creates:

```
specs/auth/oauth-oidc/
├── spec.md              # Feature overview
├── frd.md               # Functional requirements
├── plan.md              # Implementation plan (WBS)
└── user-journeys.md     # User stories
```

### Spec Template Structure

1. **Executive Summary** — 1 paragraph: what, why, who cares
2. **Problem Statement** — Current pain points
3. **Solution Overview** — High-level approach
4. **Architecture** — Design diagrams, components
5. **Functional Requirements** — FR-xxx-nnn list
6. **Integration Points** — Which systems integrate
7. **Success Criteria** — How we validate completion
8. **Open Questions** — Unresolved design points

### Creating a New ADR

```bash
./scripts/create-adr.sh \
  --number 015 \
  --title "Plugin System Architecture" \
  --status proposed
```

## Validation & Quality Gates

```bash
# Check all specs have implementations
./scripts/spec-links check --strict

# Validate YAML syntax
./scripts/validate-specs.sh

# Check for broken cross-references
./scripts/check-links.sh
```

## Configuration

Create `~/.phenotype-specs.toml`:

```toml
[registry]
canonical_path = "/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoSpecs"

[agileplus]
api_url = "http://localhost:8080/agileplus"

[validation]
require_frd = true
require_plan = true
require_implementations = true
```

## License & Governance

Licensed under Apache 2.0. See `LICENSE`. Governance in `CLAUDE.md`. Spec format guide in `docs/SPEC_FORMAT.md`. ADR format in `docs/ADR_FORMAT.md`. Traceability requirements in `docs/TRACEABILITY.md`.
