import numpy as np  

# Part 1: Bill calculator 
print("Bryce B Stakehouse - Thank you for dining with us!")  

# Fixed variables and empty list for costs
meal_costs = [] 
tip_rate = 0.18  
tax_rate = 0.07

# Input from user
num_items = int(input("How many food items are you purchasing? "))  

# This loop takes the cost of each item ordered and appends the meal_costs list
for i in range(num_items):  
    cost = float(input(f"Enter the price of item {i + 1}: $"))  
    meal_costs.append(cost)  

# Changing the list to a numpy array for an easy sum aggregations
meal_costs_array = np.array(meal_costs) 
total_meal_cost = np.sum(meal_costs_array)  

# Calculate tip, tax, and total amount  
tip_amount = total_meal_cost * tip_rate  
tax_amount = total_meal_cost * tax_rate  
total_cost = total_meal_cost + tip_amount + tax_amount  

# Print the amounts  
print("\nHere’s your bill:")  
print(f"Total Meal Cost: ${total_meal_cost:.2f}")  
print(f"Tip (18%): ${tip_amount:.2f}")  
print(f"Sales Tax (7%): ${tax_amount:.2f}")  
print(f"Total Amount: ${total_cost:.2f}")  
