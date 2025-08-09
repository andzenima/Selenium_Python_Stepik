# lesson_2_1__5

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

with webdriver.Chrome() as driver:
    driver.get("https://suninjuly.github.io/math.html")

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    ans = driver.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])

    time.sleep(3)
    driver.switch_to.alert.accept()