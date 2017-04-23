'''
Voor deze oefening moet je een afbeelding pixel per pixel inkleuren.
Je krijgt reeds voorbeeldcode (vertical_gradient) die illustreert
hoe je een verticale gradiënt moet produceren.
Je kan het resultaat ervan zien met

  python solution.py vertical


Implementeer de andere functies. Om te weten
wat elke functie moet doen, kan je de modeloplossing runnen
zoals beschreven staat in de commentaar bij elke
te implementeren functie.
'''


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
    '''
    Het resultaat moet hetzelfde zijn als
      python solution.py red-vertical
    '''

    
def horizontal_gradient(image):
    '''
    Het resultaat moet hetzelfde zijn als
      python solution.py horizontal
    '''
    raise NotImplementedError()

            
def inverse_horizontal_gradient(image):
    '''
    Het resultaat moet hetzelfde zijn als
      python solution.py inverse-horizontal
    '''


    
def diagonal_gradient(image):
    '''
    Het resultaat moet hetzelfde zijn als
      python solution.py diagonal
    '''
    raise NotImplementedError()




if __name__ == '__main__':
    image = Image.new('RGB', (500, 500))

    table = { 'vertical': vertical_gradient,
              'red-vertical': red_vertical_gradient,
              'horizontal': horizontal_gradient,
              'inverse-horizontal': inverse_horizontal_gradient,
              'diagonal': diagonal_gradient }
    
    table[sys.argv[1]](image)
    image.show()
