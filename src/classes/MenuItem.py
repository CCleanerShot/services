import json
from classes import MenuOptionCategory


class MenuItem:
    def __init__(self, name: str = "", price: float = 0.0, option_categories: list[MenuOptionCategory] = [], category: str = "", special_instructions: bool = False):
        self.name = name
        self.price = price
        self.options_categories = option_categories or []
        self.category = category
        self.special_instructions = special_instructions


    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "options": [o.to_dict() for o in self.options_categories],
            "category": self.category,
            "special_instructions": self.special_instructions,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)