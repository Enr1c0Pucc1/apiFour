import os
from help_functions import download_image
import requests
from dotenv import load_dotenv


def fetch_nasa_apod(api_key):
    download_count = 40
    params = {'count' : download_count, 'api_key' : api_key}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url,params=params)
    response.raise_for_status()
    photos = response.json()
    for count, photo in enumerate(photos, start=1):
        photo_url = photo['url']
        filename = f'nasa_apod_{count}'
        download_image(photo_url, filename)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(nasa_api_key)