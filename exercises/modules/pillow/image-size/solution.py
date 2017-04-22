from PIL import Image
import sys


if __name__ == '__main__':
    with Image.open(sys.argv[1]) as image:
        print("{} x {}".format(image.width, image.height))
