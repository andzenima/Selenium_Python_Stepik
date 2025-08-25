# lesson_3_4__4

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")