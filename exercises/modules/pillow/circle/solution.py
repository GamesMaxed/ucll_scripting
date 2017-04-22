from PIL import Image, ImageDraw


def create_image(width, height):
    return Image.new('RGB', (width, height))


if __name__ == '__main__':
    image = create_image(100, 100)

    draw = ImageDraw.Draw(image)
    upper_left = (0,0)
    lower_right = (99, 99)
    color = (255, 0, 0)
    draw.ellipse([upper_left, lower_right], color)
    
    image.save('circle.png')
