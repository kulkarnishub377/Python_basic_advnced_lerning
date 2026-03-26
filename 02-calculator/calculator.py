"""
Terminal Calculator - Project 02
--------------------------------
What it does: A terminal calculator supporting addition, subtraction, 
multiplication, and division. Handles division by zero gracefully with a 
try/except block. Loops so the user can perform multiple calculations.

Pro Hints:
- We separate the mathematical logic into standalone functions.
- We use a dictionary-based dispatcher to map operators to functions cleanly.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Exception handling for division by zero
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def calculator():
    print("Welcome to the Terminal Calculator!")
    print("Operations supported: +, -, *, /")
    print("------------------------------------")
    
    # Store operators in a dictionary representing the dispatcher pattern
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        # Prompting user for inputs
        num1_in = input("Enter first number (or 'q' to quit): ")
        if num1_in.lower() == 'q':
            break
            
        operator = input("Enter operation (+, -, *, /): ")
        if operator not in operations:
            print("Invalid operator! Please use +, -, *, or /.\n")
            continue
            
        num2_in = input("Enter second number: ")
        
        # Safely parse numeric input
        try:
            num1 = float(num1_in)
            num2 = float(num2_in)
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue
            
        # Retrieve the relevant function based on the operator and execute it
        calculation_func = operations[operator]
        result = calculation_func(num1, num2)
        
        print(f"Result: {num1} {operator} {num2} = {result}\n")
        
if __name__ == "__main__":
    calculator()
