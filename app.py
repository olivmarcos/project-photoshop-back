from flask import Flask, flash, request, jsonify, send_from_directory
from flask_cors import CORS

import upload_file_service
import apply_filter_service

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALTERED_FOLDER = "altered"
app.config["ALTERED_FOLDER"] = ALTERED_FOLDER

allowed_origins = ["http://localhost:5173"]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})


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

    file_name = upload_file_service.execute(file)
    if not file_name:
        return jsonify({"error": "Invalid file format"})

    return jsonify({"message": "File uploaded successfully", "file_name": file_name})


@app.route("/api/v1/filter", methods=["POST"])
def apply_negative_effect():
    data = request.get_json()

    filter_to_apply = data.get("filterToApply")
    file_name = data.get("fileName")
    gamma = data.get("gamma")
    aValue = data.get("aValue")
    bValue = data.get("bValue")
    second_image_name = data.get("secondFileName")
    scale_factor = data.get("scaleFactor")

    new_file = apply_filter_service.execute(
        filter_to_apply,
        file_name,
        second_image_name,
        gamma,
        aValue,
        bValue,
        scale_factor,
    )

    return jsonify({"message": "File altered successfully", "file_name": new_file})


@app.route("/api/v1/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/api/v1/altered/<filename>")
def altered_file(filename):
    return send_from_directory(app.config["ALTERED_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
