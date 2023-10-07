import os
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOADED_IMAGES_FOLDER = "./uploaded_images"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", 'bmp'}

def allowed_file(file_name: str) -> bool:
    return "." in file_name and file_name.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def execute(file) -> str | bool:
    if not allowed_file(file.filename):
        return False
    
    file_name = secure_filename(file.filename)
    current_dateTime = datetime.now()
    file_name = str(current_dateTime.microsecond) + "_" + file_name
    file.save(os.path.join(UPLOADED_IMAGES_FOLDER, file_name))

    return file_name