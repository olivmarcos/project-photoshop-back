import os
import numpy as np
from datetime import datetime
import image_service

EQUALIZED_IMAGES_FOLDER = './equalized_images'

def execute(image_name: str, location: str = None) -> None:
    if not image_name:
        return False
    
    image = image_service.get_image(image_name, location)

    histogram = image_service.get_image_histogram(image)

    normalized_histogram = histogram / np.sum(histogram)

    cdf = np.cumsum(normalized_histogram)

    equalized_img = cdf[image] * 255
    equalized_img = equalized_img.astype(np.uint8)
    equalized_img = image_service.create_from_array(equalized_img, 'L')

    current_dateTime = datetime.now()
    image_name_parts = image_name.split('_')
    image_name = str(current_dateTime.microsecond) + "_" + image_name_parts[1]
    
    equalized_img.save(os.path.join(EQUALIZED_IMAGES_FOLDER, image_name))

    return image_name