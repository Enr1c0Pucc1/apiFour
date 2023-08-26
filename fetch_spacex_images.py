import os
from help_functions import download_image
import requests
import argparse


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
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id',
                         type=str,
                         default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(launch_id=args.launch_id)


if __name__ == '__main__':
    main()