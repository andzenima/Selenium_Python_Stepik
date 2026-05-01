from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/huge_form.html")

    elemets = driver.find_elements(By.CSS_SELECTOR, 'input')
    for element in elemets:
        element.send_keys("Answer")

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = driver.switch_to.alert
    print(alert.text.split(": ")[1])
    alert.accept()
