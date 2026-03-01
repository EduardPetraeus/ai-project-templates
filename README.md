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
```

## Generated Output

```
<project-name>/
├── CLAUDE.md              # AI agent governance
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

## Mode Options

| Mode | Description |
|------|------------|
| `solo` | Single developer workflow |
| `team` | Multi-developer workflow with task assignment |

## Dependencies

- Python 3.11+
- PyYAML (`pip install pyyaml`)

No Jinja2 required. Templates use simple `{{variable}}` placeholders with `str.replace`.

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
