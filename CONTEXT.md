# CONTEXT.md — ai-project-templates

## What This Repo Does

Python-based project scaffolder for the Agentic Engineering OS.
One command generates a complete project with governance (CLAUDE.md), project management (backlog/), and engineering standards (.engineering/) baked in.

## Current State

- **Version:** 1.0.0
- **Status:** Stable, ready for public use
- **Stacks:** python-data, python-web, docs-only, databricks-lakehouse
- **Modes:** solo, team
- **Tests:** 32+ pytest tests covering all stacks and features
- **CI:** GitHub Actions with lint, test, and scaffold-all-stacks validation

## Architecture

```
scaffold.py              Main CLI — reads config, renders templates, creates project
configs/                 Stack-specific YAML configs (directories, extra_files, conventions)
templates/               .tmpl files with {{variable}} placeholders
templates/.github/       CI workflow templates per stack type
tests/                   pytest test suite
docs/                    Usage and customization guides
examples/                Pre-generated scaffold output for reference
backlog/                 Legacy task files (migrated to GitHub Issues)
```

### How Scaffolding Works

1. `parse_args()` reads CLI arguments (--name, --stack, --mode, --output-dir, --dry-run)
2. `load_config()` reads the stack YAML from configs/
3. `create_project()` collects directories and files, then either prints (dry-run) or writes them
4. Templates are rendered by replacing `{{key}}` with context values — no Jinja2
5. AGENTS.md symlink to CLAUDE.md is created for multi-agent compatibility

### Key Files

| File | Purpose |
|------|---------|
| `scaffold.py` | Main entry point (~260 lines) |
| `configs/python-data.yaml` | Medallion architecture: bronze/silver/gold |
| `configs/python-web.yaml` | API/web app: api/models/services |
| `configs/docs-only.yaml` | Documentation-only projects |
| `configs/databricks-lakehouse.yaml` | Databricks: notebooks, DLT, Unity Catalog |
| `templates/CLAUDE.md.tmpl` | Governance template for scaffolded projects |

## Dependencies

- **Runtime:** Python 3.11+, PyYAML
- **Dev:** pytest, ruff
- **No Jinja2** — templates use simple string replacement

## Conventions

- All content in English
- `kebab-case` for file/directory names
- `snake_case` for Python variables and functions
- Templates use `.tmpl` extension with `{{variable}}` placeholders
- Configs use YAML format
