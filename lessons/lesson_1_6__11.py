import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/registration2.html")

    driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]').send_keys("John")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys("test@mail.com")

    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(2)

    assert "Congratulations! You have successfully registered!" == driver.find_element(By.TAG_NAME, "h1").text

    print(driver.find_element(By.TAG_NAME, "h1").text)