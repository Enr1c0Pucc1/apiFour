import os
from help_functions import download_image
import requests
from dotenv import load_dotenv


def fetch_nasa_apod(api_key):
    params = {'count' : 40, 'api_key' : api_key}
    url = 'https://api.nasa.gov/planetary/apod'
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


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(nasa_api_key)