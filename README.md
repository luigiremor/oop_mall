# Mall Object-Oriented Programming Project 🛒

This is a simple Mall project implemented using Object-Oriented Programming principles, including three classes: Item, Cart, and Customer.

### Classes
#### Item
The Item class represents an item in the mall. It has the following attributes:

name: A string representing the name of the item.
price: A float representing the price of the item.
#### Cart
The Cart class represents a shopping cart in the mall. It has the following attributes:

items: A list of Item objects representing the items in the cart.
customer: A Customer object representing the customer who owns the cart.
It also has the following methods:

add_item(item): Adds an Item object to the cart.
remove_item(item): Removes an Item object from the cart.
total_cost(): Calculates and returns the total cost of all the items in the cart.
#### Customer
The Customer class represents a customer in the mall. It has the following attributes:

name: A string representing the name of the customer.
age: An integer representing the age of the customer.
### Example Usage
Here is an example of how to use these classes together:
```python

# Create some items
item1 = Item("Shirt", 29.99, 2)
item2 = Item("Jeans", 39.99, 3)
item3 = Item("Shoes", 49.99, 1)

# Create a customer
customer = Customer("John", 25)

# Create a cart for the customer and add some items
cart = Cart(customer)
cart.add_item(item1)
cart.add_item(item2)

# Calculate the total cost of the cart
total_cost = cart.total_cost()

# Remove an item from the cart
cart.remove_item(item2)

# Calculate the total cost of the cart again
total_cost = cart.total_cost()
```
Conclusion
This is a simple implementation of a Mall project using Object-Oriented Programming principles. The Item, Cart, and Customer classes can be used to represent a shopping experience in a mall.
