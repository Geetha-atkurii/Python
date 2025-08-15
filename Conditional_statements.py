#Conditional statements
"""
Conditional statements allow you to execute code based on certain conditions.
They are used to control the flow of execution in a program.
The most common conditional statements are `if`, `elif`, and `else`.
"""

# If statement
def check_number(num):
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print("The number is zero.")

# Example usage
check_number(10)
