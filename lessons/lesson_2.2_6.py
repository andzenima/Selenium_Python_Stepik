# lesson_2.2_6

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/execute_script.html")

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    ans = driver.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(str(math.log(abs(12 * math.sin(x)))))

    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    rad = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    rad.location_once_scrolled_into_view
    rad.click()

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) +2:])

    time.sleep(3)
    driver.switch_to.alert.accept()

