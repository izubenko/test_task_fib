import pytest
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


link = 'https://13.68.239.92/'
# TestUserCredentials
userEmail = "test"
userPassword = "test1"

M = {0: 0, 1: 1}


def calc_fib(n):
    if n in M:
        return M[n]
    M[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return M[n]


test_positive_data_fib = [
    ("0", calc_fib(0)),
    ("15", calc_fib(15)),
    ("29", calc_fib(29))]


def test_post_access_check_status_code_equals_200():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.post(f'{link}api/v1/token',
                             {"username": userEmail, "password": userPassword}, verify=False)
    assert response.status_code == 200


@pytest.mark.parametrize("num_to_calc,expected", test_positive_data_fib)
def test_get_fib_function_with_positive_data(num_to_calc, expected):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(
        f'{link}api/v1/fibonacci?number={num_to_calc}', verify=False)
    response_body = response.json()
    assert response_body["result"] == expected
