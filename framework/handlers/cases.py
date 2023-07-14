from framework.clients.api import ApiClient


class CasesClient(ApiClient):
    url = "https://ws3.morpher.ru/russian/declension"

    @staticmethod
    def get_prepositional_case(word: str) -> dict:
        headers = {"User-Agent": "My Python script"}
        params = dict(
            s=word,
            format="json",
        )
        data = CasesClient.get(
            url=CasesClient.url, headers=headers, params=params, status_code=200
        )
        return data.json()
