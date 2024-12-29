import json
import os
from PIL import Image
import numpy as np
import re
import pkg_resources

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '../data')
DATA_JSON = os.path.join(DATABASE, 'thivien_nomfoundation.json')
IMAGE_DIR = os.path.join(DATABASE, 'hvthivien_images')

json_database = None

def load_database():
    global json_database
    json_database = {}
    data_file = pkg_resources.resource_filename(__name__, '../data/thivien_nomfoundation.json')
    with open(data_file, 'r') as f:
        db = json.load(f)
    for item in db:
        json_database[item['chinese_character']] = item

def get_image(image_path: str) -> np.ndarray:
    image_path = re.sub(r'/', '_', image_path)
    image_path = os.path.join(IMAGE_DIR, image_path)
    img_path = pkg_resources.resource_filename(__name__, '../data/hvthivien_images/' + image_path)
    img = Image.open(image_path)
    return np.array(img)

def get_field(chinese_character, field: str) -> str:
    if chinese_character in json_database:
        return json_database[chinese_character].get(field, None)
    return None
