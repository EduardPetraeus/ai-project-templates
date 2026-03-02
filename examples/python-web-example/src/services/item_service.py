"""Business logic for item operations."""

from __future__ import annotations

from src.models.item import Item


class ItemService:
    """Service layer for item CRUD operations."""

    def __init__(self) -> None:
        self._items: dict[str, Item] = {}

    def create(self, item_id: str, name: str, description: str = "") -> Item:
        """Create a new item."""
        item = Item(id=item_id, name=name, description=description)
        self._items[item_id] = item
        return item

    def get(self, item_id: str) -> Item | None:
        """Get an item by ID."""
        return self._items.get(item_id)

    def list_all(self) -> list[Item]:
        """List all items."""
        return list(self._items.values())

    def delete(self, item_id: str) -> bool:
        """Delete an item. Returns True if found and deleted."""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False
