import urllib.parse

from framework.clients.api import ApiClient


class EmployersClient(ApiClient):
    path = "/employers"

    @staticmethod
    def get_employers(
        status_code: int = 200,
        text: str | None = None,
        area: int | None = None,
        only_with_vacancies: bool | None = None,
        page: int = 0,
        per_page: int = 100,
    ) -> dict:
        params = {
            "text": text,
            "area": area,
            "only_with_vacancies": only_with_vacancies,
            "page": page,
            "per_page": per_page,
        }
        data = EmployersClient.get(
            path=EmployersClient.path, status_code=status_code, params=params
        )
        return data.json()
