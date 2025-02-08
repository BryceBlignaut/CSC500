# CSC500-1
#Bryce Blignaut

# Initialize the ItemToPurchase Class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Prompt user for name, price, and quantity inputs (Item 1)
print("Item 1")
name1 = input("Enter the item name: ")
price1 = float(input("Enter the item price: "))
quantity1 = int(input("Enter the item quantity: "))

# Assign class attributes to item1
item1 = ItemToPurchase(name1, price1, quantity1)

print()

# Prompt user for name, price, and quantity inputs (Item 1)
print("Item 2")
name2 = input("Enter the item name: ")
price2 = float(input("Enter the item price: "))
quantity2 = int(input("Enter the item quantity: "))

# Assign class attributes to item2
item2 = ItemToPurchase(name2, price2, quantity2)

# Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

# Display total cost
print()
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")
