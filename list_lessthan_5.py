"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#since the list is already sorted, can just print the first 5 elements
# list_a = a[:5]
# print(list_a)

#If the list is not sorted:
for number in a:
    if number < 5:
        print(number)  

# Create a new list with elements less than 5
new_list_less_than_5 = [number for number in a if number < 5]
print("List of numbers that are lessthan 5: ",new_list_less_than_5)

# Ask the user for a number and return a list of elements less than that number
user_input = int(input("Please enter a number: "))
user_list = [number for number in a if number < user_input]
print(f"List of numbers that are less than {user_input}: {user_list}")