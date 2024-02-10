#lab3.2.3_floor.py
#This program takes in a float and outputs an int rounded down.
#Math module will be used for this "math.floor()"
#Author: Angela Davis

import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))

