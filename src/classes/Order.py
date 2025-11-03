from classes import OrderMenuItem


class Order:
    def __init__(self, items: list[OrderMenuItem] | None = None):
        self.items = items or []