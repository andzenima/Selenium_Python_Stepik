from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("https://SunInJuly.github.io/execute_script.html")

    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()