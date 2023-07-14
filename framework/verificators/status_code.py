import functools
import requests


def status_code_check(func: callable) -> callable:
    @functools.wraps(func)
    def function(*args, **kwargs) -> requests.Response:
        expected_status_code = kwargs.pop("status_code")
        returned_value = func(*args, **kwargs)
        assert (
            expected_status_code == returned_value.status_code
        ), f"Returned status code {returned_value.status_code} does not match expected {expected_status_code}"

        return returned_value

    return function
