from email.mime import image
import os
from unittest import findTestCases
import filters

ALTERED_FOLDER = "./altered"

ALLOWED_FILTERS = [
    "negative",
    "logarithm",
    "inverse-logarithm",
    "power",
    "root",
    "rotation-ninety-degree",
    "rotation-counterclockwise-ninety-degree",
    "rotation-one-hundred-eighty",
    "expansion",
    "compression",
    "add-two-images",
    "nearest-neighbor-resampling"
]


def allowed_filter(filter):
    return filter in ALLOWED_FILTERS


def execute(filter, image_name, second_image_name, gamma, aValue, bValue, enlargement_factor):
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

    if filter == "rotation-ninety-degree":
        new_image = filters.rotation_ninety_degree(image_name, gamma)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "rotation-counterclockwise-ninety-degree":
        new_image = filters.rotation_counterclockwise_ninety_degree(image_name, gamma)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "rotation-one-hundred-eighty":
        new_image = filters.root(image_name, gamma)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "expansion":
        new_image = filters.expansion(image_name, aValue, bValue)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "compression":
        new_image = filters.compression(image_name, aValue, bValue)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "add-two-images":
        percentage = 25
        new_image = filters.add_two_images(image_name, second_image_name, percentage)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == 'nearest-neighbor-resampling':
        new_image = filters.nearest_neighbor_resampling(image_name, enlargement_factor)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    return image_name
