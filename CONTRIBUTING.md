# Contributing to ai-project-templates

Thank you for your interest in contributing. This guide explains how to add stacks, modify templates, and submit changes.

## Quick Start

```bash
git clone https://github.com/EduardPetraeus/ai-project-templates.git
cd ai-project-templates
pip install pyyaml pytest ruff
python -m pytest tests/ -v
```

## Adding a New Stack

1. **Create a config file** in `configs/` named `your-stack.yaml`:

```yaml
stack: your-stack
description: "Brief description of the stack"

directories:
  - src/
  - tests/

extra_files:
  - requirements.txt

conventions:
  naming: snake_case
```

2. **Add the stack** to `VALID_STACKS` in `scaffold.py`.

3. **Choose a CI template** — map the stack to an existing CI template in the `ci_template_map` dict in `create_project()`, or create a new template under `templates/.github/workflows/`.

4. **Add tests** in `tests/test_scaffold.py`:
   - Directory creation test
   - Extra files test
   - Config loading test
   - Template substitution test

5. **Test it end-to-end**:

```bash
python scaffold.py --name test-stack --stack your-stack --mode solo --output-dir /tmp/test
python scaffold.py --dry-run --name test-stack --stack your-stack --mode solo
```

## Modifying Templates

Templates live in `templates/` with `.tmpl` extension. They use `{{variable}}` placeholders:

| Variable | Description |
|----------|------------|
| `{{project_name}}` | Project name from --name |
| `{{date}}` | Scaffold date (YYYY-MM-DD) |
| `{{stack}}` | Stack type |
| `{{mode}}` | Working mode (solo/team) |
| `{{description}}` | Stack description from config |

No Jinja2 — just simple string replacement. Keep it that way.

## Pull Request Process

1. Fork the repo and create a feature branch from `main`
2. Make your changes
3. Run all checks:
   ```bash
   ruff check scaffold.py tests/
   ruff format --check scaffold.py tests/
   python -m pytest tests/ -v
   ```
4. Add or update tests for your changes
5. Submit a pull request with a clear description

## Code Style

- Python: Follow ruff defaults (see `.engineering/` for config)
- All content in English — code, comments, docs, everything
- Keep `scaffold.py` under 300 lines
- Only dependency: PyYAML (no Jinja2, no Click, no Rich)

## Reporting Issues

Use GitHub Issues. Include:
- What you expected
- What happened instead
- Steps to reproduce
- Stack and mode used

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
