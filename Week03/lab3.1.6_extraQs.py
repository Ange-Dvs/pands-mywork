# lab3.1.6_ExtraQs.py
# This program is to track the answers to the extra questions for the lab.

#6. Why does this expression cause an error? How can you fix it?
#Expression in lab: 
# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)
# This does not work because you are mixing strings and integers in the same variable
# without defining what the value entered should be.

# Alternative approach could be

number = 99 
print = ("I have eaten {} burritos.".format (number))


#7. Why is eggs a valid variable name while 100 is invalid?
#8. What three functions can be used to get the integer, floating-point number, or string version of a value?