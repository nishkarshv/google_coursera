#! /usr/bin/env python3
import os
import requests
imagefolder = '/home/student-04-d994d532c433/supplier-data/images/'
url = 'http://localhost/upload/'
for files in os.listdir(imagefolder):
    if files.endswith('jpeg'):
        filename = imagefolder + files
        with open(filename, 'rb') as f:
            r = requests.post(url, files={'file': f})
