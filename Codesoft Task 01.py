# This is a simple calculator program.

# Function to add two numbers
def add(a , b):
    return a + b

# Function to subtract two numbers
def subtract(a , b):
    return a - b

# Function to multiply two numbers
def multiply(a , b):
    return a * b

# Function to divide two numbers
def divide(a , b):
    return a / b

# Function to find power of a number
def power(a , b):
    return a ** b

# Main loop for the calculator
while True:

    # Display available operations
    print("1. Addition") 
    print("2. Subtraction") 
    print("3. Multiplication") 
    print("4. Division") 
    print("5. Exit") 

    # User input for operation selection
    select = input("Enter choice (1:2:3:4:5): ")

    # Perform operation based on user's choice
    if select == '1':
        # Addition
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print('.........................................................')
        print(f"             Answer: {num1} + {num2} = {result}")
        print('.........................................................')
        
    elif select == '2':
        # Subtraction
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtract(num1, num2)
        print('.........................................................')
        print(f"             Answer: {num1} - {num2} = {result}")
        print('.........................................................')

    elif select == '3':
        # Multiplication
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        print('.........................................................')
        print(f"             Answer: {num1} * {num2} = {result}")
        print('.........................................................')

    elif select == '4':
        # Division
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        print('.........................................................')
        print(f"             Answer: {num1} / {num2} = {result}")
        print('.........................................................')
    
    elif select == '5':
        # Exit
        print('.........................................................')
        print(f"             Exiting the calculator. Goodbye! :-")
        print('.........................................................')
        break

    else:
        # Invalid selection
        print('.........................................................')
        print(f"             Your selection is invalid. Please try again...")
        print('.........................................................')
