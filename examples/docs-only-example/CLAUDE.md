# CLAUDE.md — docs-only-example

This file governs all AI agent sessions in this repository.

## project_context

- **Repo:** docs-only-example
- **Purpose:** Documentation-only repository
- **Created:** 2026-03-02
- **Stack:** docs-only
- **Mode:** solo

## conventions

- All content in English — no exceptions
- Python: `snake_case` for variables and functions, `PascalCase` for classes
- File names: `kebab-case`
- YAML for configuration, Markdown for documentation

## session_protocol

1. Read this CLAUDE.md before starting work
2. Check `backlog/` for current tasks — run `/pick-next-task`
3. Work in feature branches — never commit directly to main
4. After changes: run tests, verify output
5. Complete task — run `/complete-task`
6. At session end: evaluate if CONTEXT.md needs updating

## security_protocol

- Never commit secrets, credentials, or `.env` files
- Validate all inputs before processing
- No hardcoded passwords or API keys
- Use environment variables for sensitive configuration

## quality_standards

- All code must have tests
- All YAML must be valid
- All cross-references must resolve
- No secrets in committed files
- Code must pass ruff linting (see `.engineering/ruff.toml`)

## kill_switch

If any of the following occur, STOP immediately:
- Tests fail after a change and the cause is unclear
- A file outside the project directory would be modified
- Credentials or secrets are about to be committed
- The agent is looping without progress (3+ attempts at same task)

Do not proceed until the issue is diagnosed and resolved with the developer.

## framework_references

- Governance: https://github.com/EduardPetraeus/ai-governance-framework
- Project Management: https://github.com/EduardPetraeus/ai-project-management
- Engineering Standards: https://github.com/EduardPetraeus/ai-engineering-standards

## agents

AGENTS.md is a symlink to this file for multi-agent compatibility.
