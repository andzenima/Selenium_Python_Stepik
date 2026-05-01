import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/file_input.html")

    driver.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("John")
    driver.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("Doe")
    driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("example@mail.com")

    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "lesson_2_2__8_test_file.txt")

    with open(file_path, "wb") as file:
        file.truncate(1024)

    driver.find_element(By.CSS_SELECTOR, '[name="file"]').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()