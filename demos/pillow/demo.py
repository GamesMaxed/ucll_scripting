#! /usr/bin/env python


import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "-small.jpg"

    with Image.open(infile) as image:
        image.resize(size).save(outfile)


