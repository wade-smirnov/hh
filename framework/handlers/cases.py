import requests


class CasesClient:
    url = "https://ws3.morpher.ru/russian/declension"

    @staticmethod
    def get_prepositional_case(word: str):
        headers = {"User-Agent": "My Python script"}
        params = dict(
            s=word,
            format="json",
        )
        data = requests.get(url=CasesClient.url, headers=headers, params=params)
        return data.json()
