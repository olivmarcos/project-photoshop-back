import os
from filters import negative, logarithm

ALTERED_FOLDER = "./altered"
ALLOWED_FILTERS = ['negative', 'logarithm', 'inverse-logarithm', 'power', 'root']

def allowed_filter(filter):
    return filter in ALLOWED_FILTERS

def execute(filter, image_name):
    if not filter or not image_name:
        return False
    
    if not allowed_filter(filter):
        return False

    if filter == "negative":
        new_image = negative(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))


    if filter == "logarithm":
        new_image = logarithm(image_name)
        new_image.save(os.path.join(ALTERED_FOLDER, image_name))

    if filter == "inverse-logarithm":
        new_image = logarithm(image_name)
        # TO-DO

    if filter == "power":
        new_image = logarithm(image_name)
        # TO-DO

    if filter == "root":
        new_image = logarithm(image_name)
        # TO-DO
        
    return image_name
