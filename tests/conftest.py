import pytest
from framework.handlers.areas import AreasClient
from framework.helpers.areas import AreasHelper


@pytest.fixture
def areas_data(scope="session") -> dict:
    return AreasClient.get_areas()


@pytest.fixture
def areas_countries_data(scope="session") -> dict:
    return AreasClient.get_areas_countries()


@pytest.fixture
def random_area_id(areas_data: dict) -> int:
    data = AreasHelper.get_random_area(areas_data=areas_data)
    return data.get("id")
