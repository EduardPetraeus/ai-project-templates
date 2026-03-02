"""Silver layer — data cleansing and transformation.

This module applies business rules, data type conversions, and quality
checks to promote data from bronze to silver. The silver layer contains
clean, validated, and standardized data.
"""

from __future__ import annotations


def clean_records(records: list[dict], required_fields: list[str]) -> list[dict]:
    """Remove records with missing required fields and strip whitespace.

    Args:
        records: Raw records from the bronze layer.
        required_fields: Fields that must have non-empty values.

    Returns:
        Cleaned records with whitespace stripped from all string values.
    """
    cleaned = []
    for record in records:
        # Strip whitespace from all string values
        stripped = {
            k: v.strip() if isinstance(v, str) else v for k, v in record.items()
        }
        # Check required fields
        if all(stripped.get(field) for field in required_fields):
            cleaned.append(stripped)
    return cleaned
