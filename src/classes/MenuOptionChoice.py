import json
from typing import Self


class MenuOptionChoice:
    def __init__(self, name: str = "", price: float = 0.0, amount_limit: int = 0, amount_required: int = 0, nested: Self | None = None):
        self.name = name
        self.price = price
        self.amount_limit = amount_limit
        self.amount_required = amount_required
        self.nested = nested

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "amount_limit": self.amount_limit,
            "amount_required": self.amount_required,
            "nested": self.nested.to_dict() if self.nested else None,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
