import os
import requests
from dotenv import load_dotenv

from urllib.parse import urlsplit
from pathlib import Path


def download_image(photo,filename):
    Path('images').mkdir(parents=True, exist_ok=True)
    extension = check_extension(photo)
    response = requests.get(photo)
    response.raise_for_status()
    if extension:
        with open(f'images/{filename}{extension}', 'wb') as file:
            file.write(response.content)


def check_extension(photo):
    split_result = urlsplit(photo)
    path = os.path.splitext(split_result.path)
    extension = path[1]
    return extension