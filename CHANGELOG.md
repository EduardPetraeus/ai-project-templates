# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/).

## [1.0.0] - 2026-03-01

### Added
- `--dry-run` flag for previewing scaffold output without writing files
- AGENTS.md symlink to CLAUDE.md in all scaffolded projects (multi-agent compatibility)
- `agents` section in CLAUDE.md template documenting the symlink
- GitHub Actions CI workflow for the repo itself (lint, test, scaffold-all-stacks)
- Pre-generated examples in `examples/` for python-data and databricks-lakehouse stacks
- CONTEXT.md with repo architecture and current state
- CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md for open source readiness
- AGENTS.md symlink at repo root

### Changed
- Refactored `create_project()` to collect files/dirs before writing (enables dry-run)
- Migrated backlog YAML tasks to GitHub Issues

### Fixed
- 3 ruff F541 errors (f-strings without placeholders in print statements)

## [0.2.0] - 2026-03-01

### Added
- databricks-lakehouse stack config with notebook structure, DLT, Unity Catalog conventions
- GitHub Actions CI templates (ci-python.yml.tmpl, ci-docs.yml.tmpl) for scaffolded projects
- CI template selection based on stack type
- Tests for databricks stack and CI template generation
- CUSTOMIZATION.md documentation

## [0.1.0] - 2026-03-01

### Added
- Initial scaffolder with python-data, python-web, docs-only stacks
- Template rendering with {{variable}} placeholder substitution
- Stack-specific YAML configs for directories, extra files, and conventions
- Core file generation: CLAUDE.md, CONTEXT.md, ARCHITECTURE.md, README.md, .gitignore
- Project management files: backlog/TASK-001.yaml, .claude/commands/
- Engineering standards: .engineering/ruff.toml, .engineering/pyproject.toml
- ADR template: docs/adr/ADR-000-template.md
- pytest test suite with 28 tests
- USAGE.md documentation
