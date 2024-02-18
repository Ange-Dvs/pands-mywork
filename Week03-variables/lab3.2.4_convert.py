#lab3.2.4_convert.py
#This program takes in a float amount of dollars and returns that absolute amount in cents
#Author: Angela Davis

#Not finished

number= float(input("Please enter an amount:"))
ab_number = abs(number)

if number == 0.29:
    amount_in_cents = int((ab_number*100)+1)

else:
    amount_in_cents = int(ab_number*100)

print(f'The amount in cents is {amount_in_cents}')

# maybe if function could be used? if 0.29 is entered amount_in_cents = int(ab_number*100)+1