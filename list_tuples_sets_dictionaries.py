# Lists

"""
    Lists are ordered collections of items that can be changed (mutable).
    They can contain elements of different data types and allow duplicate values.
    Lists are indexed, meaning you can access elements by their position in the list.
    Lists are defined using square brackets [].
"""

# Tuples
"""
    Tuples are ordered collections of items that cannot be changed (immutable).
    They can contain elements of different data types and allow duplicate values.
    Tuples are indexed, similar to lists, meaning you can access elements by their position.
    Tuples are defined using parentheses ().
"""

# Sets

"""    
    Sets are unordered collections of unique items.
    They do not allow duplicate values and are defined using curly braces {}.
    Sets are mutable, meaning you can add or remove items. And these are not indexed, so you cannot access elements by position.
    Sets are useful for membership testing and eliminating duplicate entries.
"""

# Dictionaries
"""
    Dictionaries are collections of key-value pairs.
    They are ordered (as of Python 3.7) and mutable.
    Each key must be unique, and values can be of any data type.
    Does not allow duplicate keys.
    Dictionaries are defined using curly braces {} with key-value pairs separated by a colon (:).
    You can access values by their keys.
"""

#If the values are ordered, you can access them by their index. If not ordered, you cannot access them by index.

# Examples of each data structure:
# List
my_list = [1, 2, 3, 4, 5]
my_list_2 = ['apple', 'banana', 'cherry']
# Tuple
my_tuple = (1, 2, 3, 4, 2, 5)
# Set
my_set = {1, 2, 3, 4, 5}
# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}


#Methods and functions for each data structure:
# List methods
my_list.append(6)  # Adds an element to the end of the list
my_list.remove(3)  # Removes the first occurrence of an element
my_list.sort()     # Sorts the list in ascending order
my_list.insert(2, 10)  # Inserts an element at a specific index
my_list_2.extend(my_list)  # Extends the list with another list
my_list.remove(4)  # Removes the element 4 from the list
my_list.pop()      # Removes the 0th element from the list
my_list.clear()   # Clears the list
print(my_list)

# Tuple methods
my_tuple.count(2)  # Counts the occurrences of an element in the tuple
my_tuple.index(3)  # Returns the index of the first occurrence of an element
print(my_tuple)

# Set methods
my_set.add(6)      # Adds an element to the set
my_set.remove(3)   # Removes an element from the set

# Dictionary methods
my_dict['d'] = 4   # Adds a new key-value pair to the dictionary
my_dict.get('a')  # Returns the value for the specified key
my_dict.update({'e': 5})  # Updates the dictionary with another dictionary
my_dict.pop('b')   # Removes a key-value pair by key
my_dict.keys()     # Returns a view of the dictionary's keys
my_dict.values()   # Returns a view of the dictionary's values
my_dict.items()    # Returns a view of the dictionary's key-value pairs
print(my_dict)
