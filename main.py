import requests, os
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()

TOKEN = os.environ.get('TOKEN')
HEADERS = {"Authorization": f"OAuth {TOKEN}"}


url_requests = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_url(self, url, name):
        resp  = requests.get (url, headers=self.token, params={
            'path': f'/{name}',
            'overwrite': 'true'
        })
        resp.raise_for_status()
        return resp.json()['href']

    def upload(self, file_path: str, url):
        with open(file_path, 'rb') as f:
            resp = requests.post(url, files={'file': f})

        return resp


if __name__ == '__main__':
    uploader = YaUploader(HEADERS)
    upload_url = uploader.get_upload_url(url_requests, 'IMG_1858.jpeg')
    print(upload_url)
    result = uploader.upload('IMG_1858.jpeg', upload_url)
    print(result)
