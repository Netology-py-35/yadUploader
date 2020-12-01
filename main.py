# https://cloud-api.yandex.net/v1/disk/resources/upload?path=tree.jpg&url=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2015%2F04%2F23%2F22%2F00%2Ftree-736885_1280.jpg
from pprint import pprint

import requests

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
HEADERS = {"Authorization": "OAuth AgAAAAAEAnRIAADLWwWAerR-zUo3gEHfKmNPss8"}


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        with open(file_path, 'rb') as f:
            resp = requests.post(url, files={'file': f}, headers=self.token, params={'path': '/public'})
        return resp.json()


if __name__ == '__main__':
    uploader = YaUploader(HEADERS)
    result = uploader.upload('demo.txt')
    print(result)

    # resp = requests.get(url, params={'path':'/'}, headers=HEADERS)
    # resp.raise_for_status()
    # data = resp.json()
    # pprint(data)
