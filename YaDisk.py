import requests


class YaUploader:

    def __init__(self, toke: str):
        self.token = toke

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        result = self._get_upload_link(file_path=file_path)
        url = result.get("href")
        response = requests.put(url, data=open('1.txt', 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    path_to_file = 'test/1.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
