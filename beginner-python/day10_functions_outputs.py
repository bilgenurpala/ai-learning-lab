# Calculator

# Write a **comprehensive Calculator** using functions and dictionaries.

# Rules:
# - Create separate functions for `add`, `subtract`, `multiply`, `divide`
# - Store all operations in a dictionary: `{"+": add, "-": subtract, ...}`
# - Ask the user for the first number
# - Show available operations and ask which one to use
# - Ask for the second number and show the result
# - After each calculation ask:
#   - Type `"yes"` → continue calculating with the **result** as the first number
#   - Type `"no"` → start over with a new first number
# - Handle division by zero

# Example output:
# ```
# Enter a number: 10
# Pick an operation: + - * /
# Pick an operation: +
# Enter the next number: 5
# 10 + 5 = 15
# Continue calculating with 15? (yes/no):

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    num1 = float(input("Enter a number: "))
    while True:
        print("Pick an operation: " + " ".join(operations.keys()))
        operation = input("Pick an operation: ")
        if operation not in operations:
            print("Invalid operation. Please try again.")
            continue
        num2 = float(input("Enter the next number: "))
        result = operations[operation](num1, num2)
        if result is None:
            break
        print(f"{num1} {operation} {num2} = {result}")
        if input(f"Continue calculating with {result}? (yes/no): ").lower() != "yes":
            break
        num1 = result
