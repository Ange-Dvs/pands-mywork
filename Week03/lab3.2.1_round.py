#lab3.2.1_round.py
#This program takes in a float number and outputs an in rounded up or down.
#Important to note that the round functions rounds to the nearest even number. 
#Author: Angela Davis

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}'.format(numberToRound,roundedNumber))
