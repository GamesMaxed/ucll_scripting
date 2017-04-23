from PIL import Image, ImageDraw


def create_image(width, height):
    return Image.new('RGB', (width, height))

def create_frame(index):
    frame = create_image(100, 100)
    
    draw = ImageDraw.Draw(frame)
    upper_left = (index,45)
    lower_right = (index + 10, 55)
    color = (255, 0, 0)
    draw.ellipse([upper_left, lower_right], color)

    return frame

    
if __name__ == '__main__':
    frames = [ create_frame(index) for index in range(100) ]

    frames[0].save('animation.gif', save_all=True, append_images=frames[1:], duration=1, loop=True)
