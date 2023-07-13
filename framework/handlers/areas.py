from framework.clients.api import ApiClient


class AreasClient(ApiClient):
    path = '/areas'

    @staticmethod
    def get_areas():
        data = AreasClient.get(AreasClient.path)
        return data.json()