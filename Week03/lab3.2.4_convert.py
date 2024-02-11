#lab3.2.4_convert.py
#This program takes in a float amount of dollars and returns that absolute amount in cents
#Author: Angela Davis


import math

number= float(input("Please enter an amount:"))
amount_in_cents = abs(number)

print(f'The amount in cents is {amount_in_cents}')

#abs won't work because we need to remove the decimal point. 
