# lesson_2_2__8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/file_input.html")

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Bob")

    second_name = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
    second_name.send_keys("Peterson")

    email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("example@mail.com")

    upload = driver.find_element(By.ID, "file")
    upload.send_keys("/Users/artemparkhomenko/Downloads/file.txt")

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) +2:])

    time.sleep(3)

# auto file creating:
# with open("test.txt", "w") as file:
#     content = file.write("automationbypython")  # create test.txt file