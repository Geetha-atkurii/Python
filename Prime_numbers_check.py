# Take the input from the user and use a for loop to print the prime numbers in between 1 and the user input.

input_number = int(input("Enter a number: "))

print("Prime numbers between 1 and", input_number, "are: ")

for num in range(2, input_number + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Checks up to the square root of num
    #for i in range(2, num): checks all numbers less than num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

