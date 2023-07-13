import requests
from framework.verificators.status_code import status_code_check


class ApiClient:
    url = "https://api.hh.ru"

    @staticmethod
    @status_code_check
    def get(path: str) -> requests.Response:
        url = ApiClient.url + path
        return requests.get(url)

    @staticmethod
    @status_code_check
    def post(path: str, data: dict) -> requests.Response:
        url = ApiClient.url + path
        return requests.post(url, data=data)

    @staticmethod
    @status_code_check
    def put(path: str, data: dict) -> requests.Response:
        url = ApiClient.url + path
        return requests.put(url, data=data)
