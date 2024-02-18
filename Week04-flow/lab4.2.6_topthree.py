# lab4.2.6_topthree
# The program generates 10 random numbers between 0 - 100 and prints them, the top 3 are then printed. 
# Author: Angela Davis

import random #importing random function to use

how_many        = 10                #variable created for how mamy numbers to generate
top_how_many    = 3                 #variable created for how mamy of the highest numbers are needed
range_from      = 0                 #variable created for lowest number to consider in the range for random number
range_to        = 100               #variable created for highest number to consider in the range for random number

ten_ran_numbers = []                #defining a blank list

for i in range(0,how_many):         #for the elements in the list from 0 to 10(defined above)
    ten_ran_numbers.append(random.randint(range_from, range_to)) #generate a random integer between the range 0-100 defined above and add it to the list
print(f"{how_many} random numbers\t {ten_ran_numbers}") #when the number of elements in the list reaches 10 it prints this line

top_numbs = ten_ran_numbers.copy()  #copying the list of 10 random numbers and call them top_numbs
top_numbs.sort(reverse= True)       #takes the copied list and uses the sort function to sort them in reverse order from highest to lowest
print (f"The top {top_how_many} are \t\t {top_numbs[0:top_how_many]}") # prints the out put of the top 3 numbers





