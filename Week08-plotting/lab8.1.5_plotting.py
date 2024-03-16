# lab8.1.2_plotting.py
# This program plaots the function y = m^2
# Author: Angela Davis 

import numpy as np
import matplotlib.pyplot as plt

x_points = np.array(range(1, 101))
y_points = x_points * x_points

plt.plot (x_points, y_points)
plt.show()