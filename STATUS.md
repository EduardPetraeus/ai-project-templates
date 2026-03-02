# STATUS.md — Workstream 4 (V2 Features)

**Branch:** `feature/v2`
**Date:** 2026-03-02
**Status:** Complete

## What Was Done

### Task 1: Input Validation for Project Names
- Added `validate_project_name()` with regex pattern `^[a-z0-9][a-z0-9-]*$`
- Validation runs in both `create_project()` and `main()` for clear error messages
- Invalid names (spaces, uppercase, underscores, special chars) produce helpful errors with examples

### Task 2: Template Escaping for Literal Braces
- `\{\{` renders as literal `{{` in output; `\}\}` renders as `}}`
- Uses sentinel-based escaping in `render_template()` to avoid conflicts with placeholder substitution
- Enables scaffolding projects that use Jinja2 or similar templating engines

### Task 3: Windows Symlink Fallback
- `AGENTS.md` symlink creation is wrapped in try/except
- On `OSError` (common on Windows without admin), falls back to `shutil.copy2()`
- Prints informative note when fallback is used

### Task 4: Example Scaffolds (4 Complete)
- `examples/python-cli-example` — CLI tool with argument parsing, tests
- `examples/python-web-example` — Web API with models, services, routes, tests
- `examples/docs-only-example` — Documentation repository with guides and conventions
- `examples/data-pipeline-example` — Medallion architecture (bronze/silver/gold) with realistic code and tests

### Task 5: Meaningful Template Content
- `ARCHITECTURE.md.tmpl` — Full starter content with system diagram placeholder, component table, data flow guidance, deployment section, security considerations
- `CONTEXT.md.tmpl` — Structured living context with active work table, pending actions, decisions, tech debt, key contacts

### Task 6: Tests (59 total, all passing)
- 14 tests for project name validation (valid and invalid names)
- 5 tests for template escaping (escaped, normal, mixed, missing template)
- 3 tests for Windows symlink fallback (mock OSError, verify copy, verify normal symlink)
- Plus all 37 existing tests retained and passing

### Task 7: README Updated
- Documented validation rules with examples
- Documented escaping syntax with table
- Documented Windows support
- Added examples section
- Added AGENTS.md to generated output tree
- Updated dependencies to Python 3.9+

## Verification

- `ruff check .` — all checks passed
- `ruff format --check .` — all files formatted
- `pytest tests/ -v` — 59/59 passed
