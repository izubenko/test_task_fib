from fib_calc.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogInPageLocators():
    QA_INTERVIEW_BUTTON_AT_HEADER = (By.XPATH, "//a[text()='QA Interview']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='logout']")
    EMAIL_ADDRESS_LABEL = (By.XPATH, "//label[text()='Email address']")
    EMAIL_ADDRESS_INPUT = (By.ID, "formBasicEmail")
    PASSWORD_LABEL = (By.XPATH, "//label[text()='Password']")
    PASSWORD_INPUT = (By.ID, "formBasicPassword")
    REMEMBER_ME_CHECKBOX = (By.ID, "formBasicCheckbox")
    REMEMBER_ME_TEXT = (By.CLASS_NAME, "form-check-label")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    ERROR_MESSAGE_BODY = (By.CLASS_NAME, "toast-body")


class LogInPage(BasePage):
    def fill_email_address_input(self, email):
        email_address_input = self.browser.find_element(
            *LogInPageLocators.EMAIL_ADDRESS_INPUT)
        email_address_input.send_keys(email)

    def fill_password_input(self, password):
        password_input = self.browser.find_element(
            *LogInPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_remember_me_checkbox(self):
        remember_me_checkbox = self.browser.find_element(
            *LogInPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me_checkbox.click()

    def click_login_button(self):
        login_button = self.browser.find_element(
            *LogInPageLocators.LOGIN_BUTTON)
        login_button.click()

    def login_as_a_user(self, email, password):
        self.fill_email_address_input(email)
        self.fill_password_input(password)
        self.click_login_button()

    def wait_for_message_at_body_of_error_popup(self):
        self.text_present_in_element(
            *LogInPageLocators.ERROR_MESSAGE_BODY, "No active account found with the given credentials")
