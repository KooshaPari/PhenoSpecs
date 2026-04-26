# Agent Rules - phenotype-registry

**This project is managed through AgilePlus.**

## Overview

Phenotype-Registry is the central repository and package management system for the Phenotype ecosystem. It provides artifact storage, dependency resolution, versioning, and distribution services for all Phenotype components across multiple languages and platforms.

### Purpose & Goals

- **Mission**: Provide a unified registry for all Phenotype artifacts with enterprise reliability
- **Primary Goal**: Enable consistent dependency management across polyglot Phenotype services
- **Secondary Goals**:
  - Support multiple package formats (Cargo, npm, Go modules, PyPI)
  - Provide private registry capabilities for internal packages
  - Enable artifact signing and verification
  - Support geo-replicated distribution

### Key Responsibilities

1. **Artifact Storage**: Store and version binary artifacts, source packages
2. **Dependency Resolution**: Resolve transitive dependencies across ecosystems
3. **Distribution**: CDN-backed artifact delivery
4. **Authentication**: User and service authentication, access control
5. **Metadata**: Package metadata, documentation, provenance
6. **Replication**: Multi-region replication for availability

## Stack

### Primary Language & Runtime
- **Language**: Go 1.24+ (registry service), Rust (CLI)
- **Runtime**: Native with aggressive generics adoption
- **Architecture**: Microservices with shared storage backend

### Core Dependencies
```go
// Web Framework
github.com/gin-gonic/gin
github.com/go-chi/chi/v5

// Storage
github.com/aws/aws-sdk-go-v2/service/s3
github.com/minio/minio-go/v7
github.com/redis/go-redis/v9

// Database
github.com/jackc/pgx/v5
gorm.io/gorm

// Authentication
github.com/golang-jwt/jwt/v5
github.com/coreos/go-oidc/v3

// Package Formats
github.com/docker/distribution    // OCI registry
github.com/goreleaser/nfpm/v2     // Package building

// Utilities
github.com/spf13/cobra            # CLI
github.com/spf13/viper            # Config
go.uber.org/zap                   # Logging
```

### Registry Types Supported
- **Cargo**: Rust crate registry
- **npm**: JavaScript package registry
- **Go Module**: Go module proxy
- **PyPI**: Python package registry
- **OCI**: Docker/OCI image registry
- **Generic**: Arbitrary artifact storage

### Build & Development Tools
- **Task Runner**: Task (Taskfile.yml)
- **Linting**: golangci-lint
- **Testing**: gotestsum
- **Documentation**: OpenAPI + registry API docs

## Quick Start

### Prerequisites

```bash
# Go 1.24+
brew install go@1.24

# Task runner
brew install go-task/tap/go-task

# PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# Redis
brew install redis
brew services start redis
```

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd phenotype-registry

# Install dependencies
go mod download

# Build the project
task build

# Verify installation
registry --version
```

### Development Environment Setup

```bash
# Copy environment configuration
cp .env.example .env

# Initialize database
task db:init
task db:migrate

# Start development server
task dev
```

### Running the Registry

```bash
# Development mode
task dev

# Production build
task build:release

# Run production server
./bin/registry server
```

### Verification

```bash
# Run all tests
task test

# Check code quality
task lint
task format:check

# Health check
curl http://localhost:8080/health
```

## Architecture

### System Design

Phenotype-Registry implements a multi-format registry with pluggable backends:

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Applications                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │  Cargo   │ │   npm    │ │   Go     │ │   pip    │     │
│  │  Client  │ │  Client  │ │   get    │ │  Client  │     │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘     │
└───────┼────────────┼────────────┼────────────┼────────────┘
        │            │            │            │
        ▼            ▼            ▼            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Registry API Gateway                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Cargo      │  │    npm       │  │    Go        │     │
│  │   API        │  │    API       │  │    Proxy     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
├─────────────────────────────────────────────────────────────┤
│                    Core Services                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Package    │  │   Version    │  │   Download   │     │
│  │   Manager    │  │   Manager    │  │   Service    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
├─────────────────────────────────────────────────────────────┤
│                    Storage Layer                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Postgres │ │   S3     │ │  Redis   │ │  Search  │     │
│  │(Metadata)│ │(Packages)│ │ (Cache)  │ │(Elastic) │     │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Component Breakdown

#### 1. API Gateway
- **Format Adapters**: Protocol-specific endpoints
- **Authentication**: JWT, API keys, mTLS
- **Rate Limiting**: Per-user and per-package limits

#### 2. Core Services
- **Package Manager**: CRUD operations for packages
- **Version Manager**: Version metadata, yanking
- **Download Service**: Package serving with caching

#### 3. Storage Layer
- **PostgreSQL**: Package metadata, versions, dependencies
- **S3/MinIO**: Actual package files (tarballs, wheels)
- **Redis**: Hot package cache, download counters
- **Elasticsearch**: Package search index

### Package Lifecycle

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│ Publish │ → │ Validate│ → │ Store   │ → │ Index   │
│         │   │         │   │         │   │         │
└─────────┘   └─────────┘   └─────────┘   └─────────┘
      ↑                                        ↓
      └──────────── Yank/Unyank ←──────────────┘
```

### Supported Formats

```go
// Registry formats supported
type Format string

const (
    FormatCargo    Format = "cargo"    // Rust
    FormatNPM      Format = "npm"      // JavaScript
    FormatGo       Format = "go"       // Go modules
    FormatPyPI     Format = "pypi"     // Python
    FormatOCI      Format = "oci"      // Containers
    FormatGeneric  Format = "generic"  // Arbitrary
)

// Common package structure
type Package struct {
    Name        string
    Version     string
    Format      Format
    Description string
    Author      string
    License     string
    Dependencies []Dependency
    Files       []File
}
```

## Quality Standards

### Testing Requirements

#### Test Coverage
- **Minimum Coverage**: 80% for services, 70% for adapters
- **Critical Paths**: 95% for publish/download paths
- **Measurement**: `go test -coverprofile` with CI

#### Test Categories
```bash
# Unit tests
task test:unit

# Integration tests
task test:integration

# E2E tests with real clients
task test:e2e
```

### Code Quality

#### Go Standards
```bash
# Linting
golangci-lint run --config=.golangci.yml

# Formatting
go fmt ./...
gofumpt -l -w .
```

### Reliability Standards

| Metric | Target | Measurement |
|--------|--------|-------------|
| Uptime | 99.99% | API availability |
| Download latency | < 100ms p99 | Package download |
| Publish latency | < 5s | Package publish |
| Storage durability | 99.9999999% | Data durability |

## Git Workflow

### Branch Strategy

```
main
  │
  ├── feature/oci-support
  │   └── PR #45 → squash merge ──┐
  │                               │
  ├── feature/package-signing      │
  │   └── PR #46 → squash merge ──┤
  │                               │
  ├── fix/race-publish             │
  │   └── PR #47 → squash merge ──┤
  │                               │
  └── hotfix/security-patch ────────┘
      └── PR #48 → merge commit
```

### Branch Naming

```
feature/<scope>-<description>
fix/<component>-<issue>
perf/<optimization>
refactor/<scope>
docs/<topic>
chore/<maintenance>
hotfix/<critical>
```

### Commit Conventions

```
feat(oci): add OCI image registry support

Enables storing and distributing Docker images with
full OCI compliance. Includes manifest verification.

Closes #123

fix(storage): resolve race in concurrent uploads

Two simultaneous uploads of same version could corrupt
index. Now uses optimistic locking with ETags.
```

## File Structure

```
phenotype-registry/
├── cmd/
│   └── registry/              # CLI entry point
│       └── main.go
│
├── pkg/
│   ├── api/                   # HTTP handlers
│   │   ├── cargo.go
│   │   ├── npm.go
│   │   ├── go.go
│   │   └── pypi.go
│   ├── core/                  # Core services
│   │   ├── package.go
│   │   ├── version.go
│   │   └── download.go
│   ├── storage/               # Storage backends
│   │   ├── s3.go
│   │   ├── database.go
│   │   └── cache.go
│   ├── auth/                  # Authentication
│   │   ├── jwt.go
│   │   └── apikey.go
│   └── models/                # Data models
│       └── package.go
│
├── internal/                   # Internal packages
│   ├── config/
│   └── utils/
│
├── migrations/                 # Database migrations
│   └── *.sql
│
├── helm/                       # Helm charts
│   └── registry/
│
├── docs/
│   ├── api.md
│   └── formats.md
│
├── tests/
│   ├── integration/
│   └── e2e/
│
├── Taskfile.yml
├── go.mod
├── go.sum
├── README.md
├── CHANGELOG.md
└── AGENTS.md                   # This file
```

## CLI

### Core Commands

```bash
# Server Operations
registry server                # Start server
registry server --config ./config.yaml

# Package Management
registry package list          # List packages
registry package info <name>   # Show package info
registry package yank <name> <version>  # Yank version
registry package unyank <name> <version>

# User Management
registry user create <username>  # Create user
registry user token <username>   # Generate token
registry user revoke <username>  # Revoke tokens

# Maintenance
registry db migrate            # Run migrations
registry db rollback           # Rollback migration
registry cache clear           # Clear caches
registry index rebuild         # Rebuild search index

# Diagnostics
registry doctor                # Health check
registry status                # Server status
registry metrics               # Show metrics
```

### Configuration

```yaml
# config.yaml
server:
  port: 8080
  tls:
    enabled: true
    cert: /etc/certs/server.crt
    key: /etc/certs/server.key

database:
  type: postgres
  url: postgres://localhost/registry
  max_connections: 50

storage:
  type: s3
  bucket: phenotype-registry
  region: us-east-1

cache:
  type: redis
  url: redis://localhost:6379

formats:
  - cargo
  - npm
  - go
  - pypi
  - oci

auth:
  jwt:
    secret: ${JWT_SECRET}
    expiry: 24h
```

## Troubleshooting

### Common Issues

#### Issue: Package publish failing with 409

**Symptoms:**
```
Error: 409 Conflict - version already exists
```

**Resolution:**
```bash
# Check if version exists
registry package info my-package --version 1.0.0

# Yank and republish (if needed)
registry package yank my-package 1.0.0
# Update version in package
registry publish

# Or use force flag (owner only)
registry publish --force
```

---

#### Issue: High storage costs

**Diagnosis:**
```bash
# Check storage usage
registry metrics | grep storage

# List large packages
registry package list --sort=size --limit=50
```

**Resolution:**
```bash
# Enable lifecycle policies
registry config set storage.lifecycle.enabled true

# Clean old versions
registry package prune --older-than 1y --keep-versions 5
```

---

#### Issue: Search returning no results

**Diagnosis:**
```bash
# Check search index
registry index status

# Verify Elasticsearch
curl http://localhost:9200/_cluster/health
```

**Resolution:**
```bash
# Rebuild index
registry index rebuild

# Check for indexing errors
registry logs --component indexer
```

---

#### Issue: Slow package downloads

**Diagnosis:**
```bash
# Check cache hit rate
registry metrics | grep cache_hit

# Verify CDN status
```

**Resolution:**
```bash
# Warm cache
registry cache warm --popular

# Increase cache TTL
registry config set cache.ttl 24h
```

---

### Debug Mode

```bash
# Enable debug logging
export REGISTRY_LOG_LEVEL=debug

# Verbose output
registry publish --verbose

# API debugging
curl -v http://localhost:8080/api/v1/packages
```

### Recovery Procedures

```bash
# Recover from backup
registry db restore --from s3://backups/registry-$(date +%Y%m%d).sql

# Verify package integrity
registry package verify --all

# Rebuild from S3
registry index rebuild-from-storage
```

---

## Agent Self-Correction & Verification Protocols

### Critical Rules

1. **Immutability**
   - Published packages are immutable
   - Yank instead of delete
   - Audit all changes

2. **Security**
   - All packages scanned
   - Signed packages verified
   - Access controlled

3. **Availability**
   - Multi-region replication
   - Automatic failover
   - Graceful degradation

4. **AgilePlus Integration**
   - Reference registry specs
   - Update for new package formats

---

*This AGENTS.md is a living document. Update it as phenotype-registry evolves.*
