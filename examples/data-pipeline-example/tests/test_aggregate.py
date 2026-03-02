"""Tests for the gold layer aggregation logic."""

from __future__ import annotations

from src.gold.aggregate import count_by_field


def test_count_by_field():
    """Verify grouping and counting by a field."""
    records = [
        {"department": "engineering", "name": "Alice"},
        {"department": "engineering", "name": "Bob"},
        {"department": "marketing", "name": "Carol"},
    ]
    result = count_by_field(records, "department")
    assert result["engineering"] == 2
    assert result["marketing"] == 1


def test_count_by_field_missing_values():
    """Verify missing field values are counted as 'unknown'."""
    records = [
        {"name": "Alice"},
        {"department": "engineering", "name": "Bob"},
    ]
    result = count_by_field(records, "department")
    assert result["unknown"] == 1
    assert result["engineering"] == 1
