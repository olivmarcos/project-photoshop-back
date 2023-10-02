from PIL import Image

UPLOAD_FOLDER = "./uploads"


def get_image(image_name: str) -> Image:
    if not image_name:
        return False

    image = Image.open(UPLOAD_FOLDER + "/" + image_name)
    if image.mode != "L":
        image = image.convert("L")

    return image


def get_pixel_at(image: Image, i, j) -> int:
    if not image:
        return

    return image.getpixel((i, j))


def put_pixel_at(image: Image, i: int, j: int) -> None:
    if not image:
        return

    return image.putpixel((i, j))


def get_image_histogram(image: Image) -> list:
    if not image:
        return False

    return image.histogram()
