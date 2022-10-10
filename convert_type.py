#Write a Python program to change from json or yaml format to csv and Excel(XLSX) and vise-versa.Using
# Sample command:
# python3 convert_type.py --input test.csv --output test.json

import csv
import json
import argparse

data = {}
def input(fileCSV):
    with open(fileCSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['No']
            data[key] = row

def output(fileJSON):
    with open(fileJSON, 'w') as file:
        file.write(json.dumps(data, indent=8))

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Name of CSV file',type=input, required=True)
parser.add_argument('--output', help='Name of JSON file',type=output, required=True)
parser.parse_args()



