import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    print("\nquit driver..")
    driver.quit()