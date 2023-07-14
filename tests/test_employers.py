import allure
import random
import math
from framework.handlers.employers import EmployersClient
from framework.verificators.employers import EmployersVerificator


@allure.feature("Getting employers info")
class TestAreas:
    @allure.title("Test full /employers response")
    def test_get_employers_full(self):
        per_page = random.randrange(20, 100, 20)
        page = random.randint(1, 10)
        response_data = EmployersClient.get_employers(per_page=per_page, page=page)

        assert response_data, "Response body is empty"

        EmployersVerificator.validate_employers_schema(data=response_data)

        number_of_returned_items = len(response_data.get("items"))
        assert (
            number_of_returned_items == per_page
        ), f"Number of returned items is {number_of_returned_items}, expected {per_page}"

        expected_pages = math.ceil(response_data.get("found") / per_page)
        return_pages = response_data.get("pages")
        assert (
            expected_pages == return_pages
        ), f"Expected {expected_pages} as number of pages, got {return_pages}"

        returned_page = response_data.get("page")
        assert page == returned_page, f"Expected {page} page, got {returned_page}"
        assert 1

    @allure.title("Test /employers text search with different register")
    def test_search_employers(self):
        response_data = EmployersClient.get_employers(text="Мой офис")
        response_data1 = EmployersClient.get_employers(text="Мой офис".lower())
        response_data2 = EmployersClient.get_employers(text="Мой офис".upper())

        assert 1
