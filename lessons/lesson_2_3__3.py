# lesson_2_3__3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/alert_accept.html")

    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    driver.switch_to.alert.accept()

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)
    ans = driver.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(str(math.log(abs(12 * math.sin(x)))))
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])
    time.sleep(3)

