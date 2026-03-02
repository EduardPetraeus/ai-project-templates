"""Gold layer — business-level aggregations.

This module produces the final, consumption-ready datasets. Gold layer
data is optimized for analytics, reporting, and downstream consumers.
"""

from __future__ import annotations

from collections import Counter


def count_by_field(records: list[dict], field: str) -> dict[str, int]:
    """Count records grouped by a specific field value.

    Args:
        records: Cleaned records from the silver layer.
        field: The field name to group by.

    Returns:
        Dictionary mapping field values to their counts.
    """
    counter = Counter(record.get(field, "unknown") for record in records)
    return dict(counter.most_common())
