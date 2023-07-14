import allure
import random
import math

from framework.constants import CitiesIds, CountriesNames, SearchString
from framework.handlers.employers import EmployersClient
from framework.helpers.areas import AreasHelper
from framework.verificators.employers import EmployersVerificator


@allure.feature("Getting employers info")
class TestEmployers:
    @allure.title("Test full /employers response")
    def test_get_employers_full(self):
        with allure.step("Test data preparation"):
            per_page = random.randrange(20, 100, 20)
            page = random.randint(1, 10)
        with allure.step("Request to /employers"):
            response_data = EmployersClient.get_employers(per_page=per_page, page=page)

        with allure.step("Response data structure check"):
            assert response_data, "Response body is empty"

            EmployersVerificator.validate_employers_schema(data=response_data)

        with allure.step("Response data logic checks"):
            number_of_returned_items = len(response_data.get("items"))
            assert (
                number_of_returned_items == per_page
            ), f"Number of returned items is {number_of_returned_items}, expected {per_page}"

            expected_pages = math.ceil(response_data.get("found") / per_page)
            returned_pages = response_data.get("pages")
            assert (
                expected_pages == returned_pages
            ), f"Expected {expected_pages} as number of pages, got {returned_pages}"

            returned_page = response_data.get("page")
            assert page == returned_page, f"Expected {page} page, got {returned_page}"

    @allure.title("Test /employers 'Мой офис' string search with different register")
    def test_search_employers_different_register(self):
        different_register = EmployersClient.get_employers(text="Мой офис")
        lower_register = EmployersClient.get_employers(
            text=SearchString.default.lower()
        )
        upper_register = EmployersClient.get_employers(
            text=SearchString.default.upper()
        )
        assert (
            different_register == lower_register == upper_register
        ), "Results differ, depending on register"

    @allure.title("Test /employers text search with area filter")
    def test_search_employers_area_filter(self, areas_countries_data, areas_data):
        with allure.step("Test data preparation"):
            russian_area = AreasHelper.get_area_by_country_name(
                areas_countries_data=areas_countries_data, name=CountriesNames.russia
            )

        with allure.step("Requests to /employers with area filter"):
            russian_area_response = EmployersClient.get_employers(
                text=SearchString.default, area=russian_area.get("id")
            )
            saint_petersburg_response = EmployersClient.get_employers(
                text=SearchString.default, area=CitiesIds.saint_petersburg
            )

        with allure.step("/employers with area filter logic check"):
            for employer in saint_petersburg_response.get("items"):
                assert employer in russian_area_response.get(
                    "items"
                ), "Some employers from city are not presented in search results for country"

    @allure.title("Test failing of framework test")
    def test_fail_step(self):
        with allure.step("Imitating data preparation"):
            pass

        with allure.step("Some steps before fail"):
            pass

        with allure.step("Step that failed"):
            assert 0, "This test case was intented to fail"
