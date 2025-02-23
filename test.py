class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.name == modified_item.name:
                if modified_item.description != "none":
                    item.description = modified_item.description
                if modified_item.price != 0:
                    item.price = modified_item.price
                if modified_item.quantity != 0:
                    item.quantity = modified_item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        
        if choice == 'a':
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, price, quantity, description))
        elif choice == 'r':
            name = input("Enter the name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the item name: ")
            price = int(input("Enter the new price (or 0 to keep unchanged): "))
            quantity = int(input("Enter the new quantity (or 0 to keep unchanged): "))
            description = input("Enter the new description (or 'none' to keep unchanged): ")
            cart.modify_item(ItemToPurchase(name, price, quantity, description))
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose again.")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)

main()