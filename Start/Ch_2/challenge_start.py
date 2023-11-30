# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter, OrderedDict

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


types = []
for value in data["features"]:
    types.append(value["properties"]["type"])

c = Counter(types)
for key in OrderedDict(c):
    print(f"{key:15}: {c[key]}")