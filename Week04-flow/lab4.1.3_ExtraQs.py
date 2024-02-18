# lab4.2.3_ExtraQs.py
# This file is to contain the answers to the extra questions in the lab 4.2. 
# Author: Angela Davis

# 3. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
# equal to a Distinction.
# How would you modify the program in 1 to deal with this?
# I see two ways.
# A: One approach could be to adjust the conditionals to include X.5 to include in the higher bracket. 
#       If example if you have 39.5 or higher it should be considered in the 40% bracket. 
# A: Second approach is likely using some casting but casting to int will round down not consider if it's .5 or high to round up.
# A: Need to check more on the second way. 

grade = float(input("Enter the percentage: "))

if grade < 0 or grade > 100:
    print("The grade is not valid.\nThe percentage should be between 0 & 100.")

elif grade >= 0 and grade < 39.5: 
    print("Fail")

elif grade >= 39.5 and grade <= 49.4: 
    print("Pass")

elif grade >= 49.5 and grade <= 59.4:
    print("Merit 2")

elif grade >= 59.5 and grade <= 69.4:
    print("Merit 1")

else: 
    print("Distinction")

# 4. How would you use a while loop to modify 1 so that it keeps prompting the
# user for a number until the user enters -1
# Here you would need to have while loop that had a condition for checking if the number entered is != -1.
# While the condition is true the program should ask for a number. 
# When -1 is then entered it checks if it is odd or even (even though it will always be odd....)

print("This is the extra Q4 program\nYou will continue to be asked for a number until you enter -1")
number = int(input("Please enter a number:"))

while number != -1: 
    number = int(input('Please enter a number:'))

if (number % 2) != 0:
    print(f"The number you entered is {number}\n{number} is odd number")

else:
    print(f"The number you have entered is {number}.\n{number} is an even number.")