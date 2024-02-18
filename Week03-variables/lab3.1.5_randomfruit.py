# lab3.1.5_randomfruit.py
# This program prints out a random fruit from a predefined list of fruits.
# Author: Angela Davis

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear'] #[] makes this a list

index= random.randint(0, len(fruits)-1)
# Next week we will learn more for lists and tuples. 
# Current assumption is that the line above is used the lenght of the list to select a random number. 
# There are 4 items in the list, len = 4. 
# However it seems we are starting at 0 for the lowest number in the range. 
# Then we look to be taking the lenght of the list (4) and - 1 = 3
# 0 = (Apple) 1 = Orange, 2 = Banana, 3 = Pear

fruit = fruits[index]
print(f"Here is a random fruit: {fruit}")

# Idea: is there a way of having the user provide the fruits for the list? 
# Test below with a static/predefined lenght of the list. Not sure how you could make the list dynamic.
# Test seems to work after running program multiple times with same input list I saw all fruits returned as the answer.
# Feels like this confirms my assumption above for the len() part of the code.

import random
print("Now the program lets you enter 5 fruits and will give choose a random fruit from your list")
first_fruit = input("Enter your first fruit for the list: ")
second_fruit = input("Enter your second fruit for the list: ")
third_fruit = input("Enter your third fruit for the list: ")
forth_fruit = input("Enter your forth fruit for the list: ")
fifth_fruit = input("Enter your fifth fruit for the list: ")
 
fruits2 = [first_fruit, second_fruit, third_fruit, forth_fruit, fifth_fruit]

index2 = random.randint(0, len(fruits2)-1)

fruit2 = fruits2[index]
print(f"Here is a random fruit from your list: {fruit2}")