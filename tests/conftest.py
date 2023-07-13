import pytest
from framework.handlers.areas import AreasClient


@pytest.fixture
def areas_data(scope="session"):
    return AreasClient.get_areas()
