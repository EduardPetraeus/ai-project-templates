# ai-project-templates

Scaffold new projects with governance, project management, and engineering standards in one command.

## What This Does

`scaffold.py` generates a complete project structure with:

- **CLAUDE.md** — AI agent governance rules (from [ai-governance-framework](https://github.com/EduardPetraeus/ai-governance-framework))
- **Backlog + commands** — YAML task engine (from [ai-project-management](https://github.com/EduardPetraeus/ai-project-management))
- **Engineering config** — Ruff, pytest, conventions (from [ai-engineering-standards](https://github.com/EduardPetraeus/ai-engineering-standards))
- **Architecture docs** — ADR templates, CONTEXT.md, ARCHITECTURE.md

## Quick Start

```bash
pip install pyyaml

# Scaffold a Python data engineering project
python scaffold.py --name my-project --stack python-data --mode solo

# Scaffold a Python web project
python scaffold.py --name my-api --stack python-web --mode team

# Scaffold a docs-only project
python scaffold.py --name my-docs --stack docs-only --mode solo

# Scaffold into a specific directory
python scaffold.py --name my-project --stack python-data --mode solo --output-dir ~/projects

# Dry run — preview what would be created
python scaffold.py --name my-project --stack python-data --mode solo --dry-run
```

## Generated Output

```
<project-name>/
├── CLAUDE.md              # AI agent governance
├── AGENTS.md              # Symlink to CLAUDE.md (copy on Windows)
├── CONTEXT.md             # Living project context
├── ARCHITECTURE.md        # Architecture documentation
├── README.md              # Project README
├── .gitignore
├── backlog/
│   └── TASK-001.yaml      # First task
├── .claude/
│   └── commands/
│       ├── pick-next-task.md
│       ├── complete-task.md
│       └── create-task.md
├── .engineering/
│   ├── ruff.toml
│   └── pyproject.toml
├── .github/
│   └── workflows/
│       └── ci.yml         # CI pipeline (lint + test)
└── docs/
    └── adr/
        └── ADR-000-template.md
```

## Stack Options

| Stack | Description | Extra Directories |
|-------|------------|-------------------|
| `python-data` | Data engineering with medallion architecture | `src/bronze/`, `src/silver/`, `src/gold/`, `tests/` |
| `python-web` | Web application (API + services) | `src/api/`, `src/models/`, `src/services/`, `static/`, `tests/` |
| `docs-only` | Documentation-only repository | `docs/` |
| `databricks-lakehouse` | Databricks with medallion + DLT | `notebooks/bronze/`, `notebooks/silver/`, `notebooks/gold/`, `notebooks/dlt/` |

## Mode Options

| Mode | Description |
|------|------------|
| `solo` | Single developer workflow |
| `team` | Multi-developer workflow with task assignment |

## Project Name Validation

Project names must follow these rules:

- Lowercase letters (`a-z`), digits (`0-9`), and hyphens (`-`) only
- Must start with a letter or digit (not a hyphen)
- No spaces, underscores, or uppercase letters

```bash
# Valid names
python scaffold.py --name my-project ...     # OK
python scaffold.py --name api-v2 ...         # OK
python scaffold.py --name data-pipeline-01 ...  # OK

# Invalid names — clear error message
python scaffold.py --name "foo bar" ...      # ERROR: spaces not allowed
python scaffold.py --name "MyProject" ...    # ERROR: uppercase not allowed
python scaffold.py --name "my_project" ...   # ERROR: underscores not allowed
```

## Template Escaping

Templates use `{{variable}}` for placeholder substitution. If your project needs literal `{{` and `}}` in output files (e.g., for Jinja2 templates), use the escape syntax:

| In template | Rendered output |
|-------------|----------------|
| `{{project_name}}` | `my-project` (substituted) |
| `\{\{` | `{{` (literal) |
| `\}\}` | `}}` (literal) |

This lets you scaffold projects that use Jinja2, Handlebars, or similar templating engines without conflicts.

## Windows Support

On Windows, `AGENTS.md` is normally created as a symlink to `CLAUDE.md`. If symlink creation fails (common without admin privileges), the scaffolder automatically falls back to creating `AGENTS.md` as a copy of `CLAUDE.md`.

## Dependencies

- Python 3.9+
- PyYAML (`pip install pyyaml`)

No Jinja2 required. Templates use simple `{{variable}}` placeholders with `str.replace`.

## Examples

The `examples/` directory contains 4 complete scaffolds for reference:

| Example | Stack | Description |
|---------|-------|-------------|
| `python-cli-example` | python-data | CLI tool with argument parsing and tests |
| `python-web-example` | python-web | Web API with models, services, and tests |
| `docs-only-example` | docs-only | Documentation repository with guides |
| `data-pipeline-example` | python-data | Data pipeline with bronze/silver/gold layers |

## Part of the Agentic Engineering OS

| Repo | Purpose |
|------|---------|
| [ai-governance-framework](https://github.com/EduardPetraeus/ai-governance-framework) | Governance layer for AI-assisted development |
| [ai-project-management](https://github.com/EduardPetraeus/ai-project-management) | YAML-based task engine |
| [ai-engineering-standards](https://github.com/EduardPetraeus/ai-engineering-standards) | Code conventions and standards |
| [ai-project-templates](https://github.com/EduardPetraeus/ai-project-templates) | Project scaffolder (this repo) |
| [agentic-engineering](https://github.com/EduardPetraeus/agentic-engineering) | Umbrella documentation |

## Documentation

- [Usage Guide](docs/USAGE.md) — detailed usage instructions with all flag combinations
- [Customization Guide](docs/CUSTOMIZATION.md) — how to add stacks and modify templates

## License

MIT
