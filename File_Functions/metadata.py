from PIL import Image

def read_image_metadata(image_path):
        with Image.open(image_path) as img:
            metadata = {
                "format": img.format,
                "datetime_original": img._getexif().get(36867) if img._getexif() else None,
            
            }

            return metadata

'''
Example usage:
image_path = "path/to/your/image.jpg"
metadata = read_image_metadata(image_path) 

'''
