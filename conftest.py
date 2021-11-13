import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.base_page import BasePage

options = webdriver.ChromeOptions()
options.add_argument('headless')


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    test_browser = webdriver.Chrome(chrome_options=options)
    yield test_browser
    print("\nquit browser..")
    test_browser.quit()

