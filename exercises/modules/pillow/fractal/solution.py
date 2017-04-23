import argparse
from PIL import Image
import re


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, c):
        return Complex(self.re + c.re, self.im + c.im)

    def __mul__(self, c):
        return Complex(self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re)

    def abs(self):
        return (self.re * self.re + self.im * self.im) ** 0.5


def mandelbrot(c, max_steps, bound):
    z = Complex(0, 0)

    for i in range(max_steps):
        z = z * z + c

        if z.abs() > bound:
            return i / (max_steps - 1)

    return max_steps


class Projection:
    def __init__(self, image_size, center, size):
        cx, cy = center
        self.left = cx - size / 2
        self.top = cy + size / 2
        self.size = size
        self.dx = size / image_size
        self.dy = size / image_size

    def at(self, x, y):
        px = self.left + self.dx * x
        py = self.top - self.dy * y

        return Complex(px, py)
    

def generate_image(image_size, projection, max_steps, bound):
    image = Image.new('RGB', (image_size, image_size))

    pixels = image.load()
    
    for y in range(image_size):
        print("Computing row {}".format(y), flush=True)
        for x in range(image_size):
            c = projection.at(x, y)
            value = int(mandelbrot(c, max_steps, bound) * 255)
            color = (value, value, value)
            pixels[x,y] = color

    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-c', '--center', required=True)
    parser.add_argument('-s', '--domain-size', required=True, type=float)
    parser.add_argument('-S', '--image-size', required=True, type=int)
    parser.add_argument('--max-iterations', default=100, type=int)
    parser.add_argument('--bound', default=10.0, type=float)
    args = parser.parse_args()

    match = re.fullmatch(r'\(([-.0-9]+),([-.0-9]+)\)', args.center)
    cx = float(match.group(1))
    cy = float(match.group(2))
    projection = Projection(args.image_size, (cx, cy), args.domain_size)

    image = generate_image(args.image_size, projection, args.max_iterations, args.bound)
    if args.output:
        image.save(args.output)
    else:
        image.show()
        
    
