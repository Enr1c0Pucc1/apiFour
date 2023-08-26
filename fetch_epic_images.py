import os
from help_functions import download_image
import requests
from dotenv import load_dotenv


def epic(api_key):
    params = {'api_key' : api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_files = response.json()
    for count, epic in enumerate(epic_files, start=1):
        filename = epic['image']
        unsplit_date = epic['date'].split()
        date_split = unsplit_date[0].split('-')
        year, month, day = date_split
        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{filename}.png?api_key={api_key}'
        file_name = f'epic_{count}'
        download_image(url, file_name)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    epic(nasa_api_key)