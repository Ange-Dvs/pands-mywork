# lab3.1.5_randomfruit2.py
# This program prints out a random fruit from a predefined tuple of fruits.
# As a best practise if the choices are predefined and not going to be changed
# we should use tuples () instead of a list []. 
# Author: Angela Davis

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear') #() makes this a tuple
index= random.randint(0, len(fruits)-1)
fruit = fruits[index]
print(f"Here is a random fruit: {fruit}")

# Idea: is there a way of having the user provide the fruits for the tuple? 
# Test below with a static/predefined lenght of the tuple.
# After running the program this seems to also work.
# Check next weeks lecture to see what is meant by "And for this example, we should have used a tuple, because we don’t change the list". 
# Maybe changes in lenght referenced. Or no changes to the content of the list after value is assigned to space 0 - 4.

import random
print("Now the program lets you enter 5 fruits and will give choose a random fruit from your list")
first_fruit = input("Enter your first fruit for the list: ")
second_fruit = input("Enter your second fruit for the list: ")
third_fruit = input("Enter your third fruit for the list: ")
forth_fruit = input("Enter your forth fruit for the list: ")
fifth_fruit = input("Enter your fifth fruit for the list: ")
 
fruits2 = (first_fruit, second_fruit, third_fruit, forth_fruit, fifth_fruit)

index2 = random.randint(0, len(fruits2)-1)

fruit2 = fruits2[index]
print(f"Here is a random fruit from your list: {fruit2}")