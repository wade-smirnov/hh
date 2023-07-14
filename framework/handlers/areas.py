from framework.clients.api import ApiClient


class AreasClient(ApiClient):
    path = "/areas"

    @staticmethod
    def get_areas(status_code: int = 200) -> dict:
        data = AreasClient.get(path=AreasClient.path, status_code=status_code)
        return data.json()

    @staticmethod
    def get_areas_by_id(area_id: int, status_code: int = 200) -> dict:
        path = AreasClient.path + "/" + str(area_id)
        data = AreasClient.get(path=path, status_code=status_code)
        return data.json()

    @staticmethod
    def get_areas_additional_case(
        area_id: int, additional_case: str = "prepositional", status_code: int = 200
    ) -> dict:
        path = (
            AreasClient.path
            + "/"
            + str(area_id)
            + f"/?additional_case={additional_case}"
        )
        data = AreasClient.get(path=path, status_code=status_code)
        return data.json()

    @staticmethod
    def get_areas_countries(status_code: int = 200) -> dict:
        path = AreasClient.path + "/countries"
        data = AreasClient.get(path=path, status_code=status_code)
        return data.json()
