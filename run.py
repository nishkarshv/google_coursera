#! /usr/bin/env python3
import os
import requests
descfolder = '/home/student-04-d994d532c433/supplier-data/descriptions/'
imagefolder = '/home/student-04-d994d532c433/supplier-data/images/'
imagelist = []
url = 'http://35.226.253.37/fruits/'
for files in os.listdir(descfolder):

    filename = descfolder + files
    with open(filename, 'r') as f:
        reads = f.readlines()
    image_name = imagefolder+ files.split(".")[0]+".jpeg"
    name = reads[0].strip()
    weight = reads[1].strip().split(" ")[0]
    desc = reads[2].strip()
    imagedict = {"name":name, "weight":weight, "description":desc, "image_name":image_name}
    imagelist.append(imagedict)
print(imagelist)
for imagedata in imagelist:
    x = requests.post(url, data=imagedata)
    #print(x)
    if x.status_code == 201:
        pass
    else:
        print("Failed")
