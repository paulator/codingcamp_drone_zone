import json
import cv2
import numpy as np
from PIL import Image

def suche_muell(loaded_bild):

    untere_grenze_rot = np.array([0,0,200])
    obere_grenze_rot = np.array([50,50,255])
    

    maske_rot = cv2.inRange(loaded_bild, untere_grenze_rot, obere_grenze_rot)
    
    konturen_rot, _ = cv2.findContours(maske_rot, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for kontur_r in konturen_rot:
        (x,y,w,h) = cv2.boundingRect(kontur_r)
        cv2.circle(loaded_bild, (x +w // 2, y+h // 2), 100, (0,0,0), 5)
    
    

    if len(konturen_rot):

        return(True)
    
    else:
        return(False)
    
   


jsonfile_name = '.\\output\\coords.json'

with open(jsonfile_name, 'r') as json_file:
    filtered_rows= json.load(json_file)

    print(filtered_rows)

zeile_mit_muell = []

for row in filtered_rows:
    
    bild_dateipfad = row['filename']
    print(bild_dateipfad)
    loaded_bild = cv2.imread('output\\' + bild_dateipfad)

    row['muell_gefunden'] = suche_muell(loaded_bild)

    zeile_mit_muell.append(row)



jsonfile_name = '.\\output\\result.js'

with open(jsonfile_name, 'w') as json_file:
    json_file.write("var jsonData = ")
    json.dump(zeile_mit_muell, json_file, indent=4)

    print(zeile_mit_muell)




