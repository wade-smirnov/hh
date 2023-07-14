from framework.errors import CommonErrors, AreasErrorTypes
from framework.handlers.areas import AreasClient
from framework.helpers.areas import AreasHelper
from framework.utils import random_word, morph_word_to_prepositinal_case
from framework.verificators.areas import AreasVerificator


class TestAreas:
    def test_get_areas_full(self):
        response_data = AreasClient.get_areas()
        assert response_data, "Response body is empty"
        AreasVerificator.validate_areas_schema(content=response_data)
        areas_ids = AreasHelper.get_all_area_ids(areas_data=response_data)
        assert areas_ids == set(areas_ids), "Response ids are not unique"
        # assert db_data == response_data, "Response data is not matching data from db (currently no access to db)"

    def test_get_areas_by_id(self, areas_data: list):
        expected_data = AreasHelper.get_random_area(areas_data=areas_data)
        response_data = AreasClient.get_areas_by_id(area_id=expected_data.get("id"))

        AreasVerificator.validate_specific_area_schema(content=response_data)
        assert (
            response_data == expected_data
        ), "Returned content is not mathing expected one"

    def test_get_areas_specific_negative(self, areas_data: list):
        nonexistent_area_id = AreasHelper.get_nonexistent_area_id(areas_data=areas_data)
        response_data = AreasClient.get_areas_by_id(
            area_id=nonexistent_area_id, status_code=404
        )
        assert (
            response_data.get("errors")[0].get("type") == CommonErrors(404).name
        ), "Response error message does not match expected one"

    def test_get_areas_additional_case(self, areas_data: list):
        expected_data = AreasHelper.get_random_area(areas_data=areas_data)
        random_area_id = expected_data.get("id")

        response_data = AreasClient.get_areas_additional_case(area_id=random_area_id)
        AreasVerificator.validate_additional_case_schema(content=response_data)

        word = response_data.get("name")
        expected_prepositional_case = morph_word_to_prepositinal_case(word=word)

        expected_data["name_prepositional"] = expected_prepositional_case
        assert (
            response_data == expected_data
        ), "Returned content is not mathing expected one"

    def test_get_areas_additional_case_negative(self, random_area_id):
        case = random_word()
        response_data = AreasClient.get_areas_additional_case(
            area_id=random_area_id, additional_case=case, status_code=400
        )
        assert (
            response_data.get("errors")[0].get("type") == AreasErrorTypes.incorrect_case
        ), "Response error message does not match expected one"

    def test_get_areas_countries(self):
        response_data = AreasClient.get_areas_countries()
        assert response_data, "Response body is empty"
        AreasVerificator.validate_countries_schema(content=response_data)
        # assert db_data == response_data, "Response data is not matching data from db (currently no access to db)"

