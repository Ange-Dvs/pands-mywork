# salaries.py
# This program makes a list called salaries that has 10 random numbers between 20000 - 80000
# The numbers generated are seeded so that it always generates the same random numbers
# 5000 is added to the original salaries  
# Then 5% is added, lastly the salaries are cast from floats to ints and stored as new_salaries. 
#
# Author: Angela Davis

import numpy as np 

min_salary = 20000
max_salary = 80000
num_of_entries = 10

np.random.seed(1)
salaries =  np.random.randint(min_salary, max_salary, num_of_entries)
print(salaries)

salaries_plus = salaries + 5000
print(salaries_plus)

salaries_five_percent = salaries_plus * 1.05
print(salaries_five_percent)

new_salaries = salaries_five_percent.astype(int)
print(new_salaries)

