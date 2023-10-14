# Drone Zone

lorem ispum what is Drone Zone.  
Important:
Video has to be recorded with 60 fps for these scripts!

## Preparation - Video

Before executing the scripts:
1. Copy File to input
2. Rename file to "video.mp4" 


## Preparation - Geodata

Before executing the script: 
1. Copy the Geodata files from your phone.
2. Converte it on https://www.phantomhelp.com/LogViewer, download the csv-file.
3. Copy File to input
4. Rename file to "geodata.csv"
5. Important: Delete the first row from the geodata.csv file "sep=,"




## Step 1
As a first step we have to start the first script.

`python 01_create_images.py`

## Step 2
Second step:
Start the 2nd script which filters the csv-file.

`python 02_csv_reader.py`


## Step 3
Third Steps:
Start the third script which analizes the pictures and indetifies rubbish.

`python 03_detect_rubbish.py`