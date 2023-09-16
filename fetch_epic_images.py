import os
from help_functions import download_image
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv


def fetch_epic_images(api_key):
    params = {'api_key' : api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_photo_info_list = response.json()
    for count, epic in enumerate(epic_photo_info_list, start=1):
        filename = epic['image']
        unsplit_date = epic['date'].split()
        date_split = unsplit_date[0].split('-')
        year, month, day = date_split
        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{filename}.png'
        file_name = f'epic_{count}'
        download_image(url, file_name, params)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_epic_images(nasa_api_key)