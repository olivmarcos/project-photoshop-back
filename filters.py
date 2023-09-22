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


# caso queira botar uma area para o usuario informar o valor da contante,me informe que eu ajusto, o Sergio achoq ue disse que o valor padrão era 105.886  mas vou confirmar com ele hj
# eu tbm n sei acho que vai precisar importar o numpy pra mexer com contas eu n sei se vc tem ele . . .  deve ter . . .
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


def invLogarithm(image_name):
    image = getImage(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            exp = original_pixel / 105.886
            output_pixel = int(np.power(10, exp))
            copy.putpixel((i, j), output_pixel)

    return copy


def power(image_name, gamma):
    image = getImage(image_name)
    copy = image.copy()
    exponent = gamma
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.power(((original_pixel + 1) / 256), exponent) * 256)
            copy.putpixel((i, j), output_pixel)

    return copy


def root(image_name, gamma):
    image = getImage(image_name)
    copy = image.copy()
    index = gamma
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(
                np.power(((original_pixel + 1) / 256), (1 / index)) * 256
            )
            copy.putpixel((i, j), output_pixel)

    return copy


def rotation_ninety_degree(image_name, gamma):
    image = getImage(image_name)
    copy = image.copy()
    # TO-DO
    return copy


def rotation_counterclockwise_ninety_degree(image_name, gamma):
    image = getImage(image_name)
    copy = image.copy()
    # TO-DO
    return copy


def rotation_one_hundred_eighty(image_name, gamma):
    image = getImage(image_name)
    copy = image.copy()
    # TO-DO
    return copy
