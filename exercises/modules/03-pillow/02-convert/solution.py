from PIL import Image
import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('--target-format', required=True)
    args = parser.parse_args()

    for file in args.files:
        target = os.path.splitext(file)[0] + "." + args.target_format
        print("{} -> {}".format(file, target))
        with Image.open(file) as image:
            image.save(target)
