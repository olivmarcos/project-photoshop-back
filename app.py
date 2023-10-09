from flask import Flask, flash, request, jsonify, send_from_directory
from flask_cors import CORS

import upload_file_service
import apply_filter_service
import generate_histogram
import equalize_image

app = Flask(__name__)

UPLOADED_IMAGES_FOLDER = "uploaded_images"
app.config["UPLOADED_IMAGES_FOLDER"] = UPLOADED_IMAGES_FOLDER

FILTERED_IMAGES_FOLDER = "filtered_images"
app.config["FILTERED_IMAGES_FOLDER"] = FILTERED_IMAGES_FOLDER

IMAGES_HISTOGRAMS_FOLDER = "images_histograms"
app.config["IMAGES_HISTOGRAMS_FOLDER"] = IMAGES_HISTOGRAMS_FOLDER

EQUALIZED_IMAGES_FOLDER = "equalized_images"
app.config["EQUALIZED_IMAGES_FOLDER"] = EQUALIZED_IMAGES_FOLDER

allowed_origins = ["http://localhost:5173"]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/images/upload", methods=["POST"])
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

    return jsonify(
        {
            "message": "Generated image equalization succesfully",
            "data": {"fileName": file_name},
        }
    )


@app.route("/api/v1/images/uploaded/<file_name>", methods=["GET"])
def uploaded_file(file_name):
    return send_from_directory(app.config["UPLOADED_IMAGES_FOLDER"], file_name)


@app.route("/api/v1/images/filter", methods=["POST"])
def apply_negative_effect():
    data = request.get_json()

    filter_to_apply = data.get("filterToApply")
    file_name = data.get("fileName")
    gamma = data.get("gamma")
    aValue = data.get("aValue")
    bValue = data.get("bValue")
    second_image_name = data.get("secondFileName")
    scale_factor = data.get("scaleFactor")
    merge_percentage = data.get("mergePercentage")
    hiperboost = data.get("hiperboost")
    sobel = data.get("sobel")
    mask_size = data.get("maskSize")

    new_file = apply_filter_service.execute(
        filter_to_apply,
        file_name,
        second_image_name,
        gamma,
        aValue,
        bValue,
        scale_factor,
        merge_percentage,
        hiperboost,
        sobel,
        mask_size,
    )

    return jsonify(
        {
            "message": "filter applied successfully",
            "data": {"fileName": new_file},
        }
    )


@app.route("/api/v1/images/filtered/<file_name>", methods=["GET"])
def altered_file(file_name):
    return send_from_directory(app.config["FILTERED_IMAGES_FOLDER"], file_name)


@app.route("/api/v1/images/histogram", methods=["POST"])
def create_histogram():
    data = request.get_json()
    file_name = data.get("fileName")
    location = data.get("from")

    histogram_file_name = generate_histogram.execute(file_name, location)

    return jsonify(
        {
            "message": "Generated histogram succesfully",
            "data": {"fileName": histogram_file_name},
        }
    )


@app.route("/api/v1/images/histogram/<file_name>", methods=["GET"])
def get_histogram(file_name):
    return send_from_directory(app.config["IMAGES_HISTOGRAMS_FOLDER"], file_name)


@app.route("/api/v1/images/equalize", methods=["POST"])
def image_equalization():
    data = request.get_json()
    file_name = data.get("fileName")
    location = data.get("from")
    
    equalized_image = equalize_image.execute(file_name, location)

    return jsonify(
        {
            "message": "Generated image equalization succesfully",
            "data": {"fileName": equalized_image},
        }
    )


@app.route("/api/v1/images/equalized/<file_name>", methods=["GET"])
def get_equali(file_name):
    return send_from_directory(app.config["EQUALIZED_IMAGES_FOLDER"], file_name)


if __name__ == "__main__":
    app.run(debug=True)
