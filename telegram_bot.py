from email.policy import default
import telegram
import random
import time
import argparse
import os
import dotenv


def main():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    filenames = next(os.walk('images/'), (None, None, []))[2]
    random_filenames = random.shuffle(filenames)
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    channel_id = os.environ['CHANNEL_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('--pause',
                        type=int,
                        default=14400)
    args = parser.parse_args()
    pause_time = args.pause

    while True:
        bot = telegram.Bot(token=telegram_bot_token)
        chat_id = channel_id
        for file in filenames:
            with open(f'images/{file}', 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(pause_time)
        break


if __name__ == '__main__':
    main()