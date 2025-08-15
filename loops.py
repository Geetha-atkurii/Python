#Loops

"""Loops are used to execute a block of code repeatedly.
They are essential for iterating over collections or performing repetitive tasks.
The two main types of loops in Python are `for` loops and `while` loops.
"""

#For loop
"""
A `for` loop iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.
for item in sequence:
    # code block to execute
"""
# Example of a for loop
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(f"Item: {item}")

# Example of iterating over a string
my_string = "Hello"
for char in my_string:
    print(f"Character: {char}")
# Example of iterating over a range
for i in range(5):
    print(f"Number: {i}")
   
for i in range(1, 11):
    print(f"Square of {i} is {i**2}")

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


#While loop
"""A `while` loop continues to execute as long as a specified condition is true.

variable initialization
while condition:
    # code block to execute
    variable update   

If the variable isn't updated correctly, it can lead to an infinite loop. 
"""
# Example of a while loop
count = 0
while count < 10:
    print(f"Count is: {count}")
    count += 1  # Increment the count by 1
