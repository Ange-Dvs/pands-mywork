#lab3.2.4_convert.py
#This program takes in a float amount of dollars and returns that absolute amount in cents
#Author: Angela Davis

amount = float(input('Please enter an amount:'))

dollars, cents = map(int, str(amount).split('.'))
# There are 4 main steps being carried out in the line above:
 
#       1 & 2.    str(amount).split('.') - this converts the float amount taken in from the user to a string. The string is then split using '.' as the seperator.
#                   You then have two strings the dollar amount as one string & cents amount as another.
#       3.        map(int, ....) then takes the strings and converts them to integers
#       4.        dollars, cents = - sets the variable names for the two integers derived from the string using the split function. 

absolute_cents = abs(dollars) * 100 + abs(cents) 
# abs() function is used to convert the int values of the dollars and cents variables to their absolute number to avoid any negative numbers causing issues with the end calculation.
# The two absolute values are added to give us the amount inputted by the user converted into cents.

print (f'The amount in cent is: {absolute_cents}')

# It then calculates the absolute amount in cents by multiplying the absolute value in dollars by 100 and adding the absolute value of the cents. 
