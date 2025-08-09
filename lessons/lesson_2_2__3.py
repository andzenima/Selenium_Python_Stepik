# lesson_2_2__3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as driver:
    driver.get("https://suninjuly.github.io/selects1.html")

    num1 = driver.find_element(By.ID, "num1").text
    num2 = driver.find_element(By.ID, "num2").text
    op = driver.find_element(By.CSS_SELECTOR, "#num1 + .nowrap").text

    res = str(eval(num1+op+num2))

    select = Select(driver.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_visible_text(res)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])

    time.sleep(3)
    driver.switch_to.alert.accept()