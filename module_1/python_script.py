# Source Code for Part 1:
print("Part 1: Addition and Subtraction")
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform addition and subtraction
addition_result = num1 + num2
subtraction_result = num1 - num2

# Display results
print(f"The result of addition is: {addition_result}")
print(f"The result of subtraction is: {subtraction_result}")

# Part 2: Multiplication and Division

# Pseudocode for Part 2:
# 1. Prompt the user to input the first number (num1).
# 2. Prompt the user to input the second number (num2).
# 3. Convert the inputs to floats.
# 4. Perform multiplication (num1 * num2) and store the result.
# 5. Perform division (num1 / num2) and store the result (ensure num2 is not zero).
# 6. Print the multiplication result.
# 7. Print the division result (if num2 is not zero).

# Source Code for Part 2:
print("\nPart 2: Multiplication and Division")
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform multiplication and division
multiplication_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "undefined (division by zero is not allowed)"

# Display results
print(f"The result of multiplication is: {multiplication_result}")
print(f"The result of division is: {division_result}")