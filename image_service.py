from PIL import Image
import numpy as np

UPLOADED_IMAGES_FOLDER = "uploaded_images"


def get_image(image_name: str, location: str = UPLOADED_IMAGES_FOLDER) -> Image:
    if not image_name:
        return False
    
    if location:
        print(location)

    image = Image.open(location + "/" + image_name)

    if image.mode != "L":
        image = image.convert("L")

    return image


def create_from_array(image_values: list, mode: str) -> Image:
    return Image.fromarray(image_values, mode)


def get_image_histogram(image: Image) -> list:
    if not image:
        return False

    height = image.size[0] - 1
    width = image.size[1] - 1

    histogram = np.zeros([256], np.int32)

    for x in range(0, height):
        for y in range(0, width):
            histogram[image.getpixel((y, x))] += 1

    return histogram
