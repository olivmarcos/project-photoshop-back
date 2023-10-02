import image_service
import plot_image_service

def execute(image_name: str) -> str:
    if not image_name:
        return False
        
    image = image_service.get_image(image_name)
    histogram = image_service.get_image_histogram(image)
    histogram_file_name = plot_image_service.execute(image_name, histogram)
    return histogram_file_name