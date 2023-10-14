import csv
import pandas as pd
import json

filtered_rows = []

df=pd.read_csv('.\\input\\geodata.csv')
fileName = 1
for index, row in df.iterrows():
    d=row.to_dict()
    if 'CAMERA.isVideo' in d and d['CAMERA.isVideo'] == True:
        filtered_rows.append({
            'latitude' : d['OSD.latitude'],
            'longitude' : d['OSD.longitude'],
            'filename': str(fileName) + '.jpg'
        })
        fileName = fileName + 1
#             #print(row)
    #print(d)

#print(filtered_rows)

jsonfile_name = '.\\output\\coords.json'

with open(jsonfile_name, 'w') as json_file:
    json.dump(filtered_rows, json_file, indent=4)

    print(filtered_rows)



