import os
from help_functions import download_image
import requests
import argparse


def fetch_spacex_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    if not photos:
        return None
    for count, photo in enumerate(photos, start=1):
        filename = f'spacex_{count}'
        download_image(photo, filename)
    

def main():
    parser = argparse.ArgumentParser(description='скачивает фотографии с запуска, по id запуска.')
    parser.add_argument('--launch_id',
                         type=str,
                         help='указывается id запуска с которого надо скачать фото',
                         default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(launch_id=args.launch_id)


if __name__ == '__main__':
    main()