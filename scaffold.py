#!/usr/bin/env python3
"""
scaffold.py — Project scaffolder for the Agentic Engineering OS.

Generates a complete project structure with governance, project management,
and engineering standards from a single command.

Dependencies: PyYAML (only external dependency). No Jinja2 required.

Usage:
    python scaffold.py --name my-project --stack python-data --mode solo
    python scaffold.py --name my-project --stack python-web --mode team --output-dir ~/projects
    python scaffold.py --name my-docs --stack docs-only --mode solo
"""

import argparse
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPT_DIR / "templates"
CONFIGS_DIR = SCRIPT_DIR / "configs"

VALID_STACKS = ["python-data", "python-web", "docs-only", "databricks-lakehouse"]
VALID_MODES = ["solo", "team"]


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


def load_config(stack: str) -> dict:
    """Load stack configuration from YAML file."""
    config_path = CONFIGS_DIR / f"{stack}.yaml"
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config not found: {config_path}\nValid stacks: {', '.join(VALID_STACKS)}"
        )
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------


def render_template(template_path: Path, context: dict) -> str:
    """Render a .tmpl template by replacing {{key}} placeholders with values."""
    if not template_path.exists():
        print(f"WARNING: Template not found: {template_path}, skipping.")
        return ""
    content = template_path.read_text()
    for key, value in context.items():
        content = content.replace("{{" + key + "}}", str(value))
    return content


# ---------------------------------------------------------------------------
# Project creation
# ---------------------------------------------------------------------------


def create_project(
    name: str, stack: str, mode: str, output_dir: Path, dry_run: bool = False
) -> Path:
    """Create the full project structure.

    Args:
        name: Project name (used as directory name).
        stack: Stack type (python-data, python-web, docs-only, databricks-lakehouse).
        mode: Working mode (solo, team).
        output_dir: Parent directory where project folder is created.
        dry_run: If True, print what would be created without writing files.

    Returns:
        Path to the created project directory.
    """
    config = load_config(stack)
    project_dir = output_dir / name

    if not dry_run and project_dir.exists():
        print(f"ERROR: Directory already exists: {project_dir}")
        print("Remove it first or choose a different name.")
        sys.exit(1)

    # Template context — all values available in {{placeholder}} substitution
    context = {
        "project_name": name,
        "date": date.today().isoformat(),
        "stack": stack,
        "mode": mode,
        "description": config.get("description", ""),
    }

    # ----- Collect directories -----
    all_dirs = []
    directories = config.get("directories", [])
    all_dirs.extend(directories)
    core_dirs = ["docs/adr", "backlog", ".claude/commands", ".engineering"]
    for d in core_dirs:
        if d not in all_dirs:
            all_dirs.append(d)

    # ----- Collect template files -----
    template_mappings = {
        "CLAUDE.md.tmpl": "CLAUDE.md",
        "CONTEXT.md.tmpl": "CONTEXT.md",
        "ARCHITECTURE.md.tmpl": "ARCHITECTURE.md",
        "README.md.tmpl": "README.md",
        "gitignore.tmpl": ".gitignore",
        "TASK-001.yaml.tmpl": "backlog/TASK-001.yaml",
        "pick-next-task.md.tmpl": ".claude/commands/pick-next-task.md",
        "complete-task.md.tmpl": ".claude/commands/complete-task.md",
        "create-task.md.tmpl": ".claude/commands/create-task.md",
        "ruff.toml.tmpl": ".engineering/ruff.toml",
        "pyproject.toml.tmpl": ".engineering/pyproject.toml",
        "ADR-000-template.md.tmpl": "docs/adr/ADR-000-template.md",
    }

    created_files = []
    rendered_contents = {}
    for template_name, output_name in template_mappings.items():
        template_path = TEMPLATES_DIR / template_name
        content = render_template(template_path, context)
        if content:
            created_files.append(output_name)
            rendered_contents[output_name] = content

    # ----- Extra files from config (e.g. requirements.txt) -----
    extra_files = config.get("extra_files", [])
    for filename in extra_files:
        created_files.append(filename)

    # ----- CI template selection based on stack -----
    ci_template_map = {
        "docs-only": "ci-docs.yml.tmpl",
        "python-data": "ci-python.yml.tmpl",
        "python-web": "ci-python.yml.tmpl",
        "databricks-lakehouse": "ci-python.yml.tmpl",
    }
    ci_template_name = ci_template_map.get(stack)
    ci_content = None
    if ci_template_name:
        ci_template_path = TEMPLATES_DIR / ".github" / "workflows" / ci_template_name
        ci_content = render_template(ci_template_path, context)
        if ci_content:
            created_files.append(".github/workflows/ci.yml")
            if ".github/workflows" not in all_dirs:
                all_dirs.append(".github/workflows")

    # ----- AGENTS.md symlink -----
    created_files.append("AGENTS.md -> CLAUDE.md")

    # ----- Dry run: print plan and return -----
    if dry_run:
        print(f"[DRY RUN] Project '{name}' would be created at: {project_dir}")
        print(f"Stack: {stack} | Mode: {mode}")
        print("\nDirectories:")
        for d in sorted(all_dirs):
            print(f"  {d}/")
        print("\nFiles:")
        for f in sorted(created_files):
            print(f"  {f}")
        return project_dir

    # ----- Write: create directories -----
    for dir_path in all_dirs:
        (project_dir / dir_path).mkdir(parents=True, exist_ok=True)

    # ----- Write: create template files -----
    for output_name, content in rendered_contents.items():
        file_path = project_dir / output_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

    # ----- Write: create extra files -----
    for filename in extra_files:
        file_path = project_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()

    # ----- Write: CI file -----
    if ci_content:
        ci_file_path = project_dir / ".github" / "workflows" / "ci.yml"
        ci_file_path.parent.mkdir(parents=True, exist_ok=True)
        ci_file_path.write_text(ci_content)

    # ----- Write: AGENTS.md symlink -----
    agents_path = project_dir / "AGENTS.md"
    agents_path.symlink_to("CLAUDE.md")

    # ----- Print summary -----
    print(f"\nProject '{name}' created at: {project_dir}")
    print(f"Stack: {stack}")
    print(f"Mode: {mode}")
    print(f"Date: {context['date']}")
    print(f"\nDirectories created: {len(all_dirs)}")
    print(f"Files created: {len(created_files)}")
    print("\nFiles:")
    for f in sorted(created_files):
        print(f"  {f}")
    print("\nNext steps:")
    print(f"  cd {project_dir}")
    print("  git init")
    print("  git add -A && git commit -m 'Initial scaffold from ai-project-templates'")

    return project_dir


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(args: list = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Scaffold a new project with governance, PM, and engineering standards.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scaffold.py --name my-project --stack python-data --mode solo\n"
            "  python scaffold.py --name api-service --stack python-web --mode team --output-dir ~/projects\n"
            "  python scaffold.py --name docs-repo --stack docs-only --mode solo\n"
        ),
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Project name (used as directory name)",
    )
    parser.add_argument(
        "--stack",
        required=True,
        choices=VALID_STACKS,
        help="Stack type: python-data, python-web, or docs-only",
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=VALID_MODES,
        help="Working mode: solo or team",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files",
    )
    return parser.parse_args(args)


def main():
    """Main entry point."""
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created output directory: {output_dir}")

    create_project(
        name=args.name,
        stack=args.stack,
        mode=args.mode,
        output_dir=output_dir,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
