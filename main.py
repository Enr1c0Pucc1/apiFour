import os
import requests
from dotenv import load_dotenv

from urllib.parse import urlsplit
from pathlib import Path


def download_image(photo,filename):
    extension = check_extension(photo)
    response = requests.get(photo)
    response.raise_for_status()
    if extension != '':
        with open(f'images/{filename}{extension}', 'wb') as file:
            file.write(response.content)

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    for count, photo in enumerate(photos, start=1):
        filename = f'spacex_{count}'
        download_image(photo, filename)


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
    

def check_extension(photo):
    split_result = urlsplit(photo)
    path = os.path.splitext(split_result.path)
    extension = path[1]
    return extension


def epic():
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_api_key}'
    response = requests.get(url)
    response.raise_for_status()
    epic_json = response.json()
    for count, epic in enumerate(epic_json, start=1):
        filename = epic['image']
        unsplit_date = epic['date'].split()
        date_split = unsplit_date[0].split('-')
        year, month, day = date_split
        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{filename}.png?api_key={nasa_api_key}'
        file_name = f'epic_{count}'
        download_image(url, file_name)


def download_nasa_apods(urls):
    for count, photo in enumerate(urls, start=1):
        filename = f'nasa_apod_{count}'
        download_image(photo, filename)


if __name__ == '__main__':
    load_dotenv()
    Path('images').mkdir(parents=True, exist_ok=True)
    nasa_api_key = os.environ['NASA_API_KEY']
    photo_urls = fetch_nasa_apod()
    download_nasa_apods(photo_urls)
    fetch_spacex_last_launch()
    epic()