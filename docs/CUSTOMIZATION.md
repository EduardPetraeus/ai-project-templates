# Customization Guide

## Adding a New Stack

### 1. Create the config YAML

Create a new file in `configs/`:

```yaml
# configs/my-stack.yaml
stack: my-stack
description: "Description of this stack type"
directories:
  - src/core
  - src/utils
  - tests
  - docs/adr
  - backlog
  - .claude/commands
  - .engineering
extra_files:
  - requirements.txt
conventions:
  naming: snake_case
  sql_prefix: false
  medallion: false
```

**Required fields:**
- `stack` — must match the filename (without `.yaml`)
- `description` — used in generated CLAUDE.md, CONTEXT.md, README.md
- `directories` — list of directories to create
- `extra_files` — list of empty files to create (e.g., `requirements.txt`)
- `conventions` — dict of project conventions (informational, included in context)

### 2. Register the stack

Update `VALID_STACKS` in `scaffold.py`:

```python
VALID_STACKS = ["python-data", "python-web", "docs-only", "my-stack"]
```

### 3. Test it

```bash
python scaffold.py --name test-my-stack --stack my-stack --mode solo --output-dir /tmp
```

Verify the output structure matches expectations.

## Modifying Templates

Templates are in `templates/` and use `{{variable}}` placeholder syntax.

### Available Placeholders

| Placeholder | Source | Example Value |
|-------------|--------|---------------|
| `{{project_name}}` | `--name` argument | `my-project` |
| `{{date}}` | Auto-generated (ISO format) | `2026-03-01` |
| `{{stack}}` | `--stack` argument | `python-data` |
| `{{mode}}` | `--mode` argument | `solo` |
| `{{description}}` | From config YAML `description` field | `Python data engineering project` |

### How substitution works

The scaffolder uses simple `str.replace()` — no template engine required:

```python
content = template.read_text()
for key, value in context.items():
    content = content.replace("{{" + key + "}}", str(value))
```

This means:
- No conditional logic in templates (unlike Jinja2)
- No loops or filters
- Just direct text replacement
- If a placeholder is not in the context, it remains as-is

### Adding a new template file

1. Create the `.tmpl` file in `templates/`:

```
templates/my-file.md.tmpl
```

2. Add the mapping in `scaffold.py` in the `template_mappings` dict:

```python
template_mappings = {
    # ... existing mappings ...
    "my-file.md.tmpl": "my-file.md",          # root-level file
    "my-file.md.tmpl": "subdir/my-file.md",   # nested file
}
```

3. The parent directory is created automatically.

## Modifying Core Files

### PM Commands

The PM commands (`pick-next-task.md`, `complete-task.md`, `create-task.md`) are template files in `templates/`. Edit the `.tmpl` files directly.

These commands do not use any `{{variable}}` placeholders — they are static content copied as-is.

### Engineering Config

The ruff and pyproject config files are templates too:
- `templates/ruff.toml.tmpl` — Ruff linter settings
- `templates/pyproject.toml.tmpl` — pytest, mypy, black settings

The `pyproject.toml.tmpl` uses `{{project_name}}` for the package name.

### ADR Template

Edit `templates/ADR-000-template.md.tmpl` to change the default ADR structure. It uses `{{date}}` for the creation date.

### Gitignore

Edit `templates/gitignore.tmpl` to change what gets ignored. This is a static template with no placeholders.

## Adding New Placeholders

To add a new placeholder available in all templates:

1. Add it to the `context` dict in `create_project()`:

```python
context = {
    "project_name": name,
    "date": date.today().isoformat(),
    "stack": stack,
    "mode": mode,
    "description": config.get("description", ""),
    "my_new_var": "my value",  # add here
}
```

2. Use `{{my_new_var}}` in any `.tmpl` file.

## Testing Changes

After making changes, run the test suite:

```bash
pip install pytest pyyaml
pytest tests/ -v
```

All tests should pass. If adding a new stack, add corresponding test cases in `tests/test_scaffold.py`.
