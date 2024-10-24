import requests
from pathlib import Path


def download_images_from_url():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        full_data = response.json()
        photos_list = full_data["photos"]

        number = 1
        for photo in photos_list:
            img_url = photo.get("img_src")

            if img_url:
                img_response = requests.get(img_url)
                path_for_photos = Path(f"photos/mars_photo{number}.jpg")

                with open(path_for_photos, 'wb') as img:
                    img.write(img_response.content)

            number += 1
    else:
        print(f"Error with status code: {response.status_code}")
