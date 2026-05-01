import math
from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/find_link_text")

    driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()

    driver.find_element(By.TAG_NAME, 'input').send_keys("John")
    driver.find_element(By.NAME, 'last_name').send_keys("Doe")
    driver.find_element(By.CLASS_NAME, 'form-control.city').send_keys("Philadelphia")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()