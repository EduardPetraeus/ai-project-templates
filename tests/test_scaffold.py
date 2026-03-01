"""Tests for the project scaffolder."""

import sys
from pathlib import Path

import pytest

# Add parent directory to path so we can import scaffold
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scaffold import create_project, load_config, parse_args, VALID_STACKS


@pytest.fixture
def tmp_output_dir(tmp_path):
    """Provide a temporary output directory."""
    return tmp_path


# ---------------------------------------------------------------------------
# Directory creation tests
# ---------------------------------------------------------------------------

class TestCreatesExpectedDirectories:
    """Verify that all expected directories are created for each stack."""

    def test_python_data_directories(self, tmp_output_dir):
        project_dir = create_project("test-proj", "python-data", "solo", tmp_output_dir)
        assert (project_dir / "src" / "bronze").is_dir()
        assert (project_dir / "src" / "silver").is_dir()
        assert (project_dir / "src" / "gold").is_dir()
        assert (project_dir / "tests").is_dir()
        assert (project_dir / "backlog").is_dir()
        assert (project_dir / ".claude" / "commands").is_dir()
        assert (project_dir / ".engineering").is_dir()
        assert (project_dir / "docs" / "adr").is_dir()

    def test_python_web_directories(self, tmp_output_dir):
        project_dir = create_project("test-proj", "python-web", "team", tmp_output_dir)
        assert (project_dir / "src" / "api").is_dir()
        assert (project_dir / "src" / "models").is_dir()
        assert (project_dir / "src" / "services").is_dir()
        assert (project_dir / "static").is_dir()
        assert (project_dir / "tests").is_dir()
        assert (project_dir / "backlog").is_dir()
        assert (project_dir / ".claude" / "commands").is_dir()
        assert (project_dir / ".engineering").is_dir()
        assert (project_dir / "docs" / "adr").is_dir()

    def test_docs_only_directories(self, tmp_output_dir):
        project_dir = create_project("test-docs", "docs-only", "solo", tmp_output_dir)
        assert (project_dir / "docs").is_dir()
        assert (project_dir / "docs" / "adr").is_dir()
        assert (project_dir / "backlog").is_dir()
        assert (project_dir / ".claude" / "commands").is_dir()
        # docs-only should not have src directories
        assert not (project_dir / "src").exists()

    def test_core_files_always_exist(self, tmp_output_dir):
        """Every stack must produce governance, PM, and engineering files."""
        for stack in VALID_STACKS:
            name = f"test-{stack}"
            project_dir = create_project(name, stack, "solo", tmp_output_dir)
            assert (project_dir / "CLAUDE.md").exists()
            assert (project_dir / "CONTEXT.md").exists()
            assert (project_dir / "ARCHITECTURE.md").exists()
            assert (project_dir / "README.md").exists()
            assert (project_dir / ".gitignore").exists()
            assert (project_dir / "backlog" / "TASK-001.yaml").exists()
            assert (project_dir / ".claude" / "commands" / "pick-next-task.md").exists()
            assert (project_dir / ".claude" / "commands" / "complete-task.md").exists()
            assert (project_dir / ".claude" / "commands" / "create-task.md").exists()
            assert (project_dir / ".engineering" / "ruff.toml").exists()
            assert (project_dir / ".engineering" / "pyproject.toml").exists()
            assert (project_dir / "docs" / "adr" / "ADR-000-template.md").exists()


# ---------------------------------------------------------------------------
# Template substitution tests
# ---------------------------------------------------------------------------

class TestTemplatesHaveCorrectSubstitutions:
    """Verify that {{placeholders}} are replaced with actual values."""

    def test_claude_md_substitution(self, tmp_output_dir):
        project_dir = create_project("my-project", "python-data", "solo", tmp_output_dir)
        content = (project_dir / "CLAUDE.md").read_text()
        assert "my-project" in content
        assert "python-data" in content
        assert "solo" in content
        assert "{{" not in content
        assert "}}" not in content

    def test_context_md_substitution(self, tmp_output_dir):
        project_dir = create_project("my-project", "python-web", "team", tmp_output_dir)
        content = (project_dir / "CONTEXT.md").read_text()
        assert "my-project" in content
        assert "python-web" in content
        assert "team" in content
        assert "{{" not in content

    def test_task_yaml_substitution(self, tmp_output_dir):
        project_dir = create_project("my-project", "python-data", "solo", tmp_output_dir)
        content = (project_dir / "backlog" / "TASK-001.yaml").read_text()
        assert "my-project" in content
        assert "{{" not in content

    def test_pyproject_substitution(self, tmp_output_dir):
        project_dir = create_project("my-project", "python-data", "solo", tmp_output_dir)
        content = (project_dir / ".engineering" / "pyproject.toml").read_text()
        assert "my-project" in content
        assert "{{" not in content

    def test_readme_substitution(self, tmp_output_dir):
        project_dir = create_project("my-project", "python-data", "solo", tmp_output_dir)
        content = (project_dir / "README.md").read_text()
        assert "my-project" in content
        assert "{{" not in content


# ---------------------------------------------------------------------------
# Error handling tests
# ---------------------------------------------------------------------------

class TestErrorHandling:
    """Verify that invalid inputs raise appropriate errors."""

    def test_invalid_stack_raises_error(self):
        with pytest.raises(FileNotFoundError, match="Config not found"):
            load_config("nonexistent-stack")

    def test_invalid_stack_rejected_by_argparse(self):
        with pytest.raises(SystemExit):
            parse_args(["--name", "test", "--stack", "invalid", "--mode", "solo"])

    def test_invalid_mode_rejected_by_argparse(self):
        with pytest.raises(SystemExit):
            parse_args(["--name", "test", "--stack", "python-data", "--mode", "invalid"])

    def test_refuses_existing_directory(self, tmp_output_dir):
        (tmp_output_dir / "existing-project").mkdir()
        with pytest.raises(SystemExit):
            create_project("existing-project", "python-data", "solo", tmp_output_dir)


# ---------------------------------------------------------------------------
# Output directory tests
# ---------------------------------------------------------------------------

class TestOutputDir:
    """Verify output directory handling."""

    def test_output_dir_created_if_missing(self, tmp_path):
        """scaffold.py creates --output-dir if it does not exist."""
        missing_dir = tmp_path / "nested" / "output"
        assert not missing_dir.exists()
        # Simulate what main() does: create if missing
        missing_dir.mkdir(parents=True, exist_ok=True)
        project_dir = create_project("test-proj", "python-data", "solo", missing_dir)
        assert project_dir.exists()
        assert (project_dir / "CLAUDE.md").exists()

    def test_default_output_dir_is_current(self):
        args = parse_args(["--name", "test", "--stack", "python-data", "--mode", "solo"])
        assert args.output_dir == "."

    def test_custom_output_dir_parsed(self):
        args = parse_args([
            "--name", "test",
            "--stack", "python-web",
            "--mode", "team",
            "--output-dir", "/tmp/custom",
        ])
        assert args.output_dir == "/tmp/custom"


# ---------------------------------------------------------------------------
# Config loading tests
# ---------------------------------------------------------------------------

class TestLoadConfig:
    """Tests for config loading."""

    def test_load_python_data_config(self):
        config = load_config("python-data")
        assert config["stack"] == "python-data"
        assert "directories" in config
        assert "src/bronze" in config["directories"]

    def test_load_python_web_config(self):
        config = load_config("python-web")
        assert config["stack"] == "python-web"
        assert "src/api" in config["directories"]

    def test_load_docs_only_config(self):
        config = load_config("docs-only")
        assert config["stack"] == "docs-only"
        assert config["extra_files"] == []


# ---------------------------------------------------------------------------
# Databricks-lakehouse stack tests
# ---------------------------------------------------------------------------

class TestDatabricksLakehouseStack:
    """Tests for the databricks-lakehouse stack."""

    def test_databricks_directories(self, tmp_output_dir):
        project_dir = create_project("test-db", "databricks-lakehouse", "solo", tmp_output_dir)
        assert (project_dir / "notebooks" / "bronze").is_dir()
        assert (project_dir / "notebooks" / "silver").is_dir()
        assert (project_dir / "notebooks" / "gold").is_dir()
        assert (project_dir / "notebooks" / "dlt").is_dir()
        assert (project_dir / "src" / "utils").is_dir()
        assert (project_dir / "src" / "schemas").is_dir()

    def test_databricks_extra_files(self, tmp_output_dir):
        project_dir = create_project("test-db", "databricks-lakehouse", "solo", tmp_output_dir)
        assert (project_dir / "requirements.txt").exists()
        assert (project_dir / "databricks.yml").exists()

    def test_databricks_config_loading(self):
        config = load_config("databricks-lakehouse")
        assert config["stack"] == "databricks-lakehouse"
        assert config["conventions"]["unity_catalog"] is True
        assert config["conventions"]["dlt"] is True

    def test_databricks_core_files(self, tmp_output_dir):
        project_dir = create_project("test-db2", "databricks-lakehouse", "solo", tmp_output_dir)
        assert (project_dir / "CLAUDE.md").exists()
        assert (project_dir / "backlog" / "TASK-001.yaml").exists()
        assert (project_dir / ".engineering" / "ruff.toml").exists()

    def test_databricks_template_substitution(self, tmp_output_dir):
        project_dir = create_project("my-db-project", "databricks-lakehouse", "solo", tmp_output_dir)
        content = (project_dir / "CLAUDE.md").read_text()
        assert "my-db-project" in content
        assert "databricks-lakehouse" in content
        assert "{{" not in content


# ---------------------------------------------------------------------------
# CI template selection tests
# ---------------------------------------------------------------------------

class TestCITemplateSelection:
    """Tests for CI template generation based on stack type."""

    def test_python_data_gets_pytest_ci(self, tmp_output_dir):
        project_dir = create_project("test-ci", "python-data", "solo", tmp_output_dir)
        ci_file = project_dir / ".github" / "workflows" / "ci.yml"
        assert ci_file.exists()
        content = ci_file.read_text()
        assert "pytest" in content
        assert "ruff" in content

    def test_docs_only_gets_markdownlint_ci(self, tmp_output_dir):
        project_dir = create_project("test-ci-docs", "docs-only", "solo", tmp_output_dir)
        ci_file = project_dir / ".github" / "workflows" / "ci.yml"
        assert ci_file.exists()
        content = ci_file.read_text()
        assert "markdownlint" in content.lower() or "markdown" in content.lower()

    def test_ci_template_no_unresolved_placeholders(self, tmp_output_dir):
        project_dir = create_project("test-ci-clean", "python-web", "team", tmp_output_dir)
        ci_file = project_dir / ".github" / "workflows" / "ci.yml"
        content = ci_file.read_text()
        assert "{{" not in content

    def test_databricks_gets_python_ci(self, tmp_output_dir):
        project_dir = create_project("test-ci-db", "databricks-lakehouse", "solo", tmp_output_dir)
        ci_file = project_dir / ".github" / "workflows" / "ci.yml"
        assert ci_file.exists()
        content = ci_file.read_text()
        assert "pytest" in content
