#Example-1
# Ask the user to input three numbers and print the largest one using if statements.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    print(number1, "is bigger")
elif number2 >= number1 and number2 >= number3:
    print(number2, "is bigger")
else:
    print(number3, "is bigger")
    
    
# Example-2
"""
Find the Largest Number in a List (without max())

Use a loop and condition to find the largest element in a given list.
"""

number_list = [3, 5, 7, 2, 8, -1, 4, 10, 12, 6, 0]

# for num in number_list:
    