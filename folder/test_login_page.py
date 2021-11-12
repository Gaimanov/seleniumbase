from pages.login_page import LoginPage
import pytest
from pages.login_page import LoginPageLocators


def test_should_be_login_url(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    login_page = LoginPage(browser, link)
    login_page.open()
    assert "/login" in login_page.url, "login is absent in current url"


@pytest.mark.smoke
def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    assert login_page.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


@pytest.mark.smoke
def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    assert login_page.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
