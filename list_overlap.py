"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list_with_common_elements = []

for element in a:
    if element in b and element not in new_list_with_common_elements:
        new_list_with_common_elements.append(element)
print("Common elements between the two lists are:", new_list_with_common_elements)

# Extras: Randomly generate two lists to test this
import random
a = random.sample(range(1, 100), 15)
b = random.sample(range(1, 100), 20)
new_list = []
for element in a:
    if element in b and element not in new_list:
        new_list.append(element)
print("Randomly generated lists: ")
print("List a:", a)
print("List b:", b)
print("Common elements between the randomly generated lists are:", new_list)

# Write this in one line of Python
new_list_one_liner = list(set(a) & set(b))
print("Common elements list in one line:", new_list_one_liner)