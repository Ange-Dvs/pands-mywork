# lab3.1.6_ExtraQs.py
# This program is to track the answers to the extra questions for the lab.

#6. Why does this expression cause an error? How can you fix it?
#Expression in lab: 
# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)
# This does not work because you are mixing strings and integers in the same string. 
# You need to cast the integer to a string.

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

#7. Why is eggs a valid variable name while 100 is invalid?
# A: variables must start with a letter and can't begin with a number. 
# you could have eggs100, eggs_100, onehundred_eggs but the variable can't begin with a number.

#8. What three functions can be used to get the integer, floating-point number, or string version of a value?
# integer = int(value)
# floating point number = float(value)
# String = str(value)