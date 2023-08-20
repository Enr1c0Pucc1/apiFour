import os
from main import download_image, check_extension
import requests
import argparse

from urllib.parse import urlsplit
from pathlib import Path


def fetch_spacex_launch(launch_id):
    id = launch_id
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    if not photos:
        print('No latest photos')
    for count, photo in enumerate(photos, start=1):
        filename = f'spacex_{count}'
        download_image(photo, filename)


def fetch_spacex():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id',
                         type=str,
                         default='latest')
    args = parser.parse_args()
    Path('images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_launch(launch_id=args.launch_id)


if __name__ == '__main__':
    fetch_spacex()