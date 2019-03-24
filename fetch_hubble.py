import requests
import os


def fetch_hubble_image_by_id(image_id):    
    url = 'http://hubblesite.org/api/v3/image/'
    image_url = '{}{}'.format(url, image_id)
    response = requests.get(image_url)
    image_info = response.json()
    image_links = [file['file_url'] for file in image_info['image_files']]
    latest_link = image_links[-1]
    image_ext = latest_link.split('.')[-1]

    os.makedirs('images', exist_ok=True)

    image_saving_path = 'images/{}.{}'.format(image_id, image_ext)
    response = requests.get(latest_link)
    with open(image_saving_path, 'wb') as file:
        file.write(response.content)


def get_hubble_images_ids_by_collection(collection_name):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
    images_ids = []
    page = 0
    page_results = ['']
    while page_results != []:
        page += 1
        payload = {'page': page}
        response = requests.get(url, params=payload)
        page_results = response.json()
        for result in page_results:
            images_ids.append(result['id'])
    return images_ids


def main():
    hubble_images_ids = get_hubble_images_ids_by_collection('printshop')
    for image_id in hubble_images_ids:
        fetch_hubble_image_by_id(image_id)


if __name__ == '__main__':
    main()
