#Example-1
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Please enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
    
if num % 4 == 0:
    print(f"The number {num} is a multiple of 4.")
check = int(input("Please enter a number to divide by: "))
if num % check == 0:
    print(f"{num} divides evenly by {check}.")
else:
    print(f"{num} does not divide evenly by {check}.")


#Example-2
"""
    Given a list of numbers, use a loop and condition to extract and print all even numbers.
"""

a = [2, 6, 1, 3, 14, 8, 25, 7, 9, 10, 12, 15, 18, 20]
for k in a:
    if k % 2 == 0:
        print(f"{k} is even")
    else:
        print(f"{k} is odd")