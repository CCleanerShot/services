from typing import Self
from classes import MenuOptionChoice


class OrderMenuOptionChoice(MenuOptionChoice):
    def __init__(self, name: str = "", price: float = 0.0, amount: int = 0, amount_limit: int = 0, amount_required: int = 0, nested: Self | None = None):
        super().__init__(name, price, amount_limit, amount_required, nested)
        self.amount = amount