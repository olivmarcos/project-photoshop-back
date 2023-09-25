import os
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
    "compression"
]


def allowed_filter(filter):
    return filter in ALLOWED_FILTERS


def execute(filter, image_name, gamma):#add ", constant"
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
        new_image = filters.expansion(image_name, gamma) #add ", constant"
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "compression":
        new_image = filters.compression(image_name, gamma) #add ", constant"
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))
 

    return image_name
