"""Tests for the item service."""

from __future__ import annotations

from src.services.item_service import ItemService


def test_create_item():
    """Verify item creation."""
    service = ItemService()
    item = service.create("1", "Test Item", "A test item")
    assert item.id == "1"
    assert item.name == "Test Item"


def test_list_items():
    """Verify listing all items."""
    service = ItemService()
    service.create("1", "Item A")
    service.create("2", "Item B")
    items = service.list_all()
    assert len(items) == 2


def test_delete_item():
    """Verify item deletion."""
    service = ItemService()
    service.create("1", "Item A")
    assert service.delete("1") is True
    assert service.get("1") is None
    assert service.delete("nonexistent") is False
