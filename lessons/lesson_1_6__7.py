# lesson_1_6__7

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/huge_form.html")

    elements = driver.find_elements(By.CSS_SELECTOR, "input")

    for e in elements:
        e.send_keys("BBB")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])

    time.sleep(3)
    driver.switch_to.alert.accept()