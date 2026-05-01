import math
from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/get_attribute.html")

    x = driver.find_element(By.ID, "treasure").get_attribute("valuex")

    driver.find_element(By.ID, "answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.TAG_NAME, 'button').click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()