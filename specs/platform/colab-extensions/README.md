# Colab Extensions (migrated)

Governance specs migrated from archived `KooshaPari/phenotype-colab-extensions` (2026-06-16). Source repo deleted after absorption.

## Runtime implementation

| Home | Path | Purpose |
|------|------|---------|
| [HeliosLab](https://github.com/KooshaPari/HeliosLab) | [`webflow-plugin/`](https://github.com/KooshaPari/HeliosLab/tree/main/webflow-plugin) | Webflow DevLink / Cloud / Assets plugin + `wf` CLI |
| [HeliosLab](https://github.com/KooshaPari/HeliosLab) | [`agileplus-specs/`](https://github.com/KooshaPari/HeliosLab/tree/main/agileplus-specs) | AgilePlus-aligned colab integration specs |

## Spec documents (this folder)

| File | Description |
|------|-------------|
| [PRD.md](./PRD.md) | Product requirements for colab extensions |
| [FUNCTIONAL_REQUIREMENTS.md](./FUNCTIONAL_REQUIREMENTS.md) | Traceable FR IDs (intent; see FR drift notes) |
| [ADR.md](./ADR.md) | Architecture decisions incl. migration ADR-004 |
| [SECURITY_AUDIT.md](./SECURITY_AUDIT.md) | Data-handling audit + HeliosLab reconciliation |
| [UPSTREAM_SYNC.md](./UPSTREAM_SYNC.md) | Historical upstream sync strategy for `KooshaPari/colab` |

## FR drift (spec vs HeliosLab)

Original FRs reference `src/webflow-plugin/` and `.webflow/config.json`. HeliosLab uses:

- `.webflowrc.json` — DevLink project config
- `wf` terminal CLI — `webflow-plugin/src/commands/wf.ts`
- Plugin settings storage — `webflow-plugin/src/storage/manager.ts`

See [SECURITY_AUDIT.md](./SECURITY_AUDIT.md#migration-reconciliation--fr-drift-vs-helioslab-2026-06-16) and [ADR-004](./ADR.md#adr-004--specs-to-phenospecs-runtime-to-helioslab-2026-06-16).
