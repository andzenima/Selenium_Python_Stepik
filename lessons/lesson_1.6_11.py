# lesson_1.6_11

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/registration2.html")

    f_name = driver.find_element(By.CSS_SELECTOR, ".first_block [class*='first'] input")
    f_name.send_keys("First Name")

    l_name = driver.find_element(By.CSS_SELECTOR, ".first_block [class*='second'] input")
    l_name.send_keys("Last Name")

    e_mail = driver.find_element(By.CSS_SELECTOR, ".first_block [class*='third'] input")
    e_mail.send_keys("Email")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(2)