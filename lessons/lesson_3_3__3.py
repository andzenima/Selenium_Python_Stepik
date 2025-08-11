# lesson_3_3__3

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def fill_form(driver, link):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('1_Name')
    driver.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('2_Name')
    driver.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('mail@example.com')
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    return driver.find_element(By.TAG_NAME, 'h1').text


def test_registration(driver):
    link = 'http://suninjuly.github.io/registration1.html'
    result = fill_form(driver, link)
    assert result == "Congratulations! You have successfully registered!"


def test_registration_bug(driver):
    link = 'http://suninjuly.github.io/registration2.html'
    result = fill_form(driver, link)
    assert result == "Congratulations! You have successfully registered!"

if __name__ == "__main__":
    pytest.main()