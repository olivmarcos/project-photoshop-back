import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", 'bmp'}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def execute(file):
    if not allowed_file(file.filename):
        return False
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return filename