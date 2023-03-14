class Item:

    def __init__(self, name: str = 'Teste', price: float = 0, qtd: float = 0     ) -> None:
        self.name = name
        self.qtd = qtd
        self.price = qtd * price

    def __str__(self) -> str:
        return f"Item: {self.name} - Price: {self.price}"

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.price})"