# CLAUDE.md — ai-project-templates

This file governs all AI agent sessions in this repository.

## project_context

- **Repo:** ai-project-templates
- **Purpose:** Python-based project scaffolder for the Agentic Engineering OS
- **License:** MIT
- **Status:** Active development (v0.2.0)
- **Design principle:** One command generates a complete project with governance, PM, and engineering standards baked in
- **Dependencies:** Python 3.11+ and PyYAML (only external dependency)

## conventions

- All content in English — no exceptions
- File names: `kebab-case` for directories and files
- Python code: `snake_case` for variables and functions, `PascalCase` for classes
- Templates use `{{variable}}` placeholders (`.tmpl` extension) — no Jinja2
- Config files use YAML
- Keep scaffold.py simple — stdlib + pathlib + PyYAML only

## architecture

```
scaffold.py        → Main entry point — reads config, substitutes templates, creates project
templates/         → .tmpl templates with {{variable}} placeholders
configs/           → Stack-specific YAML configs (python-data, python-web, docs-only)
tests/             → pytest test suite
docs/              → Usage and customization guides
```

## session_protocol

1. Read this CLAUDE.md
2. Confirm scope: which templates, configs, or scaffolder logic to work on
3. After changes: run `python -m pytest tests/` to verify
4. Verify generated output matches expected structure

## security_protocol

- Never commit secrets, credentials, or `.env` files
- scaffold.py must refuse to overwrite existing directories
- Output directory must be validated before writing

## quality_standards

- scaffold.py must work with only PyYAML as external dependency
- All templates must render without errors given valid config
- Generated projects must include governance (CLAUDE.md), PM (backlog/), and standards (.engineering/)
- Tests must cover: directory creation, template rendering, error handling
- Keep scaffold.py under 300 lines

## kill_switch

If scaffold.py produces incorrect output or overwrites existing files:
1. Stop immediately
2. Do not run scaffold.py again until the issue is diagnosed
3. Check the --output-dir flag and ensure it points to a safe location

## framework_references

- Governance: ~/Github repos/ai-governance-framework
- Project Management: ~/Github repos/ai-project-management
- Engineering Standards: ~/Github repos/ai-engineering-standards
- Templates: ~/Github repos/ai-project-templates (this repo)
- Umbrella: ~/Github repos/agentic-engineering
