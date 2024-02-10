#lab3.2.2_absolute.py
#This program takes in a number from the user and gives the absolute value.
#The output shown as a example is 4.0, this .0 implies the output should be a float.
# float(input) below is defining the input from the user as a float upfront. 
#Author: Angela Davis

number= float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))
