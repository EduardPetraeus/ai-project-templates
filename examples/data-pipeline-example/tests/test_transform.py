"""Tests for the silver layer transformation logic."""

from __future__ import annotations

from src.silver.transform import clean_records


def test_clean_records_strips_whitespace():
    """Verify whitespace is stripped from string values."""
    records = [{"name": "  Alice  ", "email": " alice@example.com "}]
    result = clean_records(records, required_fields=["name"])
    assert result[0]["name"] == "Alice"
    assert result[0]["email"] == "alice@example.com"


def test_clean_records_removes_incomplete():
    """Verify records missing required fields are removed."""
    records = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "", "email": "nobody@example.com"},
        {"name": "Bob", "email": ""},
    ]
    result = clean_records(records, required_fields=["name", "email"])
    assert len(result) == 1
    assert result[0]["name"] == "Alice"
