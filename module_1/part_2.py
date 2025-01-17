# Module 1 Critical Thinking

# Code for Part 2:
print("Multiplication and Division Program")
print()
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))

# If the first number is a zero, prompt the user for a new number
while number1 == 0:
    print("The first number cannot be zero for the division calculation.")
    number1 = float(input("Please enter a non-zero number as the first number: "))

# If the first number is a zero, prompt the user for a new number
while number2 == 0:
    print("The second number cannot be zero for the division calculation.")
    number2 = float(input("Please enter a non-zero number as the second number: "))

multiplication = number1 * number2

division = number1 / number2

# Print the results
print(f"The result of the multiplication is: ", multiplication)
print(f"The result of the division is: ", division)