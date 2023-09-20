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
