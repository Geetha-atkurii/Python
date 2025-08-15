# Ask the user for a number and calculate its factorial using a loop.
n = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i  
print(f"The factorial of {n} is: {factorial}")


#Using while loop
"""
n = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"The factorial of {n} is: {factorial}")
"""
