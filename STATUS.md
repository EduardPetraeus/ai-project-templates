# Status

Last updated: 2026-03-01

## Completed

### TASK-001: Databricks-lakehouse stack config
- Added `configs/databricks-lakehouse.yaml` with notebooks structure, DLT, Unity Catalog conventions
- Updated `VALID_STACKS` in `scaffold.py` to include `databricks-lakehouse`
- Added 5 tests in `TestDatabricksLakehouseStack` (directories, extra files, config loading, core files, template substitution)

### TASK-002: GitHub Actions CI templates
- Created `templates/.github/workflows/ci-python.yml.tmpl` (ruff lint + pytest)
- Created `templates/.github/workflows/ci-docs.yml.tmpl` (markdownlint)
- Added CI template selection logic in `scaffold.py` — maps stack type to CI template
- Added 4 tests in `TestCITemplateSelection` (python-data, docs-only, no placeholders, databricks)

## Test Summary
- 28 tests across 7 test classes — all passing
- scaffold.py: 241 lines (under 300-line limit)

## Supported Stacks
| Stack | CI Template | Description |
|---|---|---|
| python-data | ci-python.yml | Medallion architecture data project |
| python-web | ci-python.yml | Python web service |
| docs-only | ci-docs.yml | Documentation-only repo |
| databricks-lakehouse | ci-python.yml | Databricks lakehouse with DLT |
