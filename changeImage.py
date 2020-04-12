#!/usr/bin/env python3

import os
import sys
from PIL import Image
import PIL
imagesfolder = '/home/student-04-d994d532c433/supplier-data/images/'
outputfolder = '/home/student-04-d994d532c433/supplier-data/images/'
for filename in os.listdir(imagesfolder):
    outfile = outputfolder+filename
    try:

        if filename.endswith("tiff"):

            image_path = os.path.join(imagesfolder, filename)
            with Image.open(image_path) as im:
                #print(im.resize((600,400)).convert("RGB"))
                #print(outfile)
                out = os.path.splitext(outfile)[0]+".jpeg"
                #print(out)
                im.resize((600,400)).convert("RGB").save(out,"JPEG")
    except PIL.UnidentifiedImageError:
        pass

