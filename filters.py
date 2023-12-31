import numpy as np
from PIL import Image
import image_service


def negative(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            original_pixel = image.getpixel((i, j))
            output_pixel = 255 - original_pixel
            copy.putpixel((i, j), output_pixel)

    return copy


def logarithm(image_name):
    image = image_service.get_image(image_name)
    c = 255 / np.log(256)
    copy = image.copy()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.round(c * np.log(1 + original_pixel)))
            copy.putpixel((i, j), output_pixel)

    return copy


def invLogarithm(image_name):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            exp = original_pixel / 105.886
            output_pixel = int(np.round(np.power(10, exp)))
            copy.putpixel((i, j), output_pixel)

    return copy


def power(image_name, gamma):
    image = image_service.get_image(image_name)
    copy = image.copy()
    exponent = gamma
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(
                np.round(np.power(((original_pixel + 1) / 256), exponent) * 256)
            )
            copy.putpixel((i, j), output_pixel)

    return copy


def root(image_name, gamma):
    image = image_service.get_image(image_name)
    copy = image.copy()
    index = gamma
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(
                np.round(np.power(((original_pixel + 1) / 256), (1 / index)) * 256)
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
            output_pixel = image.getpixel(
                (image.size[0] - 1 - i, image.size[1] - 1 - j)
            )
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

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.round(a * original_pixel + b))
            copy.putpixel((i, j), output_pixel)

    return copy


def compression(image_name, aValue, bValue):
    image = image_service.get_image(image_name)
    copy = image.copy()
    a = aValue
    b = bValue

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            original_pixel = image.getpixel((i, j))
            output_pixel = int(np.round((original_pixel / a) - b))
            copy.putpixel((i, j), output_pixel)

    return copy


def add_two_images(image_name: str, second_image_name: str, merge_percentage=int):
    image = image_service.get_image(image_name)
    copy = image.copy()

    secondImage = image_service.get_image(second_image_name)
    # secondCopy = secondImage.copy()

    a = merge_percentage
    b = 100 - merge_percentage

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            percentage_original_pixel = int(a * (image.getpixel((i, j)) / 100))
            percentage_second_original_pixel = int(
                b * (secondImage.getpixel((i, j)) / 100)
            )
            output_pixel = int(
                np.round(percentage_original_pixel + percentage_second_original_pixel)
            )
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


def mask_intern(image, i, j, mask_size):
    tam = mask_size
    pixels = []
    iteracoes = 0
    delta_center = int((tam - 1) / 2)

    if (i + delta_center + 1) > image.size[0] - 1:
        loopXMax = image.size[0] - 1
    else:
        loopXMax = i + delta_center + 1

    if (i - delta_center) < 0:
        loopXMin = 0
    else:
        loopXMin = i - delta_center

    if (j + delta_center + 1) > image.size[0] - 1:
        loopYMax = image.size[1] - 1
    else:
        loopYMax = j + delta_center + 1

    if (j - delta_center) < 0:
        loopYMin = 0
    else:
        loopYMin = j - delta_center

    if i == 0:
        if j == 0:
            for x in range(i, loopXMax):
                for y in range(j, loopYMax):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

        elif j == image.size[1] - 1:
            for x in range(i, loopXMax):
                for y in range(loopYMin, j + 1):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

        else:
            for x in range(i, loopXMax):
                for y in range(loopYMin, loopYMax):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

    elif i == image.size[0] - 1:
        if j == 0:
            for x in range(loopXMin, i + 1):
                for y in range(j, loopYMax):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

        elif j == image.size[1] - 1:
            for x in range(loopXMin, i + 1):
                for y in range(loopYMin, j + 1):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

        else:
            for x in range(loopXMin, i + 1):
                for y in range(loopYMin, loopYMax):
                    iteracoes = iteracoes + 1
                    pixels.append(image.getpixel((x, y)))

    elif j == 0:
        for x in range(loopXMin, loopXMax):
            for y in range(j, loopYMax):
                iteracoes = iteracoes + 1
                pixels.append(image.getpixel((x, y)))

    elif j == image.size[1] - 1:
        for x in range(loopXMin, loopXMax):
            for y in range(loopYMin, j + 1):
                iteracoes = iteracoes + 1
                pixels.append(image.getpixel((x, y)))

    else:
        for x in range(loopXMin, loopXMax):
            for y in range(loopYMin, loopYMax):
                iteracoes = iteracoes + 1
                pixels.append(image.getpixel((x, y)))

    mode = iteracoes
    return [pixels, mode]


def laplace(image_name: str, hiperboost: bool):
    image = image_service.get_image(image_name)
    copy = image.copy()
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, 3)

            sum = np.sum(mask[0]) - image.getpixel((i, j))
            mode = 8
            if hiperboost is True:
                mode = mode + 1

            output_pixel = int((mode * image.getpixel((i, j))) - sum)
            if (
                (i == 0)
                or (j == 0)
                or (i == image.size[0] - 1)
                or (j == image.size[1] - 1)
            ):
                output_pixel = 0

            copy.putpixel((i, j), output_pixel)
    return copy


def prewitt_sobel(image_name: str, sobel: bool):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            if (
                (i == 0)
                or (j == 0)
                or (i == image.size[0] - 1)
                or (j == image.size[1] - 1)
            ):
                output_pixel = 0
            else:
                horizontal_negativo = (
                    image.getpixel((i - 1, j - 1))
                    + image.getpixel((i, j - 1))
                    + image.getpixel((i + 1, j - 1))
                )
                horizontal_positivo = (
                    image.getpixel((i - 1, j + 1))
                    + image.getpixel((i, j + 1))
                    + image.getpixel((i + 1, j + 1))
                )

                vertical_negativo = (
                    image.getpixel((i - 1, j - 1))
                    + image.getpixel((i - 1, j))
                    + image.getpixel((i - 1, j + 1))
                )
                vertical_positivo = (
                    image.getpixel((i + 1, j - 1))
                    + image.getpixel((i + 1, j))
                    + image.getpixel((i + 1, j + 1))
                )

                if sobel is True:
                    horizontal_negativo = horizontal_negativo + image.getpixel(
                        (i, j - 1)
                    )
                    horizontal_positivo = horizontal_positivo + image.getpixel(
                        (i, j + 1)
                    )
                    vertical_negativo = vertical_negativo + image.getpixel((i - 1, j))
                    vertical_positivo = vertical_positivo + image.getpixel((i + 1, j))

                output_pixel = abs(horizontal_positivo - horizontal_negativo) + abs(
                    vertical_positivo - vertical_negativo
                )

            copy.putpixel((i, j), output_pixel)
    return copy


def max_filter(image_name, mask_size):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, mask_size)
            selected_pixels = mask[0]
            max_value = selected_pixels[0]

            for x in selected_pixels:
                if x > max_value:
                    max_value = x

            output_pixel = max_value
            copy.putpixel((i, j), output_pixel)

    return copy


def min_filter(image_name, mask_size):
    image = image_service.get_image(image_name)
    copy = image.copy()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, mask_size)
            selected_pixels = mask[0]
            min_value = selected_pixels[0]

            for x in selected_pixels:
                if x < min_value:
                    min_value = x

            output_pixel = min_value
            copy.putpixel((i, j), output_pixel)

    return copy


def mean(image_name, mask_size):
    image = image_service.get_image(image_name)
    copy = image.copy()
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, mask_size)
            sum = np.sum(mask[0])
            mode = mask[1]
            avg = sum / mode
            output_pixel = int(np.round(avg))
            copy.putpixel((i, j), output_pixel)
    return copy


def mode(image_name, mask_size):
    image = image_service.get_image(image_name)
    copy = image.copy()
    
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, mask_size)
            selected_pixels = mask[0]
            modes = find_mode(selected_pixels)
            output_pixel = modes[0]

            if len(modes) > 1:
                output_pixel = get_the_closest_mode_by_given_value(
                    modes, image.getpixel((i, j))
                )

            copy.putpixel((i, j), output_pixel)
    return copy


def find_mode(data):
    num_count = {}

    for num in data:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    max_count = max(num_count.values())

    modes = [num for num, count in num_count.items() if count == max_count]

    return modes


def get_the_closest_mode_by_given_value(modes, target_value):
    differences = [abs(mode - target_value) for mode in modes]
    min_difference = min(differences)

    closest_modes = [
        mode for mode, diff in zip(modes, differences) if diff == min_difference
    ]
    chosen_mode = max(closest_modes)

    return chosen_mode


def median(image_name, mask_size):
    image = image_service.get_image(image_name)
    copy = image.copy()
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            mask = mask_intern(image, i, j, mask_size)
            selected_pixels = mask[0]
            median_pixel = calculate_median(selected_pixels)
            output_pixel = int(np.round(median_pixel))
            copy.putpixel((i, j), output_pixel)
    return copy


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)

    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]

    return median
