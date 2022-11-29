import requests
import os


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск в корневую папку"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'  # задаем адрес, по которому будем делать запрос
        # объявляем обязательные параметры метода - путь/имяфайла, куда и с каким названием на ЯДиск будем загружать
        params = {'path': file_path} 
        # делаем запрос на получение ссылки на загрузку файла
        res = requests.get(url, headers=self.get_headers(), params=params)  
        # получаем из ответа ссылку для загрузки файла
        upload_url = res.json()['href']
        # на эту ссылку отправляем put запрос с указанием параметра data - файла, открытого для чтения
        response = requests.put(upload_url, data=open(path_file, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Файл загружен успешно')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path = input('Укажите абсолютный путь к загружаемому файлу: ')
    name_of_file = os.path.basename(path)
    path_file = os.path.join(os.getcwd(), path)
    token = input('Введите свой токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(name_of_file)
