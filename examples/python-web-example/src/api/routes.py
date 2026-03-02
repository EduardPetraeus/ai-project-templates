"""API route definitions for python-web-example."""

from __future__ import annotations

# Example route structure — replace with your web framework of choice
# (Flask, FastAPI, Django, etc.)

ROUTES = {
    "GET /health": "Health check endpoint",
    "GET /api/v1/items": "List all items",
    "POST /api/v1/items": "Create a new item",
    "GET /api/v1/items/{id}": "Get item by ID",
    "PUT /api/v1/items/{id}": "Update item by ID",
    "DELETE /api/v1/items/{id}": "Delete item by ID",
}


def health_check() -> dict:
    """Return service health status."""
    return {"status": "healthy", "service": "python-web-example"}
