import os
from main import download_image, check_extension
import requests
from dotenv import load_dotenv

from urllib.parse import urlsplit
from pathlib import Path


def epic():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
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


def main():
    epic()


if __name__ == '__main__':
    main()