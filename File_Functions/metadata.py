from PIL import Image

def read_image_metadata(image_path):
        with Image.open(image_path) as img:
            # Extract metadata from the image
            metadata = {
                "format": img.format,
                # Extract original datetime if available
                "datetime_original": img._getexif().get(36867) if img._getexif() else None,
            }
            return metadata

''' Example usage:
image_path = "path/to/your/image.jpg"
metadata = read_image_metadata(image_path) '''
