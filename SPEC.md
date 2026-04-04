# SPEC: PhenoSpecs — Specification Registry

## Meta

- **ID**: phenospecs-001
- **Title**: PhenoSpecs Specification — Unified Specification Registry
- **Created**: 2026-04-04
- **State**: specified
- **Version**: 1.0.0
- **Language**: YAML, Markdown, OpenAPI

---

## Overview

PhenoSpecs is the unified specification registry for the Phenotype ecosystem. It serves as the central source of truth for design specifications, requirements documents, ADRs (Architecture Decision Records), and API contracts across all Phenotype projects.

---

## ASCII Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PhenoSpecs Architecture                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │                        Specification Types                          │    │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────┐   │    │
│   │  │   specs/     │  │    adrs/     │  │   openapi/   │  │integrations│   │    │
│   │  │              │  │              │  │              │  │            │   │    │
│   │  │ Feature      │  │ Architecture │  │ API          │  │ Cross-sys  │   │    │
│   │  │ specs by     │  │ Decision     │  │ contracts    │  │ specs      │   │    │
│   │  │ domain       │  │ Records      │  │ (OpenAPI)    │  │            │   │    │
│   │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬─────┘   │    │
│   └─────────┼─────────────────┼─────────────────┼─────────────────┼───────-┘    │
│             │                 │                 │                 │              │
│   ┌─────────┴─────────────────┴─────────────────┴─────────────────┴───────────┐   │
│   │                         Registry Index (registry.yaml)                       │   │
│   │  ┌─────────────────────────────────────────────────────────────────────┐   │   │
│   │  │   Spec ID → Domain → File Path → Status → Implementations           │   │   │
│   │  │                                                                      │   │   │
│   │  │   SPEC-AUTH-001 → auth/ → specs/auth/oauth-flow/ → specified        │   │   │
│   │  │     └── phenotype-auth-ts (repo), phenotype-auth-go (repo)           │   │   │
│   │  │                                                                      │   │   │
│   │  │   ADR-012 → adrs/ → adrs/012-sdd-adoption.md → accepted              │   │   │
│   │  │                                                                      │   │   │
│   │  │   API-USER-001 → openapi/ → openapi/user-service.yaml → draft       │   │   │
│   │  └─────────────────────────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────┬──────────────────────────────────────────┘   │
│                                     │                                               │
│   ┌─────────────────────────────────┴───────────────────────────────────────────┐   │
│   │                         Traceability Layer                                     │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐          │   │
│   │  │  Traceability   │  │  Code Links     │  │  Validation             │          │   │
│   │  │  Macros         │  │  (spec-links)   │  │  (spec-links check)     │          │   │
│   │  │                 │  │                 │  │                         │          │   │
│   │  │ Rust: #[trace]  │  │ spec → code     │  │ Verify FR → code        │          │   │
│   │  │ Go: // FR: ...  │  │ code → spec     │  │ coverage                │          │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘          │   │
│   └───────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                       │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                         Consumer Interfaces                                  │   │
│   │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐        │   │
│   │  │  Developers       │  │  CI/CD           │  │  Agents/AI             │        │   │
│   │  │                 │  │                 │  │                         │        │   │
│   │  │ specs.pheno.dev │  │ spec-links check│  │ spec query tool         │        │   │
│   │  │ GitHub browser  │  │ PR validation   │  │ implementation search   │        │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘        │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Components Table

| Component | Path | Language | Responsibility | Status |
|-----------|------|----------|----------------|--------|
| **Specs** | `specs/` | Markdown | Feature specifications by domain | Active |
| **ADRs** | `adrs/` | Markdown | Architecture Decision Records | Active |
| **OpenAPI** | `openapi/` | YAML/JSON | API contracts | Active |
| **Integrations** | `integrations/` | Markdown | Cross-system integration specs | Active |
| **Registry** | `registry.yaml` | YAML | Central index linking all specs | Active |

---

## Data Models

### Specification Document
```yaml
---
id: SPEC-AUTH-001
title: OAuth 2.0 Authentication Flow
domain: auth
status: specified  # draft | specified | implementing | implemented
created: 2024-01-15
updated: 2024-03-20
author: @kooshapari
---

# OAuth 2.0 Authentication Flow

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-001 | Support authorization code flow | P0 |
| FR-002 | Support PKCE extension | P0 |
| FR-003 | Support refresh token rotation | P1 |

## Technical Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| TR-001 | Token lifetime | 15 min access, 7 day refresh |
| TR-002 | Encryption | AES-256-GCM |

## Data Model

```typescript
interface AuthSession {
  id: string;
  userId: string;
  accessToken: string;
  refreshToken: string;
  expiresAt: DateTime;
}
```

## Implementation Links

- phenotype-auth-ts: `src/oauth/`
- phenotype-auth-go: `oauth/`
```

### Registry Entry
```yaml
# registry.yaml format
version: "1.0"
specs:
  auth:
    oauth-flow:
      id: SPEC-AUTH-001
      path: specs/auth/oauth-flow/spec.md
      domain: auth
      status: specified
      frd_path: specs/auth/oauth-flow/frd.md
      plan_path: specs/auth/oauth-flow/plan.md
      implementations:
        - repo: phenotype-auth-ts
          path: src/oauth/
          status: implemented
        - repo: phenotype-auth-go
          path: oauth/
          status: implementing
      
  adrs:
    sdd-adoption:
      id: ADR-012
      path: adrs/012-sdd-adoption.md
      status: accepted  # proposed | accepted | deprecated | superseded
      date: 2024-01-15
```

---

## Specification Domains

| Domain | Description | Count |
|--------|-------------|-------|
| **auth** | Authentication & authorization | 10+ |
| **crypto** | Cryptographic operations | 5+ |
| **caching** | Caching strategies | 8+ |
| **database** | Data storage & access | 12+ |
| **api** | API design & implementation | 15+ |
| **integration** | System integrations | 10+ |
| **frontend** | UI/UX patterns | 8+ |
| **deployment** | CI/CD & infrastructure | 10+ |

---

## ADR Format (MADR)

```markdown
# ADR-012: Adopt SDD (Spec-Driven Development)

## Status
Accepted

## Context
Need consistent approach to feature development across teams.

## Decision
Adopt spec-driven development (SDD) methodology.

## Consequences
- Pros: Clear requirements, better traceability
- Cons: Additional upfront documentation

## Related
- ADR-011: Documentation-first approach
- Supersedes: ADR-005 (TDD-only approach)
```

---

## Traceability

### Code Annotations

**Rust:**
```rust
#[trace_fr(spec = "SPEC-AUTH-001", fr = "FR-001")]
fn authorize(request: AuthRequest) -> AuthResponse {
    // Implementation
}
```

**Go:**
```go
// FR: SPEC-AUTH-001 FR-002 - PKCE support
func GeneratePKCE() (*PKCEPair, error) {
    // Implementation
}
```

### Validation
```bash
# Check spec-to-code traceability
spec-links check

# Verify FR coverage
spec-links coverage SPEC-AUTH-001

# Find unlinked specs
spec-links unlinked
```

---

## Dependencies

| Tool | Purpose |
|------|---------|
| **spec-links** | Traceability verification CLI |
| **markdownlint** | Markdown linting |
| **yamllint** | YAML validation |
| **openapi-generator** | API client generation |

---

## Workspace Structure

```
PhenoSpecs/
├── specs/                     # Feature specifications
│   ├── auth/
│   ├── crypto/
│   ├── caching/
│   └── ...
├── adrs/                      # Architecture Decision Records
│   ├── 001-adr-format.md
│   ├── 012-sdd-adoption.md
│   └── ...
├── openapi/                   # API contracts
│   ├── user-service.yaml
│   ├── auth-service.yaml
│   └── ...
├── integrations/              # Integration specs
│   ├── workos-integration.md
│   └── ...
├── registry.yaml              # Central index
├── catalog-info.yaml          # Backstage catalog
└── README.md
```

---

## References

1. [MADR](https://adr.github.io/madr/) — Markdown ADR format
2. [OpenAPI](https://www.openapis.org/) — API specification standard
3. [Backstage](https://backstage.io/) — Developer portal (catalog-info.yaml)
4. [AgilePlus](https://github.com/KooshaPari/AgilePlus) — Spec-driven development CLI

---

*Generated: 2026-04-04*
