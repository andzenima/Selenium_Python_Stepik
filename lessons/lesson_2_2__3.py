from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("https://suninjuly.github.io/selects2.html")

    n = int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text)

    driver.find_element(By.ID, 'dropdown').click()
    driver.find_element(By.CSS_SELECTOR, f'option[value="{n}"]').click()

    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()