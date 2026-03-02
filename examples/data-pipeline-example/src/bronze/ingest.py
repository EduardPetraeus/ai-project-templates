"""Bronze layer — raw data ingestion.

This module handles loading raw data from external sources into the
bronze (landing) layer. Data is stored as-is with minimal transformation,
preserving the original format for auditability.
"""

from __future__ import annotations

import csv
from pathlib import Path


def ingest_csv(file_path: Path) -> list[dict]:
    """Ingest a CSV file into a list of row dictionaries.

    Args:
        file_path: Path to the CSV file.

    Returns:
        List of dictionaries, one per row.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    rows = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows
