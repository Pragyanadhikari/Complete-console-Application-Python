# 5. Simple E-Commerce System

# • Description: Create a console application to manage a simple e-commerce platform. Implement classes for Product, Cart, and Order. Include methods for adding products to the cart, calculating total prices, and processing orders.
# • OOP Concepts: Composition (carts contain products), Inheritance (different product categories), and Encapsulation (managing order data).

class Product:
    def __init__(self,product_id,product_name,product_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_price=product_price
    
    def __str__(self):
        return f"Name: {self.product_name} Price: {self.product_price}"
    
class Electronics(Product):
    def __init__(self, product_id, product_name, product_price, warranty):
        super().__init__(product_id, product_name, product_price)
        self.warranty = warranty
    
    def __str__(self):
        return super().__str__() + f", Warranty: {self.warranty} years"

class Dress(Product):
    def __init__(self, product_id, product_name, product_price, size):
        super().__init__(product_id, product_name, product_price)
        self.size = size
    
    def __str__(self):
        return super().__str__() + f", Size: {self.size}"
    
class Cart:
    def __init__(self):
        self.product_list = {}
    
    def add_product(self, product, quantity=1):
        if product.product_id in self.product_list:
            self.product_list[product.product_id]['quantity'] += quantity
        else:
            self.product_list[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"{product.product_name} to the cart.")

    def remove_product(self, product_id):
        if product_id in self.product_list:
            removed_product = self.product_list.pop(product_id)
            print(f"{removed_product['product'].product_name} removed from the cart.")
        else:
            print(f"Product with ID {product_id} not found.")

    def calculate_total(self):
        if not self.product_list:
            return "No items in the cart to calculate."
        else:
            total = 0
            for item in self.product_list.values():
                product = item['product']
                quantity = item['quantity']
                total += product.product_price * quantity
            return f"Total amount: {total:.2f}."

    def show_cart(self):
        if not self.product_list:
            print("Cart is empty.")
        else:
            print("Products in the cart:")
            for item in self.product_list.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{product} - Quantity: {quantity}")

class Order:
    def __init__(self, cart):
        self.cart = cart
        self.is_processed = False
    
    def process_order(self):
        if not self.cart.product_list:
            print("Cannot order an empty cart.")
        else:
            total = self.cart.calculate_total()
            print(f"Processing \n{total}")
            self.is_processed = True
            print("Order has been placed successfully.")

electronics1 = Electronics(101, "Laptop", 100000, 1)
electronics2 = Electronics(102, "Mobile", 50000, 1)
cloth1 = Dress(201, "Shirt", 800, "XL")
cloth2 = Dress(202, "Pant", 1200, "L")

cart=Cart()
cart.add_product(electronics1)
cart.add_product(cloth1)
cart.add_product(cloth2)
print(cart.calculate_total())
cart.show_cart()
cart.remove_product(102)
cart.remove_product(101)
cart.show_cart()
print(cart.calculate_total())
order=Order(cart)
order.process_order()