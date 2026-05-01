import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element(By.ID, 'book').click()

    x = driver.find_element(By.ID, "input_value").text
    driver.find_element(By.ID, "answer").send_keys(str(math.log(abs(12 * math.sin(int(x))))))

    driver.find_element(By.ID, 'solve').click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()