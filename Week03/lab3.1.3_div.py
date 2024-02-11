#lab3.1.3_dov.py
#This program reads in two numbers and divides the first one by the second and displays the result as a whole number with
# the remainder stated.
#Author: Angela Davis

x = int(input("Enter your first number:"))
y = int(input("Enter your second number: "))


answer = int(x//y) 
# // gives the answer as int. We are also defining that the answer should be an int(). 
# If had answer =(x/y) with not int() defined and only one / the program would give answer as a float when neccessary.
remainder = x%y 
# % gives us the remainder. Here we are not specifying if the answer should be an int() or not 
# however, since x & y are int() the answer will be an int()

print ("{} divided by {} is {} with remainder {}".format ( x, y, answer, remainder))

