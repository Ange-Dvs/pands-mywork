#lab3.1.2_sub.py
#This program takes in two numbers from a user and subtracts the first from the second one.
#Author:Angela Davis

x = str(input("Enter first number: "))
y = str(input("Enter second number: "))
answer = x-y
print ("{} minus {} is {} ".format (x, y, answer))

#Extra question: when the program is running, try entering in something that is not an int eg 1.1 or hello
#Answer: Yes error is thrown because we are telling the program that an integer will be entered so it is not able to handle a string or float number. 
#Strings can't be used innately in a maths equation, hence hello would throw an error even without int(input()) defined.
#If we wanted the program to be able to handle something like 1.1 we would need to replace int(input()) w/ float(input()).