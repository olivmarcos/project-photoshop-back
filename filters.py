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

def expansion(image_name, aValue, bValue):
    image = getImage(image_name)
    copy = image.copy()
    # TO-DO
    return copy

def compression(image_name, aValue, bValue):
    image = getImage(image_name)
    copy = image.copy()
    # TO-DO
    return copy

def add_two_images(image_name, second_image_name, percentage):
    image = getImage(image_name)
    copy = image.copy()

    secondImage = getImage(second_image_name)
    secondCopy = secondImage.copy()
    # TO-DO
    return copy

def nearest_neighbor_resampling(image_name, enlargement_factor):
    original_image = getImage(image_name)
    original_width = original_image.size[0]
    original_heigth = original_image.size[1]

    new_width = original_width * enlargement_factor
    new_heigth = original_heigth * enlargement_factor

    new_size = (new_width, new_heigth)

    elarged_image = Image.new('L', new_size)

    for i in range(0, elarged_image.size[0] - 1):
        for j in range(0, elarged_image.size[1] - 1):
            original_i = i // enlargement_factor
            original_j = j // enlargement_factor

            original_pixel = original_image.getpixel((original_i, original_j))
            elarged_image.putpixel((i, j), original_pixel)

    return elarged_image