import os
from filters import negative, logarithm

ALTERED_FOLDER = "./altered"


def execute(filter, image_name):
    if not filter or not image_name:
        return False

    if filter == "negative":
        new_image = negative(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))


    if filter == "logarithm":
        new_image = logarithm(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    return image_name
