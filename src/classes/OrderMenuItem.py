from classes import MenuItem, OrderMenuOptionCategory


class OrderMenuItem(MenuItem):
    def __init__(self, name: str = "", price: float = 0.0, option_categories: list[OrderMenuOptionCategory] = [], category: str = "", special_instructions: bool = False):
        super().__init__(name, price, option_categories, category, special_instructions)