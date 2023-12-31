import os
import filters

FILTERED_IMAGES_FOLDER = "./filtered_images"

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
    "nearest-neighbor-resampling",
    "bilinear-interpolation-resampling",
    "mean",
    "mode",
    "median",
    "horizontal-mirroring",
    "vertical-mirroring",
    "laplace",
    "prewitt_sobel",
    "min",
    "max"
]


def allowed_filters(filter):
    return filter in ALLOWED_FILTERS

def execute(
    filter,
    image_name,
    second_image_name,
    gamma,
    aValue,
    bValue,
    scale_factor,
    merge_percentage,
    hiperboost: bool,
    sobel: bool,
    mask_size
):
    if not filter or not image_name:
        return False

    if not allowed_filters(filter):
        return False

    if filter == "negative":
        new_image = filters.negative(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "logarithm":
        new_image = filters.logarithm(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "inverse-logarithm":
        new_image = filters.invLogarithm(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "power":
        new_image = filters.power(image_name, gamma)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "root":
        new_image = filters.root(image_name, gamma)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "rotation-ninety-degree":
        new_image = filters.rotation_ninety_degree(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "rotation-counterclockwise-ninety-degree":
        new_image = filters.rotation_counterclockwise_ninety_degree(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "rotation-one-hundred-eighty":
        new_image = filters.rotation_one_hundred_eighty(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "horizontal-mirroring":
        new_image = filters.horizontal_mirroring(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "vertical-mirroring":
        new_image = filters.vertical_mirroring(image_name)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "expansion":
        new_image = filters.expansion(image_name, aValue, bValue)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "compression":
        new_image = filters.compression(image_name, aValue, bValue)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "add-two-images":       
        new_image = filters.add_two_images(
            image_name, second_image_name, merge_percentage
        )
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "nearest-neighbor-resampling":
        new_image = filters.nearest_neighbor_resampling(image_name, scale_factor)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "bilinear-interpolation-resampling":
        new_image = filters.bilinear_interpolation_resampling(image_name, scale_factor)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "mean":
        new_image = filters.mean(image_name, mask_size)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "median":
        new_image = filters.median(image_name, mask_size)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "mode":
        new_image = filters.mode(image_name, mask_size)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "laplace":
        new_image = filters.laplace(image_name, hiperboost)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "prewitt_sobel":
        new_image = filters.prewitt_sobel(image_name, sobel)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

        
    if filter == "min":
        new_image = filters.min_filter(image_name, mask_size)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    if filter == "min":
        new_image = filters.max_filter(image_name, mask_size)
        new_image.save(os.path.join(FILTERED_IMAGES_FOLDER, image_name))

    return image_name