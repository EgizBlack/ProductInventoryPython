from Inventory import Inventory
from Product import Product


class Console:
    inventory = Inventory()

    def __init__(self, inventory):
        self.inventory = inventory

    def get_input(self):
        is_invalid = True
        while is_invalid:
            try:
                value = float(input(">> "))
                if value < 0:
                    raise ValueError
                else:
                    is_invalid = False
                    return value
            except ValueError:
                print("Please enter a valid number")

    def run(self):
        quit_flag = True
        id = 0
        price = 0.0
        quantity = 0
        while quit_flag:
            print("""
--------------------------------
Print all products: enter 1
Print single product: enter 2
Print value of entire inventory: enter 3
Add a product: enter 4
Remove a product: enter 5
Change price of a product: enter 6
Change stock of a product: enter 7
Exit application: enter 8
--------------------------------
           """)

            usr_input = self.get_input()

            if usr_input == 1:
                print("--------------------------------")
                self.inventory.print_all_items()
                print("--------------------------------")
            elif usr_input == 2:
                print("Enter id of desired product")
                self.inventory.print_item(int(self.get_input()))
            elif usr_input == 3:
                self.inventory.print_all_items()
            elif usr_input == 4:
                quit_flag2 = True
                while quit_flag2:
                    print("Enter id")
                    try:
                        id = int(self.get_input())
                        if not self.inventory.check_exist(id):
                            quit_flag2 = False
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid number or id all ready exist")
                print("Enter a price")
                price = self.get_input()
                print("Enter quantity")
                quantity = round(self.get_input())
                self.inventory.add_item(Product(id, price, quantity))
            elif usr_input == 5:
                quit_flag3 = True
                print("Enter id")
                while quit_flag3:
                    try:
                        id = int(self.get_input())
                        if not self.inventory.check_exist(id):
                            raise ValueError
                        quit_flag3 = False
                    except ValueError:
                        print("Enter a valid id")
                self.inventory.remove_item(id)
            elif usr_input == 6:
                quit_flag4 = True
                print("Enter id")
                while quit_flag4:
                    try:
                        id = int(self.get_input())
                        if not self.inventory.check_exist(id):
                            raise ValueError
                        quit_flag4 = False
                    except ValueError:
                        print("Enter a valid id")
                print("Enter desired price")
                price = self.get_input()
                self.inventory.change_price(id, price)
            elif usr_input == 7:
                quit_flag5 = True
                print("Enter id")
                while quit_flag5:
                    try:
                        id = int(self.get_input())
                        if not self.inventory.check_exist(id):
                            raise ValueError
                        quit_flag5 = False
                    except ValueError:
                        print("Enter a valid id")
                print("Enter desired quantity")
                quantity = round(self.get_input())
                self.inventory.change_quantity(id, quantity)
            elif usr_input == 8:
                print("Goodbye!")
                quit_flag = False
