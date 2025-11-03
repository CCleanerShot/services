from classes import MenuOptionCategory, MenuOptionChoice


class OrderMenuOptionCategory(MenuOptionCategory):
    def __init__(self, name: str = "", choices: list[MenuOptionChoice] = [], amount_limit: int = 0, amount_required: int = 0):
        super().__init__(name, choices, amount_limit, amount_required)