
from distutils.command.upload import upload
import requests
from pprint import pprint

heroes_list = ['Hulk', 'Captain America', 'Thanos']
def find_max_intelligence(heroes):
    files_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(files_url)
    dict_intelligence = {}
    for i in heroes:
        for l in response.json():
            if l['name'] == i:
                dict_intelligence[i] = l['powerstats']['intelligence']
            else:
                continue
    return f'Smartest superhero: {max(dict_intelligence)}'
        


my_token = ''

class YandexDisk:

    def __init__(self, token):
        self.token = my_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_file_to_disk(self, disk_file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")
if __name__ == '__main__':
    yandex = YandexDisk(my_token)
    yandex.upload_file_to_disk('/photo.jpg', 'photo.jpg')

