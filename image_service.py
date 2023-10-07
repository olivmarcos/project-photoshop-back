from PIL import Image
import numpy as np

UPLOAD_FOLDER = "./uploads"


def get_image(image_name: str) -> Image:
    if not image_name:
        return False

    image = Image.open(UPLOAD_FOLDER + "/" + image_name)

    if image.mode != "L":
        image = image.convert("L")

    return image

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
