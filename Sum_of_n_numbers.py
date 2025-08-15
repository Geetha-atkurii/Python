# Ask the user for a number n, then calculate and print the sum of numbers from 1 to n.

n = int(input("Enter a number: "))
sum_of_numbers = 0
for i in range(1, n + 1):
    sum_of_numbers += i  # Add the current number to the sum
print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")


# Ask the user for a number and print its multiplication table (from 1 to 10).
n = int(input("Enter a number to print its multiplication table: "))
for num in range(1, 11):
    result = n * num    
    print(f"{n} x {num} = {result}")
