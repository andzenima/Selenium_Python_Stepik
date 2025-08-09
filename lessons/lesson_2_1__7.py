# lesson_2_1__7

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/get_attribute.html")

    chst_n = int(driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex"))

    ans = driver.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(str(math.log(abs(12 * math.sin(chst_n)))))

    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])

    time.sleep(3)
    driver.switch_to.alert.accept()