from models.cart import Cart


class Costumer:

    def __init__(self, name: str = 'Costumer', money: float = 0, email: str = 'costumer@email.com'):
        self.name = name
        self.email = email
        self.money = money

    def __str__(self) -> str:
        return f"Costumer: {self.name} - Money: {self.money}"
    
    def __repr__(self) -> str:
        return f"Costumer({self.name}, {self.money})"
    
    def buy(self, cart: Cart) -> None:
        if self.money >= cart.total:
            self.money -= cart.total
            cart.items.clear()
            cart.total = 0
            print("Successful purchase")
        else:
            print("You don't have enough money to buy this cart")