import os
import filters

ALTERED_FOLDER = "./altered"
ALLOWED_FILTERS = ["negative", "logarithm", "inverse-logarithm", "power", "root"]


def allowed_filter(filter):
    return filter in ALLOWED_FILTERS


def execute(filter, image_name, gamma):
    if not filter or not image_name:
        return False

    if not allowed_filter(filter):
        return False

    if not gamma:
        return False

    if filter == "negative":
        new_image = filters.negative(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "logarithm":
        new_image = filters.logarithm(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "invLogarithm":
        new_image = filters.invLogarithm(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "power":
        new_image = filters.power(image_name, gamma)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "root":
        new_image = filters.root(image_name, gamma)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    return image_name
