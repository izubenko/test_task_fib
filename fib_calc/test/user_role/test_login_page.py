from fib_calc.pages.home_page import HomePage
from fib_calc.pages.login_page import LogInPage, LogInPageLocators
import pytest
import faker


link = 'https://13.68.239.92/'
# TestUserCredentials
userEmail = "test"
userPassword = "test1"
f = faker.Faker()
invalidEmail = f.email()

# UI Tests


def test_ettfc_12_user_can_login_without_remember_me_check(browser):
    browser.get(link)
    login_page = LogInPage(browser)
    login_page.fill_email_address_input(userEmail)
    login_page.fill_password_input(userPassword)
    login_page.click_login_button()
    home_page = HomePage(browser)
    home_page.should_be_home_button_at_header()


def test_ettfc_13_login_with_invalid_email(browser):
    browser.get(link)
    login_page = LogInPage(browser)
    login_page.fill_email_address_input(invalidEmail)
    login_page.fill_password_input(userPassword)
    login_page.click_login_button()
    login_page.wait_for_message_at_body_of_error_popup()
    error_message_text = browser.find_element(
        *LogInPageLocators.ERROR_MESSAGE_BODY).text
    assert error_message_text == "No active account found with the given credentials"


def test_ettfc_3_remember_me_text_is_displayed_and_written_correctly(browser):
    browser.get(link)
    remember_me_text = browser.find_element(
        *LogInPageLocators.REMEMBER_ME_TEXT).text
    assert remember_me_text == "Remember me", "Incorrect text!"
