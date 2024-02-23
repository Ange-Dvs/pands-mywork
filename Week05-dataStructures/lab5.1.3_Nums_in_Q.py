# lab5.1.3.py
# This program puts 10 random numbers into a queue(list), 
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time, print it and the current numbers still in the queue. 
# (the command pop(0) takes the first element out of a list)
# Author: Angela Davis

import random

queue = [] 
numberOfNumbers=10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print(f'queue is {queue}')

while len(queue) != 0:
    current_number = queue.pop(0)
    print(f'The current number is {current_number} and the queue is {queue}')

print(f'the queue is now empty')

