# lab7.1.4_readJSON.py
# Write a function that will read in a dict object from file
# Author: Angel Davis

import json
FILENAME = 'testdict.json'

def read_dict ():
    with open (FILENAME) as f:
        return json.load(f)

some_dict = read_dict()
print (some_dict)