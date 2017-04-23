from PIL import Image
import sys


def vertical_gradient(image):
    # Get pixels
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            # Compute color
            r = int(y / image.height * 255)
            color = (r, r, r)

            # Set color
            pixels[x, y] = color


def red_vertical_gradient(image):
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            r = int(y / image.height * 255)
            color = (r, 0, 0)
            pixels[x, y] = color

            
def horizontal_gradient(image):
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            r = int(x / image.width * 255)
            color = (r, r, r)
            pixels[x, y] = color

            
def inverse_horizontal_gradient(image):
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            r = 255 - int(x / image.width * 255)
            color = (r, r, r)
            pixels[x, y] = color

            
def diagonal_gradient(image):
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            r = int((x + y) / (image.width + image.height) * 255)
            color = (r, r, r)
            pixels[x, y] = color
            
            
if __name__ == '__main__':
    image = Image.new('RGB', (500, 500))

    table = { 'vertical': vertical_gradient,
              'red-vertical': red_vertical_gradient,
              'horizontal': horizontal_gradient,
              'inverse-horizontal': inverse_horizontal_gradient,
              'diagonal': diagonal_gradient }
    
    table[sys.argv[1]](image)
    image.show()
