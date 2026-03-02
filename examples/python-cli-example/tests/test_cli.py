"""Tests for the CLI module."""

from __future__ import annotations

from src.cli import parse_args


def test_parse_args_input_file():
    """Verify input_file is parsed correctly."""
    args = parse_args(["data.csv"])
    assert args.input_file == "data.csv"
    assert args.verbose is False


def test_parse_args_verbose():
    """Verify --verbose flag is parsed."""
    args = parse_args(["--verbose", "data.csv"])
    assert args.verbose is True
