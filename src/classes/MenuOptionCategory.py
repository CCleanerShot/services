import json
from classes.MenuOptionChoice import MenuOptionChoice

class MenuOptionCategory:
    def __init__(self, name: str = "", choices: list[MenuOptionChoice] = [], amount_limit: int = 0, amount_required: int = 0):
        self.name = name
        self.choices = choices or []
        self.amount_limit = amount_limit
        self.amount_required = amount_required

    def to_dict(self):
        return {
            "name": self.name,
            "choices": [c.to_dict() for c in self.choices],
            "amount_limit": self.amount_limit,
            "amount_required": self.amount_required,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)