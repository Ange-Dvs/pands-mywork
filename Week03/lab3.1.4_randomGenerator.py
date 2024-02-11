# lab3.1.4_randomGenerator.py
# This program prints out a random number between 1 and 10 using the module random
#Author: Angela Davis

import random

number = random.randint(1,10)
print("Here is a random number {}".format(number))

#Extra try modifying the program so that the user inputs the range
print("Now you can chose your own range for the next random number to be selected from.")
x = int(input("Enter the lowest number for your range: "))
y = int(input("Enter the highest number for your range: "))

number = random.randint(x,y)
print("Your random number between {} and {} is: {}".format (x, y, number))
