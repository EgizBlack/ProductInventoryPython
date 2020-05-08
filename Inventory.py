import locale


class Inventory:
    locale.setlocale(locale.LC_ALL, '')

    inventory = {}

    def add_item(self, item):
        if item.id in self.inventory:
            print("Product all ready in inventory")
        else:
            self.inventory[item.id] = item

    def remove_item(self, id):
        self.inventory.pop(id)

    def check_exist(self, id):
        return id in self.inventory

    def change_price(self, id, amount):
        if amount <= 0:
            print("Price can't be less than 0")
        else:
            self.inventory[id].price = amount

    def change_quantity(self, id, amount):
        if amount < 0:
            print("Quantity can't be less than 0")
        else:
            self.inventory[id].quantity = amount

    def print_item(self, id):
        print(
            f"----------------\n"
            f"Id: {self.inventory[id].id}\n"
            f"Price: {locale.currency(self.inventory[id].price, grouping=True)}\n"
            f"Quantity: {self.inventory[id].quantity}\n"
            f"----------------\n"
        )

    def print_all_items(self):
        for item in self.inventory:
            print(f"----------------\n"
                  f"ID: {self.inventory[item].id}\n"
                  f"Price: {locale.currency(self.inventory[item].price, grouping=True)}\n"
                  f"Quantity: {self.inventory[item].quantity}\n"
                  f"----------------\n")

    def inventory_value(self):
        value = 0
        for item in self.inventory:
            value += (self.inventory[item].price * self.inventory[item].quantity)
        print(locale.currency(value))
