# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:


def simplify(value):
    return {
        "place": value["properties"]["place"],
        "felt": value["properties"]["felt"],
        "type": value["properties"]["type"],
        "title": value["properties"]["title"],
        "sig": value["properties"]["sig"],
    }


def filterQuakeFelt(value):
    if value["felt"]:
        if value["felt"] >= 100:
            return value


def mostPeopleKey(value):
    if not value["felt"]:
        return 0
    return value["felt"]


def sortSig(value):
    sig = value["sig"]
    if not sig:
        sig = 0
    return sig


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

data = list(map(simplify, data["features"])) # List of dict

# 1: How many quakes are there in total?
print(f'Total quakes: {len(data)}')

# 2: How many quakes were felt by at least 100 people?
quake_felt = list(filter(filterQuakeFelt, data))
print(f'Total quakes felt by at least 100 people: {len(quake_felt)}')

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
max_felt = max(data, key=mostPeopleKey)
print(f'Place: {max_felt["place"]}, Reports: {max_felt["felt"]}')

# 4: Print the top 10 most significant events, with the significance value of each
data.sort(key=sortSig, reverse=True)
print('The 10 most significance events were:')
for item in list(iter(data))[0:10]:
    print(f'Event: {item["title"]}, Significance: {item["sig"]}')
