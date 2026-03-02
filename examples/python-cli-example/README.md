# python-cli-example

Python data engineering project (medallion architecture)

## Quick Start

```bash
# Clone the repository
git clone <repo-url>
cd python-cli-example

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Development

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt

# Run linter
ruff check src/

# Run tests
pytest tests/ -v
```

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

## Project Structure

```
python-cli-example/
├── CLAUDE.md          # AI agent governance
├── CONTEXT.md         # Living project context
├── ARCHITECTURE.md    # Architecture documentation
├── backlog/           # YAML task files
├── .claude/commands/  # AI agent commands
├── .engineering/      # Code standards (ruff, pyproject)
└── docs/adr/          # Architecture Decision Records
```

## License

MIT
