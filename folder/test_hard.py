from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time
import pytest


class TestCode():

    @pytest.mark.parametrize('part', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, part):
        answer1 = str(math.log(int(time.time() + 13.6)))
        link = f"https://stepik.org/lesson/{part}/step/1/"
        browser.get(link)
        variant = WebDriverWait(browser, 6).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        variant.send_keys(answer1)
        button = WebDriverWait(browser, 6).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )
        button.click()
        answer_response = WebDriverWait(browser, 6).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        ).text

        assert str(answer_response) == 'Correct!', f"expected 'Correct!', got {answer_response}"






