from framework.errors import CommonErrors
from framework.handlers.areas import AreasClient
from framework.helpers.areas import AreasHelper
from framework.verificators.areas import AreasVerificator


class TestAreas:
    def test_get_areas_full(self):
        response_data = AreasClient.get_areas()
        AreasVerificator.validate_areas_schema(content=response_data)
        assert response_data, "Response body is empty"
        areas_ids = AreasHelper.get_all_area_ids(areas_data=response_data)
        assert areas_ids == set(areas_ids), "Response ids are not unique"
        # assert db_data == response_data, "Response data is not matching data from db (currently no access to db)"

    def test_get_areas_by_id(self, areas_data):
        expected_data = AreasHelper.get_random_area(areas_data=areas_data)
        response_data = AreasClient.get_areas_by_id(area_id=expected_data.get("id"))

        AreasVerificator.validate_specific_area_schema(content=response_data)
        assert (
            response_data == expected_data
        ), "Returned content is not mathing expected one"

    def test_get_areas_specific_negative(self, areas_data):
        nonexistent_area_id = AreasHelper.get_nonexistent_area_id(areas_data=areas_data)
        response_data = AreasClient.get_areas_by_id(
            area_id=nonexistent_area_id, status_code=404
        )
        assert (
            response_data.get("errors")[0].get("type") == CommonErrors(404).name
        ), "Response error message does not match expected one"

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
