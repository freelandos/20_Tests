import requests


class YandexDisk:

    url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token):
        self.headers = {
            'Authorization': f'OAuth {token}',
            'Content-Type': 'application/json'
        }

    def create_folder(self, folder_path):
        request_url = self.url + 'resources'
        params = {'path': folder_path}
        response = requests.put(request_url, headers=self.headers, params=params)
        result = response.status_code
        return result
