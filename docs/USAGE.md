# Usage Guide

## Prerequisites

Install the only external dependency:

```bash
pip install pyyaml
```

No Jinja2 required. Templates use simple `{{variable}}` substitution.

## Basic Usage

```bash
python scaffold.py --name <project-name> --stack <stack> --mode <mode>
```

### Required Arguments

| Argument | Description | Options |
|----------|------------|---------|
| `--name` | Project name (used as directory name) | Any valid directory name |
| `--stack` | Stack type | `python-data`, `python-web`, `docs-only` |
| `--mode` | Working mode | `solo`, `team` |

### Optional Arguments

| Argument | Description | Default |
|----------|------------|---------|
| `--output-dir` | Parent directory for the project | Current directory (`.`) |

## All Flag Combinations

### Python Data + Solo

```bash
python scaffold.py --name my-data-project --stack python-data --mode solo
```

Generated extra directories: `src/bronze/`, `src/silver/`, `src/gold/`, `tests/`
Extra files: `requirements.txt`
Conventions: `snake_case`, SQL prefix enabled, medallion architecture

### Python Data + Team

```bash
python scaffold.py --name my-data-project --stack python-data --mode team
```

Same structure as solo. Mode is recorded in CLAUDE.md and CONTEXT.md for agent behavior.

### Python Web + Solo

```bash
python scaffold.py --name my-api --stack python-web --mode solo
```

Generated extra directories: `src/api/`, `src/models/`, `src/services/`, `static/`, `tests/`
Extra files: `requirements.txt`
Conventions: `snake_case`

### Python Web + Team

```bash
python scaffold.py --name my-api --stack python-web --mode team
```

Same structure as solo. Mode affects task assignment behavior in PM commands.

### Docs Only + Solo

```bash
python scaffold.py --name my-docs --stack docs-only --mode solo
```

Minimal structure: `docs/`, `docs/adr/`, `backlog/`, `.claude/commands/`
No `src/`, `tests/`, or `.engineering/` directories from config (though `.engineering/` is always created as a core directory).
No extra files.
Conventions: `kebab-case`

### Docs Only + Team

```bash
python scaffold.py --name my-docs --stack docs-only --mode team
```

Same as docs-only solo, with team mode recorded in context files.

## Custom Output Directory

```bash
# Scaffold into a specific directory (created if it does not exist)
python scaffold.py --name my-project --stack python-data --mode solo --output-dir ~/projects

# Scaffold into a nested path
python scaffold.py --name my-project --stack python-web --mode team --output-dir ~/work/2026/projects
```

## Generated Structure

Every scaffolded project includes these core files regardless of stack:

```
<project-name>/
├── CLAUDE.md              # AI agent governance rules
├── CONTEXT.md             # Living project context
├── ARCHITECTURE.md        # Architecture documentation
├── README.md              # Project README
├── .gitignore             # Git ignore rules
├── backlog/
│   └── TASK-001.yaml      # First task (set up project infrastructure)
├── .claude/
│   └── commands/
│       ├── pick-next-task.md   # Find and claim next task
│       ├── complete-task.md    # Mark task as done
│       └── create-task.md      # Create a new task
├── .engineering/
│   ├── ruff.toml          # Ruff linter config
│   └── pyproject.toml     # Python project config (pytest, mypy, black)
└── docs/
    └── adr/
        └── ADR-000-template.md  # Architecture Decision Record template
```

Stack-specific directories and files are added on top of this core structure.

## After Scaffolding

```bash
cd <project-name>
git init
git add -A
git commit -m "Initial scaffold from ai-project-templates"
```

Then start working:

1. Read `CLAUDE.md` for governance rules
2. Run `/pick-next-task` to claim TASK-001
3. Build your project
4. Run `/complete-task` when done
5. Run `/create-task` to add new tasks
