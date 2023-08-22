import os
from main import download_image, check_extension
import requests
from dotenv import load_dotenv

from urllib.parse import urlsplit
from pathlib import Path


def fetch_nasa_apod():
    params = {'count' : 40}
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'
    response = requests.get(url,params=params)
    response.raise_for_status()
    photos = response.json()
    nasa_urls = []
    for photo in photos:
        photo_url = photo['url']
        nasa_urls.append(photo_url)
    for count, photo in enumerate(nasa_urls, start=1):
        filename = f'nasa_apod_{count}'
        download_image(photo, filename)


def main():
    fetch_nasa_apod()


if __name__ == '__main__':
    main()