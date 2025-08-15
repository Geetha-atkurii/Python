# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


import datetime

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
# current_year = 2025 #hardcoding

current_year = datetime.datetime.now().year    #using datetime module to get the current year
years_until_100 = 100 - age
year_turn_100 = current_year + years_until_100
print(f"Hello {name}! You will turn 100 years old in the year {year_turn_100}.")
