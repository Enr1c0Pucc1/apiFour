import os
from main import download_image, check_extension
import requests
from dotenv import load_dotenv

from urllib.parse import urlsplit
from pathlib import Path


def fetch_nasa_apod():
    params = {'count' : 40}
    url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'
    response = requests.get(url,params=params)
    response.raise_for_status()
    photos = response.json()
    nasa_urls = []
    for photo in photos:
        photo_url = photo['url']
        nasa_urls.append(photo_url)
    return nasa_urls


def download_nasa_apods(urls):
    for count, photo in enumerate(urls, start=1):
        filename = f'nasa_apod_{count}'
        download_image(photo, filename)


def fetch_nasa():
    load_dotenv()
    Path('images').mkdir(parents=True, exist_ok=True)
    nasa_api_key = os.environ['NASA_API_KEY']
    photo_urls = fetch_nasa_apod()
    download_nasa_apods(photo_urls)


if __name__ == '__main__':
    fetch_nasa()