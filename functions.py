#Functions

"""
    Block of code
    Repeated use
    Also functions are used to divide the code into smaller parts
"""

def sayHello():
    print("Hello, World!")
# Calling the function
sayHello()

#Arguments and Parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

#Return values
def add_numbers(a, b):
    x = a + b
    return x
result = add_numbers(5, 3)
print(f"The sum is: {result}")

#Lambda functions
"""
Lambda functions are small anonymous functions defined with the `lambda` keyword.
They can take any number of arguments but can only have one expression.
"""
expression = lambda x: x * 2
print(f"Result of lambda function: {expression(5)}")

