from fib_calc.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators():
    HOME_BUTTON = (By.XPATH, "//a[text()='Home']")
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/a')
    # Fibonacci Calculator Panel
    FIBONACCI_INPUT = (By.XPATH, "//input[@placeholder='fibonacci']")
    CALCULATE_BUTTON = (By.XPATH, "//button[text()='Calculate']")
    DELETE_BUTTON = (By.XPATH, "//div[4]/button[3]")
    CALCULATION_RESULT = (By.TAG_NAME, "h2")

    # get button: n = 0-9 and .

    def get_button(n):
        return (By.XPATH, f"//button[text()='{n}']")


class HomePage(BasePage):
    def should_be_home_url(self):
        assert "/home" in self.browser.current_url, "There is not '/home' url!"

    def should_be_home_button_at_header(self):
        assert self.is_element_present(
            *HomePageLocators.HOME_BUTTON), "Home button is not presented on /home page!"

    def click_logout_button(self):
        logout_button = self.browser.find_element(
            *HomePageLocators.LOGOUT_BUTTON)
        logout_button.click()

    # Calculator
    def click_calculate_button(self):
        calculate_button = self.browser.find_element(
            *HomePageLocators.CALCULATE_BUTTON)
        calculate_button.click()

    def click_button(self, number):
        button = self.browser.find_element(
            *HomePageLocators.get_button(number))
        button.click()

    def click_delete_button(self):
        delete_button = self.browser.find_element(
            *HomePageLocators.DELETE_BUTTON)
        delete_button.click()

    def fill_fibonacci_input(self, value):
        fibonacci_input = self.browser.find_element(
            *HomePageLocators.FIBONACCI_INPUT)
        return fibonacci_input.send_keys(value)

    def read_fibonacci_input(self):
        fibonacci_input = self.browser.find_element(
            *HomePageLocators.FIBONACCI_INPUT)
        return fibonacci_input.get_attribute("value")
