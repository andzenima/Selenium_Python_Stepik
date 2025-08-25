# lesson_1_6__5

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/find_link_text")

    txt = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    driver.find_element(By.LINK_TEXT, txt).click()

    input1 = driver.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Donald")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Trump")
    input3 = driver.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Palm Beach")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("USA")

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])

    time.sleep(3)
    driver.switch_to.alert.accept()