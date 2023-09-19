import os
from flask import Flask, flash, request, jsonify, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from uploadFileAction import *

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

allowed_origins = ["http://localhost:5173"]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("no file part")
        return jsonify({"error": "no file part"})

    file = request.files["file"]
    if file.filename == "":
        flash("no selected file")
        return jsonify({"eror": "no selected file"})

    uploaded_file = execute(file)
    if not uploaded_file:
        return jsonify({"error": "Invalid file format"})
    
    return jsonify(
            {"message": "File uploaded successfully", "image_url": uploaded_file}
        )


@app.route("/api/v1/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    app.run(debug=True)
