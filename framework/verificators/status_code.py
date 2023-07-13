import functools


def status_code_check(func):
    @functools.wraps(func)
    def function(*args, **kwargs):
        expected_status_code = kwargs.pop("status_code")
        returned_value = func(*args, **kwargs)
        assert (
            expected_status_code == returned_value.status_code
        ), f"Returned status code {returned_value.status_code} does not match expected {expected_status_code}"

        return returned_value

    return function
