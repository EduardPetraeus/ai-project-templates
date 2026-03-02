# ARCHITECTURE.md — python-web-example

Created: 2026-03-02
Stack: python-web

## Overview

This document describes the high-level architecture of **python-web-example**.
It is the single source of truth for how the system is structured, what the
main components are, and how data flows between them. Keep it up to date as
the project evolves.

## System Diagram

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Input /   │───>│  Processing  │───>│   Output /  │
│   Ingestion │    │   (Core)     │    │   Serving   │
└─────────────┘    └──────────────┘    └─────────────┘
```

Replace this placeholder with an actual diagram of your system.
Use Mermaid, ASCII art, or link to an image.

## Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Core logic | `src/` | Main business logic and data transformations |
| Tests | `tests/` | Unit and integration tests |
| Configuration | `.engineering/` | Linter, formatter, and project settings |
| Documentation | `docs/` | ADRs, guides, and API docs |

> Add rows as you create new modules. Each component should have a clear
> single responsibility.

## Data Flow

Describe how data enters the system, how it is transformed, and where the
results go. For data engineering projects, this typically follows a medallion
pattern (bronze -> silver -> gold). For web projects, describe the request
lifecycle.

1. **Input:** Where data comes from (API, files, database, message queue)
2. **Processing:** What transformations or business logic are applied
3. **Output:** Where results are stored or served (database, API response, files)

## Key Decisions

All significant architectural decisions should be recorded as ADRs in
`docs/adr/`. Use the template at `docs/adr/ADR-000-template.md`.

| Decision | ADR | Status | Date |
|----------|-----|--------|------|
| Initial architecture | ADR-001 | Proposed | 2026-03-02 |

## Dependencies

List your key dependencies and the rationale for choosing them. This helps
future contributors understand why specific libraries were selected.

| Dependency | Version | Purpose | Alternatives Considered |
|------------|---------|---------|------------------------|
| Python | >=3.11 | Runtime | — |

## Deployment

Describe how this project is built, tested, and deployed:

1. **Local development:** How to run locally (see README.md)
2. **CI/CD:** GitHub Actions runs lint + tests on every push (see `.github/workflows/ci.yml`)
3. **Production:** Describe your deployment target and process

## Security Considerations

- No secrets in code — use environment variables or a secrets manager
- All inputs validated before processing
- Dependencies pinned to specific versions
- See CLAUDE.md `security_protocol` for agent-specific rules
