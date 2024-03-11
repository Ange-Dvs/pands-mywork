# lab7.1.3_jsondict.py
# Write a function that will store a simple Dict to a file as JSON. TEST IT

import json
FILENAME = "testdict.json"
sample = dict(name='fred', age=31, grade=[1,34,55])

def write_dict (obj):
    with open (FILENAME, "wt") as f:
        json.dump(obj, f)

write_dict(sample)
    
