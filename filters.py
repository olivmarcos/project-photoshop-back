import numpy as np
from PIL import Image
import image_service

UPLOAD_FOLDER = "./uploads"

def negative(image_name):
    image = image_service.get_image(image_name)
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
    image = image_service.get_image(image_name)
    c = 255 / np.log(256)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(c * np.log(1 + original_pixel))
            copy.putpixel((i, j), output_pixel)

    return copy


def invLogarithm(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            exp = original_pixel / 105.886
            output_pixel = int(np.power(10, exp))
            copy.putpixel((i, j), output_pixel)

    return copy


def power(image_name, gamma):
    image = image_service.get_image(image_name)
    copy = image.copy()
    exponent = gamma
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.power(((original_pixel + 1) / 256), exponent) * 256)
            copy.putpixel((i, j), output_pixel)

    return copy


def root(image_name, gamma):
    image = image_service.get_image(image_name)
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


def rotation_ninety_degree(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            output_pixel = image.getpixel((image.size[1] - 1 - j, i))
            copy.putpixel((i, j), output_pixel)

    return copy


def rotation_counterclockwise_ninety_degree(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            output_pixel = image.getpixel((j, image.size[0] - 1 - i))
            copy.putpixel((i, j), output_pixel)

    return copy


def rotation_one_hundred_eighty(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()
    
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            output_pixel = image.getpixel((image.size[0] - 1 - i, image.size[1] - 1 - j))
            copy.putpixel((i, j), output_pixel)

    return copy


def horizontal_mirroring(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()
    
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            output_pixel = image.getpixel((image.size[0] - 1 - i, j))
            copy.putpixel((i, j), output_pixel)

    return copy


def vertical_mirroring(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()
    
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            output_pixel = image.getpixel((i, image.size[1] - 1 - j))
            copy.putpixel((i, j), output_pixel)

    return copy

def expansion(image_name, aValue, bValue):
    image = image_service.get_image(image_name)
    copy = image.copy()
    a = aValue
    b = bValue

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(a * original_pixel + b)
            copy.putpixel((i, j), output_pixel)

    return copy

def compression(image_name, aValue, bValue):
    image = image_service.get_image(image_name)
    copy = image.copy()
    a = aValue
    b = bValue

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = int((original_pixel / a) - b)
            copy.putpixel((i, j), output_pixel)

    return copy

def add_two_images(image_name, second_image_name, gamma): #trocar o gamma por percentage
    image = image_service.get_image(image_name)
    copy = image.copy()

    secondImage = image_service.get_image(second_image_name)
    #secondCopy = secondImage.copy()

    a = gamma
    b = 100 - gamma

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            percentage_original_pixel =        int(a * (image.getpixel((i, j)) / 100))
            percentage_second_original_pixel = int(b * (secondImage.getpixel((i, j)) / 100))
            output_pixel = int(percentage_original_pixel + percentage_second_original_pixel)
            copy.putpixel((i, j), output_pixel)
            
    return copy


def nearest_neighbor_resampling(image_name, scale_factor):
    original_image = image_service.get_image(image_name)
    original_width = original_image.size[0]
    original_height = original_image.size[1]

    new_width = original_width * scale_factor
    new_heigth = original_height * scale_factor

    new_size = (new_width, new_heigth)

    elarged_image = Image.new("L", new_size)

    for i in range(0, elarged_image.size[0] - 1):
        for j in range(0, elarged_image.size[1] - 1):
            original_i = i // scale_factor
            original_j = j // scale_factor

            original_pixel = original_image.getpixel((original_i, original_j))
            elarged_image.putpixel((i, j), original_pixel)

    return elarged_image


def bilinear_interpolation_resampling(image_name, scale_factor):
    original_image = image_service.get_image(image_name)
    original_width = original_image.size[0]
    original_height = original_image.size[1]

    new_width = original_width * scale_factor
    new_heigth = original_height * scale_factor
    new_size = (new_width, new_heigth)

    elarged_image = Image.new("L", new_size)

    width_scale = float(original_width - 1) / (new_width - 1)
    height_scale = float(original_height - 1) / (new_heigth - 1)

    for i in range(0, elarged_image.size[0] - 1):
        for j in range(0, elarged_image.size[1] - 1):
            row = i * width_scale
            col = j * height_scale

            row_1 = int(row)
            row_2 = min(int(row) + 1, original_width - 1)
            col_1 = int(col)
            col_2 = min(int(col) + 1, original_height - 1)

            value_1 = (col_2 - col) * original_image.getpixel((row_1, col_1)) + (
                col - col_1
            ) * original_image.getpixel((row_1, col_2))

            value_2 = (col_2 - col) * original_image.getpixel((row_2, col_1)) + (
                col - col_1
            ) * original_image.getpixel((row_2, col_2))

            interpolated_value = int((row_2 - row) * value_1 + (row - row_1) * value_2)
            elarged_image.putpixel((i, j), interpolated_value)

    return elarged_image

def average(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

#    for i in range(0, image.size[0]):
#        for j in range(0, image.size[1]):
#            if i == 0:
#                if j == 0:
#                    sum = image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
#                    mode = 4
#                    print("superior esquerdo")
#
#                elif j == image.size[1] - 1:
#                    sum = image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1))
#                    mode = 4
#                    print("superior direito")
#
#                else:
#                    sum = image.getpixel((i, j - 1)) + image.getpixel((i, j)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j - 1)) + image.getpixel((i + 1, j)) + image.getpixel((i + 1, j + 1))
#                    mode = 6
#                    print("superior")
#            
#            elif i == image.size[0] - 1:
#                if j == 0:
#                    sum = image.getpixel((i, j)) + image.getpixel((i - 1, j)) + image.getpixel((i, j + 1)) + image.getpixel((i - 1, j + 1))
#                    mode = 4
#                    print("inferior esquerdo")
#
#                elif j == image.size[1] - 1:
#                    sum = image.getpixel((i, j)) + image.getpixel((i - 1, j)) + image.getpixel((i, j - 1)) + image.getpixel((i - 1, j - 1))
#                    mode = 4
#                    print("inferior direito")
#
#                else:
#                    sum = image.getpixel((i, j - 1)) + image.getpixel((i, j)) + image.getpixel((i, j + 1)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i - 1, j)) + image.getpixel((i - 1, j + 1))
#                    mode = 6
#                    print("inferior")
#            
#            elif j == 0:
#                sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j + 1)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
#                mode = 6
#                print("esquerdo")
#
#            elif j == image.size[1] - 1:
#                sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1))
#                mode = 6
#                print("direito")
#
#            else: 
#                sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1)) + image.getpixel((i - 1, j + 1)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
#                mode = 9
    
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):        
            mask = mask_intern(image, i,j)
            sum = mask[0]
            mode = mask[1]
            avg = sum/mode
            output_pixel = int(np.round(avg))
            copy.putpixel((i, j), output_pixel)
    return copy

def mask_intern(image, i, j):

#    for i in range(0, image.size[0]):
#        for j in range(0, image.size[1]):
    if i == 0:
        if j == 0:
            sum = image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
            mode = 4
            print("superior esquerdo")
        elif j == image.size[1] - 1:
            sum = image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1))
            mode = 4
            print("superior direito")
        else:
            sum = image.getpixel((i, j - 1)) + image.getpixel((i, j)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j - 1)) + image.getpixel((i + 1, j)) + image.getpixel((i + 1, j + 1))
            mode = 6
            print("superior")
    
    elif i == image.size[0] - 1:
        if j == 0:
            sum = image.getpixel((i, j)) + image.getpixel((i - 1, j)) + image.getpixel((i, j + 1)) + image.getpixel((i - 1, j + 1))
            mode = 4
            print("inferior esquerdo")
        elif j == image.size[1] - 1:
            sum = image.getpixel((i, j)) + image.getpixel((i - 1, j)) + image.getpixel((i, j - 1)) + image.getpixel((i - 1, j - 1))
            mode = 4
            print("inferior direito")
        else:
            sum = image.getpixel((i, j - 1)) + image.getpixel((i, j)) + image.getpixel((i, j + 1)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i - 1, j)) + image.getpixel((i - 1, j + 1))
            mode = 6
            print("inferior")
    
    elif j == 0:
        sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j + 1)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
        mode = 6
        print("esquerdo")
    elif j == image.size[1] - 1:
        sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1))
        mode = 6
        print("direito")
    else: 
        sum = image.getpixel((i - 1, j)) + image.getpixel((i, j)) + image.getpixel((i + 1, j)) + image.getpixel((i - 1, j - 1)) + image.getpixel((i, j - 1)) + image.getpixel((i + 1, j - 1)) + image.getpixel((i - 1, j + 1)) + image.getpixel((i, j + 1)) + image.getpixel((i + 1, j + 1))
        mode = 9
    
    return [sum, mode]
    

