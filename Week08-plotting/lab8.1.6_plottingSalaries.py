import numpy as np 
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 10

np.random.seed(1)
salaries =  np.random.randint(min_salary, max_salary, num_of_entries)
print(salaries)

plt.hist(salaries)
plt.show()
