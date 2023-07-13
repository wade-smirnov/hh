from framework.clients.api import ApiClient


class AreasClient(ApiClient):
    path = "/areas"

    @staticmethod
    def get_areas(status_code: int = 200):
        data = AreasClient.get(path=AreasClient.path, status_code=status_code)
        return data.json()
