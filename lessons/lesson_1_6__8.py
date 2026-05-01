from selenium import webdriver
from selenium.webdriver.common.by import By

with  webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/find_xpath_form")

    driver.find_element(By.TAG_NAME, 'input').send_keys("John")
    driver.find_element(By.NAME, 'last_name').send_keys("Doe")
    driver.find_element(By.CLASS_NAME, 'form-control.city').send_keys("Philadelphia")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()