# lab4.2.5_average.py
# This program reads a number from the user until the enter the value 0. 
# 0 causes the program end
# The program then prints out each of the numbers entered and the average of them using list. 
# Author: Angela Davis

# Take in number from user 
# While loop to check the number isn't 0 
# 


numbers = [] # Defining an empty list

number = int(input("Enter number (0 to quit):"))

while number != 0:
    numbers.append(number) # adds the number entered to the numbers list

    number = int(input("Enter another number (0 to quit):")) #prompts user for next number

for value in numbers: # defines value as the element in numbers list
    print(value)

average = float(sum(numbers)) / len(numbers) # defines the output as a floating number. Takes the sum of the values in the numbers list and divides it by the lenght of the list to get the average. 
print(f'The average is {average}')


