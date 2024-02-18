# lab4.1.2_grade.py
# This program reads a percentage mark and prints out the grade. 
# Author: Angela Davis

# • Under 40% => Fail 
# • Between 40% and 49% => Pass
# • Between 50% and 59% => Merit 2
# • Between 60% and 69% => Merit 1
# • Over 70% => Distinction

grade = float(input("Enter the percentage: "))

if grade < 0 or grade > 100:
    print("The grade is not valid.\nThe percentage should be between 0 & 100.")

elif grade >= 0 and grade < 40: 
    print("Fail")

elif grade >= 40 and grade <= 49: 
    print("Pass")

elif grade >=50 and grade <=59:
    print("Merit 2")

elif grade >= 60 and grade <= 69:
    print("Merit 1")

else: 
    print("Distinction")