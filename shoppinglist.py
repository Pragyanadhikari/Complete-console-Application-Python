# 14. Shopping List Application
# • Description: Build a console application to manage a shopping list. Implement classes for Item, ShoppingList, and User. Include features for adding, removing, and displaying items on the shopping list.
# • OOP Concepts: Composition (shopping lists contain items), Inheritance (different item categories), and Encapsulation (managing item details).

class Item:
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, Category: {self.category}, Quantity: {self.quantity}"
class ShoppingList:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the shopping list.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Removed {item.name} from the shopping list.")
                return
        print(f"Item {item_name} not found in the shopping list.")

    def display_items(self):
        if not self.items:
            print("The shopping list is empty.")
        else:
            print(f"\nShopping List for {self.user.name}:")
            for item in self.items:
                print(f"  - {item}")
        print()

class User:
    def __init__(self, name):
        self.name = name
        self.shopping_list = ShoppingList(self)

    def add_to_list(self, item):
        self.shopping_list.add_item(item)

    def remove_from_list(self, item_name):
        self.shopping_list.remove_item(item_name)

    def view_list(self):
        self.shopping_list.display_items()

    def add_item(self):
        ask=True
        while ask:
            print(f"\nUser {self.name} Enter the details for the item you want to add:")
            name = input("Item name: ")
            category = input("Category (Grocery, Electronic, Clothing): ")
            quantity = int(input("Quantity: "))
            if category.lower() == "grocery":
                item = GroceryItem(name, quantity)
            elif category.lower() == "electronic":
                item = ElectronicItem(name, quantity)
            elif category.lower() == "clothing":
                item = ClothingItem(name, quantity)
            else:
                item = Item(name, "Miscellaneous", quantity) 
            self.add_to_list(item)
            ask=input("Do you want to add more (y for yes)?")
            if ask.lower()=='y':
                ask=True
            else:
                ask=False

class GroceryItem(Item):
    def __init__(self, name, quantity):
        super().__init__(name, "Grocery", quantity)

class ElectronicItem(Item):
    def __init__(self, name, quantity):
        super().__init__(name, "Electronic", quantity)

class ClothingItem(Item):
    def __init__(self, name, quantity):
        super().__init__(name, "Clothing", quantity)

class ShoppingListApplication:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' has been added to the system.")

    def show_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("Users:")
            for user in self.users:
                print(f"  - {user.name}")
        print()

app = ShoppingListApplication()
u1 = User("Pragyan")
u2 = User("Rita")
app.add_user(u1)
app.add_user(u2)
u1.add_item()
u2.add_item()
u1.view_list()
u2.view_list()
u1.remove_from_list("Apples")
u1.view_list()

app.show_all_users()