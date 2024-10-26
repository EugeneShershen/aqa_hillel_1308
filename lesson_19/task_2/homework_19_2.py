import requests
from pathlib import Path


def post_method(url, img_path, img_name):
    with open(img_path, 'rb') as image_file:
        files = {'image': (img_name, image_file.read(), "image/*")}

    response = requests.post(url, files=files)

    if response.status_code != 201:
        error = f"Error with status code: {response.status_code};\ndetails: {response.text}"
        return error
    else:
        return response.status_code, response.json()


def get_method(url, content_type):
    headers = {'Content-Type': content_type}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        error = f"Error with status code: {response.status_code};\ndetails: {response.text}"
        return error
    else:
        if content_type == 'image':
            with open(Path(f'img/downloaded_image.jpg'), 'wb') as img:
                img.write(response.content)
            return response.status_code, "Image was downloaded successfully"
        elif content_type == 'text':
            return response.status_code, response.json()


def delete_method(url):
    response = requests.delete(url)

    if response.status_code != 200:
        error = f"Error with status code: {response.status_code};\ndetails: {response.text}"
        return error
    else:
        return response.status_code, response.json()
