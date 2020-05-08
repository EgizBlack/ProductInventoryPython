from Product import Product
from Inventory import Inventory
from Console import Console

inventory = Inventory()

inventory.add_item(Product(1, 1.23, 200))
inventory.add_item(Product(2, 2.2, 50))
inventory.add_item(Product(3, 0.5, 1000))
inventory.add_item(Product(4, 5.99, 75))

console = Console(inventory)
console.run()
