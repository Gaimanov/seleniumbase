import pytest
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
import time


class TestCase():

    @pytest.mark.parametrize('number', [pytest.param(7, marks=pytest.mark.xfail), '8'])
    @pytest.mark.smoke
    def test_guest_can_add_product_to_cart(self, browser, number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        # product_page.go_to_login_page()
        product_page.add_item_to_basket()
        product_page.solve_quiz_and_get_code()
        assert product_page.is_element_present(*ProductPageLocators.MESSAGE), "Message is not presented"

        msg = product_page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product = product_page.browser.find_element(*ProductPageLocators.MESSAGE).text
        assert product == msg, 'name of the book does not match book in the message'

        msg = product_page.browser.find_element(*ProductPageLocators.PRICE_MSG).text
        price = product_page.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == msg, 'price of the book does not match price in the message'

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_cart(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_basket()
        product_page.solve_quiz_and_get_code()
        assert product_page.is_not_element_present(*ProductPageLocators.ADDED), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message_by_default(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_not_element_present(*ProductPageLocators.ADDED), \
            "Success message is presented, but should not be"

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_cart(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_basket()
        product_page.solve_quiz_and_get_code()
        assert product_page.is_disappeared(*ProductPageLocators.ADDED), \
            "Success message is presented, but should not be"

    @pytest.mark.regression
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    @pytest.mark.regression
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        product_page = ProductPage(browser, link)
        product_page.open()
        try:
            product_page.enter_the_cart()
        except:
            browser.save_screenshot('screen1.png')
        assert product_page.is_not_element_present(*ProductPageLocators.BASKET_EMPTY_PROOF), \
            "Message about total price is presented, but should not be"

        assert product_page.is_element_present(*ProductPageLocators.BASKET_EMPTY_MSG), "Message about empty " \
                                                                               "basket is not presented"


class TestUserAddToCartFromProductPage():
    @pytest.mark.smoke
    @pytest.fixture(scope="function", autouse=True)
    def registration(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3'
        product_page = LoginPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        product_page.register_new_user(email, 'helpmeplease')
        assert product_page.is_element_present(*ProductPageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def test_user_cant_see_success_message_by_default(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3'
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_not_element_present(*ProductPageLocators.ADDED), \
            "Success message is presented, but should not be"

    @pytest.mark.smoke
    def test_user_can_add_product_to_cart(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_basket()
        assert product_page.is_element_present(*ProductPageLocators.MESSAGE), "Message is not presented"










