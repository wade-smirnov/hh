from framework.handlers.areas import AreasClient
from framework.verificators.areas import AreasVerificator


class TestAreas:
    def test_get_areas_full(self):
        content = AreasClient.get_areas()
        AreasVerificator.validate_areas_schema(content=content)
        # assert with DB
        assert content

    def test_get_areas_by_id(self, areas_data):
        content = AreasClient.get_areas_by_id(area_id=1)
        AreasVerificator.validate_schema(content=content)
        # assert with DB
        assert content

    def test_get_areas_specific_negative(self):
        content = AreasClient.get_areas()
        AreasVerificator.validate_schema(content=content)
        # assert with DB
        assert content

    def test_get_areas_additional_case(self):
        content = AreasClient.get_areas()
        AreasVerificator.validate_schema(content=content)
        # assert with DB
        assert content

    def test_get_areas_additional_case_negative(self):
        content = AreasClient.get_areas()
        AreasVerificator.validate_schema(content=content)
        # assert with DB
        assert content

    def test_get_areas_countries(self):
        content = AreasClient.get_areas_countries()
        AreasVerificator.validate_countries_schema(content=content)
        # assert with DB
        assert content
