import requests
import os


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(api_url)
    latest_launch = response.json()
    images_links = latest_launch['links']['flickr_images']

    os.makedirs('images', exist_ok=True)

    for i, image_link in enumerate(images_links, start=1):
        image_name = 'spacex{}.jpg'.format(i)
        response = requests.get(image_link)
        image_saving_path = 'images/{}'.format(image_name)
        with open(image_saving_path, 'wb') as file:
            file.write(response.content)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
