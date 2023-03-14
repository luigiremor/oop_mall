from models.cart import Cart
from models.item import Item


cart = Cart()

apple = Item("Apple", 1.5, 3)
banana = Item("Banana", 2.5, 1)
shrimp = Item("Shrimp", 10.5, 2)
filet_mignon = Item("Filet Mignon", 20.5, 3)

cart.add_item(apple)
cart.add_item(banana)
cart.add_item(shrimp)
cart.add_item(filet_mignon)
cart.remove_item(banana)

print(cart)

