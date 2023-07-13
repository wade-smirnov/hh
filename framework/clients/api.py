import requests


class ApiClient:
    url = 'https://api.hh.ru'

    @staticmethod
    def get(path: str) -> requests.Response:
        url = ApiClient.url + path
        return requests.get(url)
