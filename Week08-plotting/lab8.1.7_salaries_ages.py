import numpy as np 
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 10

np.random.seed(1) # adding a seed to the random numbers so the same numebers are always generated
salaries =  np.random.randint(min_salary, max_salary, num_of_entries)
print(salaries)

ages = np.random.randint(low = 21, high = 65, size = num_of_entries) # different way of getting randoms but not preferred

x_points = np.array(range(1, 101)) # generating an array of random numbers with the range 1 - 100 and setting as X points
y_points = x_points * x_points # have y eqauls to x sqaured

plt.scatter(salaries, ages, label ="salaries") # plotting a scatter plot using the salaries and ages generated above and giving the label salaries to the markers in the legend
plt.plot(x_points, y_points, color = "r", label="x squared") # plotting a red coloured line of the x and y points calculated above and labelling it x squared in the legend

plt.title("random plot") # adding a title to the plot
plt.xlabel("Salaries") # adding a label to the x axis on the plot
plt.ylabel("age") # adding a label to the y axis on the plot
plt.legend() # adding a legend to the plot 
plt.show()

plt.savefig("prettier-plot.png") #Saving plot as file called “prettier-plot.py”
