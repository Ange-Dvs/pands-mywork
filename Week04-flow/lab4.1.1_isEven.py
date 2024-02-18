#lab4.1.1_isEven.py
#This program takes in a number from a user and advises if it is even or odd.
#Author: Angela Davis

number = int(input("Please enter a number:"))

if (number % 2) == 0:
    print(f"The number you entered is {number}\n{number} is an even number")

else:
    print(f"The number you have entered is {number}.\n{number} is an odd number.")