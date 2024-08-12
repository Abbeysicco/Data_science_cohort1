# # 1. Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that 
# # take in two numbers and return the result of the operation.
# def add(num1,num2):
#     return num1+num2
# def subtract(num1,num2):
#     return num1-num2
# def multiply(num1,num2):
#     return num1*num2 
# def divide(num1,num2):
#     if num2!=0:
#         return num1/num2
#     else:
#         return 'Error. Division by zero not possible'
    
# # Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols
# operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

# # Create a function 'calculator' that prompts the user to input the first number.
# def calculator():
#     num1 = float(input('Enter the first Number: '))
#     should_continue = True

# # Use a for loop to print the available operation symbols.
#     print('\n Available Symbols')
#     for symbol in operations.keys():
#         print(symbol)

# # Create a while loop that will continue to run until the user chooses to end the current calculation
#     while should_continue:

# # Inside the while loop, prompt the user to select an operation symbol.
#         operation = input('\n Enter an operational symbol: ')

# # Prompt the user to input the second number
#         num2 = float(input('Enter the second number: '))

# # Use the dictionary to retrieve the function that corresponds to the selected operation symbol 
# # and store it in a variable 'calculation_function'
#         calculation_function = operations.get(operation)

# # Perform the calculation by calling the 'calculation_function' on the two input numbers 
# # and store the result in a variable 'answer'.
#         if calculation_function:
#             result = calculation_function(num1, num2)

# # Print the equation and the result of the calculation.
#             print(f'\n{num1} {operation} {num2}=  {result}')
#         else:
#             print('Invalid symbol entered, try again')

# # Ask the user if they would like to continue using the result as the first number for further calculations.
#         continue_calculation=input('\n Do you wish to continue with the result for the next calculation? (yes or no): ')
#         if continue_calculation=='yes':
#             num1 = result
#         else:
#             should_continue = False
# calculator()






import math  

class Calculator:  
    def __init__(self):  
        self.operations = {  
            '+': lambda x, y: x + y,  
            '-': lambda x, y: x - y,  
            '*': lambda x, y: x * y,  
            '/': lambda x, y: x / y if y != 0 else float('inf') 
        }  
    def add_operation(self, symbol, function):  
        self.operations[symbol] = function  

    def calculate(self, num1, symbol, num2):  
        if symbol not in self.operations:  
            print("Error: Invalid operation symbol.")  
            raise ValueError("Invalid operation symbol")  

        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):  
            print("Error: Inputs must be numbers.")  
            raise ValueError("Inputs must be numbers")  

        result = self.operations[symbol](num1, num2)  
        return result  

def exponentiation(x, y):  
    return (x **y)  

def square_root(x, y):  
    return math.sqrt(x)  

def logarithm(x, base):  
    return math.log(x, 10)  

# Create an instance of the Calculator class  
calc = Calculator()  

# Add advanced operations to the calculator  
calc.add_operation('**', exponentiation)  
calc.add_operation('sqrt', square_root)  
calc.add_operation('log', logarithm)  
print("Available operations:")
for symbol in calc.operations:
    print(symbol)

# Main program  
while True:  
    try:  
        num1 = float(input("Enter the first number: "))  
        symbol = input("Enter the symbol: ")
        if symbol in ['sqrt', 'log']:
            num2 = 0
        else:
            num2 = float(input("Enter the second number: "))  

        result = calc.calculate(num1, symbol, num2)  
        print("Result: ", result)  
    except ValueError as e:  
        print("Calculation error:", e)  

    choice = input("Do you want to continue? (y/n): ")  
    if choice.lower() != 'y':  
        break  