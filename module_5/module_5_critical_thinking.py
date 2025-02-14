# CSC500 Module 5 - Critical Thinking

# Part 1
import numpy as np

print("Rainfall Calculator")

# Initiate list of rainfall inches and get the number of years needed for the calculation
inches_list = []

num_years = int(input("Enter the number of years: "))

# Get the number of month for display
months = num_years * 12

# For each year in the input, get the rainfall in inches for each month and append it to a list
for i in range(num_years):

    i += 1
    print(f"Year {i}")

    for e in range(12):
        e += 1

        inches_rain = float(input(f"Enter the inches of rainfall for year {i} and month {e}: "))

        inches_list.append(inches_rain)

# Calculate the total inches and avg_rainfall

inches_list = np.array(inches_list)

total_inches = np.sum(inches_list)

avg_rainfall = round(np.average(inches_list),2)

# Display results
print(f"Number of months: {months}")
print (f'Total inches of rainfall: {total_inches}')
print(f'Average rainfall: {avg_rainfall}')

# Part 2
print("\nCSU Book Club Calculator")

# Initiate function to calculate points
def calculate_points(books_purchased):
    if books_purchased >= 8:
        return 60
    elif books_purchased >= 6:
        return 30
    elif books_purchased >= 4:
        return 15
    elif books_purchased >= 2:
        return 5
    else:
        return 0

# Get user input
books_purchased = int(input("Enter the number of books purchased this month: "))

# Implement logic to ensure the inputs are calculatable
if books_purchased < 0:
    print("Invalid input. Number of books cannot be negative.")

# Calculate the points and display result
else:
    points = calculate_points(books_purchased)
    print(f"You have been awarded {points} points!")
