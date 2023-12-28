import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_metadata(file_path):
    image = Image.open(file_path)
    image_exif = image._getexif()
    return {TAGS[k]: v for k, v in image_exif.items() if k in TAGS}
