#..........................................This is a calculator I made...................................................

# addition two numbers
def add(a , b):
    return a + b

# subtraction two numbers
def subtract(a , b):
    return a - b

#  multiplication two numbers
def multiply(a , b):
    return a * b

# divition two numbers
def divide(a , b):
    return a / b

# power of the value

def power(a , b):
    return a ** b

while True:

# list of functions to use it
    
    print("1. adiition") 
    print("2. subtraction") 
    print("3. multiplication") 
    print("4. Division") 
    print("5. Exit") 

# selected function to use 
    
    select = input("Enter choice 1 : 2 : 3 : 4 : 5 :  :-  ")

    # condition check
    if select == '1':
        # user input
        num1 = float(input("Enter first number:- "))
        num2 = float(input("Enter second number:- "))
        result = num1 + num2
        print('.........................................................')
        print(f"             Answer :- {num1} + {num2} = {result}")
        print('.........................................................')
        
    elif select == '2':
        num1 = float(input("Enter first number:- "))
        num2 = float(input("Enter second number:- "))
        result = num1 - num2
        print('.........................................................')
        print(f"             Answer :- {num1} - {num2} = {result}")
        print('.........................................................')

    elif select == '3':
        num1 = float(input("Enter first number:- "))
        num2 = float(input("Enter second number:- "))
        result = num1 * num2
        print('.........................................................')
        print(f"             Answer :- {num1} * {num2} = {result}")
        print('.........................................................')

    elif select == '4':
        num1 = float(input("Enter first number:- "))
        num2 = float(input("Enter second number:- "))
        result = num1 / num2
        print('.........................................................')
        print(f"             Answer :- {num1} / {num2} = {result}")
        print('.........................................................')
    
    elif select == '5':
        print('.........................................................')
        print(f"             Exiting The Calculator . Goodbye :-   ")
        print('.........................................................')
        break

    else :
        print('.........................................................')
        print(f"             Your selection is invalit                  ")
        print(f"                 Please Try again ...                 ")
        print('.........................................................')

