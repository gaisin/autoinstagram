from instabot import Bot
from dotenv import load_dotenv

import requests
import os
import glob


def main():
    load_dotenv()
    INSTA_USERNAME = os.getenv('INSTA_USERNAME')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')

    bot = Bot()
    bot.login(username=INSTA_USERNAME, password=INSTA_PASSWORD)

    images_paths = glob.glob("images/*")
    for image_path in images_paths:
        bot.upload_photo(image_path)


if __name__ == '__main__':
    main()