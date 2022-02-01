from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePageLocators():
    QA_INTERVIEW_TITLE = (By.XPATH, "//nav/div/a")


class BasePage():
    def __init__(self, browser: RemoteWebDriver, timeout=10):
        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)
        self.web_element = None

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def text_present_in_element(self, how, what, text, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element((how, what), text))
        except (NoSuchElementException):
            return False
        return True
