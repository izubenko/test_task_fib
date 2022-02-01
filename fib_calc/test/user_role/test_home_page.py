from fib_calc.pages.login_page import LogInPage
from fib_calc.pages.home_page import HomePage, HomePageLocators
import pytest

link = 'https://13.68.239.92/'
# TestUserCredentials
userEmail = "test"
userPassword = "test1"
M = {0: 0, 1: 1}

# Tests


class TestUserCanUseCalculator():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(link)
        login_page = LogInPage(browser)
        login_page.login_as_a_user(userEmail, userPassword)

    def calc_fib(self, n):
        if n in M:
            return M[n]
        M[n] = self.calc_fib(n - 1) + self.calc_fib(n - 2)
        return M[n]

    def test_ettfc_11_user_can_enter_an_average_value_using_the_calculator_buttons_and_calculate_the_result(self, browser):
        home_page = HomePage(browser)
        home_page.click_button(1)
        home_page.click_button(5)
        entered_number = home_page.read_fibonacci_input()
        home_page.click_calculate_button()
        calc_result = int(browser.find_element(
            *HomePageLocators.CALCULATION_RESULT).text)
        assert calc_result == self.calc_fib(
            int(entered_number)), "Not correct!"

    def test_ettfc_8_user_can_use_the_numeric_buttons_of_the_calculator(self, browser):
        home_page = HomePage(browser)
        home_page.click_button(0)
        home_page.click_button(1)
        home_page.click_button(2)
        home_page.click_button(3)
        home_page.click_button(4)
        home_page.click_button(5)
        home_page.click_button(".")
        home_page.click_button(6)
        home_page.click_button(7)
        home_page.click_button(8)
        home_page.click_button(9)
        entered_number = home_page.read_fibonacci_input()
        assert entered_number == "012345.6789", "Not correct!"
