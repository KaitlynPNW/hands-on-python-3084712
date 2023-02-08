import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #turning dictionary/string into json
back_to_dict = json.loads(einstein_json) #turning json into dictionary
print("into json" + einstein_json)
print ("\n into dictionary")
pprint(back_to_dict)

with open("laureates.csv", "r") as f: #large csv file into json; r is read mode
    reader = csv.DictReader(f)
    laureates = list(reader) #list of dictionaries


with open("laureates.json", "w") as f: #w is write mode
    json.dump(laureates, f, indent=2) #dealing with files - dump and load -- NO 'S'
