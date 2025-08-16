"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
"""
number = int(input("Enter a number to find its divisors: "))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print("The divisors of", number, "are:", divisors)