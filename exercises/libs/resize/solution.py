import os, sys
from PIL import Image


if __name__ == '__main__':
    input, scale, output = sys.argv[1:]
    scale = int(scale)

    with Image.open(input) as image:
        size = (int(image.width * scale / 100), int(image.height * scale / 100))
        image.resize(size).save(output)


