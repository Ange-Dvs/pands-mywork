# lab8.1.11_counties.py
# This program has a list of 5 counties, some counties appear more than others. 
# A pie chart is then generated of the counties.
# Author : Angela Davis

import numpy as np
import matplotlib.pyplot as plt

possible_counties = [ "Galway", "Mayo", "Cork", "Dublin", "Donegal"] ## make the array of occurences

counties = np.random.choice( possible_counties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size = (100)) # # pick 100 randomly from possible counties with the frequence set in p


unique, counts = np.unique(counties, return_counts=True) # this returns a tuple of the unique values and how many times they appear

'''plt.pie(counts, labels = unique) # makes a pie chart of the counties'''
plt.bar(unique, counts)
plt.legend() # adds a legend
plt.show()

