import matplotlib.pyplot as plt
import os


HISTOGRAMS_FOLDER = "./histograms"


def execute(image_name: str, histogram: list) -> str:
    pixel_values = list(range(256))

    plt.clf()
    plt.bar(pixel_values, histogram[:256], width=1.0, color="gray")
    plt.xlabel("Valor do pixel")
    plt.ylabel("Frequência")
    plt.title("Histograma - Imagens em escala de cinza")

    file_name = os.path.splitext(image_name)[0] + ".png"
    plt.savefig(HISTOGRAMS_FOLDER + "/" + file_name)

    return file_name
