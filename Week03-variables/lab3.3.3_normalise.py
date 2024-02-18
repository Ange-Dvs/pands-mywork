# lab3.3.3_normalise.py
# This program reads a string and takes away any leading or trailing whitespaces.
# The string is also converted to lower case.
# The lenght of the input and output strings are then displayed for the user.
# Author: Angela Davis

#Getting the user input and counting
user_string = input('Please enter a string:\t')
user_string_length = len(user_string)

#Converting the user input to lowercase and striping any leading or ending zeros.
#Then counting the string length.
final_string = user_string.lower().strip()
final_string_length = len(final_string)

print(f'That String normalised is: {final_string}\nwe reduced theh input of the sring from {user_string_length} to {final_string_length} characters')