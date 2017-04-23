from PIL import Image
import argparse
import sys
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('--size', default=64, type=int)
    args = parser.parse_args()

    for file in args.files:
        basename, extension = os.path.splitext(file)
        output_file = "{}-thumbnail{}".format(basename, extension)

        with Image.open(file) as image:
            image.thumbnail((args.size, args.size))
            image.save(output_file)
