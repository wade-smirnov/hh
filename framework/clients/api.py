import requests
from framework.verificators.status_code import status_code_check


class ApiClient:
    url = "https://api.hh.ru"

    @staticmethod
    @status_code_check
    def get(path: str) -> requests.Response:
        url = ApiClient.url + path
        return requests.get(url)
