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

    parser = argparse.ArgumentParser()
    parser.add_argument('--t',
                        type=int,
                        default=os.environ['DEFAULT_PAUSE'])
    args = parser.parse_args()
    pause_time = args.t

    os.environ['DEFAULT_PAUSE'] = str(pause_time)
    dotenv.set_key(dotenv_file, 'DEFAULT_PAUSE', os.environ['DEFAULT_PAUSE'])

    while True:
        bot = telegram.Bot(token=telegram_bot_token)
        chat_id = bot.get_updates()[-1].message.chat_id
        for file in filenames:
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{file}', 'rb'))
            time.sleep(pause_time)
        break


if __name__ == '__main__':
    main()