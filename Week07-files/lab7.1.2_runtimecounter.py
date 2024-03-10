# lab7.1.2_runtime.py
# This program counts how many times it has been run using a file existing locally on my local machine.
# Author: Angela Davis

import os.path
FILENAME = "count.txt"

def read_number(): # this function opens the file defined above as FILENAME
# some error handling added to create the files with 0 if it is not found
    try: # first we try to open the file assuming it exists
        with open(FILENAME) as f:
            number = int(f.read()) # reads the content of the flie and sets it as an integer to the variable number
            return number # the function then returns the number

    except IOError: # if the file doesn't exisit it then returns 0 as the value
        return 0

def write_number(number): # this function takes in the number from the read_number function
    with open(FILENAME, 'wt') as f: # opens the file assigned to the FILENAME variable in writing mode for text files "wt"
        f.write(str(number)) # writing as .txt means the answer must be cast to a string to store
        # the function then overwrites the number in the file to the number which has been returned from the read_Number() function

num = read_number() # assigned the outcome of read_number()function to variable num
num += 1 # taking the number from the file and adding 1 
print (f'we have run this program {num} times') # prints to the user the amount of times the file has been run using the number from the text file
write_number(num) # overwrites the original value in the file with the num value