from models.item import Item


class Cart:

    def __init__(self) -> None:
        self.items = []
        self.total = 0

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item: Item) -> None:
        self.items.remove(item)
        self.total -= item.price

    def __repr__(self) -> str:
        return f"Cart({self.items}, {self.total})"

    def __str__(self) -> str:
        return f"Cart: {[f'{item.qtd}x {item.name}' for item in self.items]} - Total: {self.total}"
    