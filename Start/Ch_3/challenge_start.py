# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
from datetime import date


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def extractFields(data):
    longitude = data["geometry"]["coordinates"][0]
    latitude = data["geometry"]["coordinates"][1]
    return {
        "Magnitude": data["properties"]["mag"],
        "Place": data["properties"]["place"],
        "Felt Reports": data["properties"]["felt"],
        "Date": data["properties"]["time"],
        "Google Map link": f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    }

def getsig(data):
    significance = data["properties"]["sig"]
    if (significance is None):
        significance = 0
    return int(significance)

def timekey(data):
    return data["Date"]

data["features"].sort(key=getsig, reverse=True)
data = list(map(extractFields, data["features"]))
data = data[0:40]
data.sort(key=timekey, reverse=True)

with open("forty_most_events.csv", "w", newline='') as csvfile:
    fieldnames = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for event in data[0:40]:
        event["Date"] = date.fromtimestamp(int(event["Date"]) / 1000).strftime("%Y-%m-%d")
        writer.writerow(event)
