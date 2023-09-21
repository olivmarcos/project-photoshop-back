import numpy as np
from PIL import Image

UPLOAD_FOLDER = "./uploads"


def getImage(image_name):
    return Image.open(UPLOAD_FOLDER + "/" + image_name).convert("L")


def negative(image_name):
    image = getImage(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = 255 - original_pixel
            copy.putpixel((i, j), output_pixel)

    return copy

#caso queira botar uma area para o usuario informar o valor da contante,me informe que eu ajusto, o Sergio achoq ue disse que o valor padrão era 105.886  mas vou confirmar com ele hj
#eu tbm n sei acho que vai precisar importar o numpy pra mexer com contas eu n sei se vc tem ele . . .  deve ter . . .
def logarithm(image_name): 
    image = getImage(image_name)
    c = 255 / np.log(256)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(c * np.log(1 + original_pixel))
            copy.putpixel((i, j), output_pixel)
    
    return copy

#Daqui pra baixo esta em modo de teste
def invLogarithm(image_name):
    image = getImage(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            exp = original_pixel/105.886
            output_pixel = int(np.power(10,exp))
            copy.putpixel((i, j), output_pixel)
    
    return copy

def pow(image_name): #add o expoente ,exp
    image = getImage(image_name)
    copy = image.copy()
    exp = 2 #remover
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.power(((original_pixel+1)/256),exp)*256)
            copy.putpixel((i, j), output_pixel)
   
    return copy

def root(image_name): #add o indice ,indice
    image = getImage(image_name)
    copy = image.copy()
    indice = 2 #remover
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.power(((original_pixel+1)/256),(1/indice))*256)
            copy.putpixel((i, j), output_pixel)

    return copy