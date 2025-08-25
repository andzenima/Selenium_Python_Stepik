# lesson_3_4__5

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, driver):
        print("start test1")
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        print("start test2")
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")