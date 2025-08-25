import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="function")
# def driver():
#     print("\nstart driver for test..")
#     driver = webdriver.Chrome()
#     yield driver
#     print("\nquit driver..")
#     driver.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "button.favorite")