# Write a Python program to read all the file from folder and change from:
# json or yaml to csv
# csv to json

import pandas as pd
import json, csv, yaml
import os


# Convert file .json to file .csv
def json_to_csv(file_Json): 
    new_json = pd.read_json(file_Json, orient='index')
    new_json.to_csv(str(file_Json).replace('.json','json_new.csv'), index=False)

# Convert file .csv to file .json
def csv_to_json(file_CSV): 
    new_csv = pd.read_csv(file_CSV)
    new_csv.to_json(str(file_CSV).replace('.csv','csv_new.json'))

# Convert file .yaml to file .csv
def yaml_to_csv(file_Yaml):
    with open(file_Yaml, 'r') as file:
        data = yaml.full_load(file) # get data from file .yaml
        fieldnames = []
        for item in data[0]:
            fieldnames.append(item) # Add fieldnames

    new_csv = str(file_Yaml).replace('.yaml', 'yaml_new.csv')
    with open(new_csv, 'w', newline='') as f: # write to file .csv
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

try:
    path = input()
    list_file = os.listdir(path=path)

    for each_file in list_file:
        file = os.path.join(path, each_file)# select file path with os.path.join

        if each_file.endswith('.csv'):
            csv_to_json(file)
        elif each_file.endswith('.json'):
            json_to_csv(file)
        elif each_file.endswith('.yaml'):
            yaml_to_csv(file)

    if (not each_file.endswith('.csv') and not each_file.endswith('.json') and not each_file.endswith('.yaml')) in list_file: # if can not find suitable file
        print("No file match")
    else:
        print("Done.")

except:
    print("Not a folder.")





