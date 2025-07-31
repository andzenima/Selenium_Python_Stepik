# lesson_2.4_8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element(By.ID, "book").click()

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)
    print(x)

    ans = driver.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(str(math.log(abs(12 * math.sin(x)))))

    driver.find_element(By.CSS_SELECTOR, "#solve").click()

    time.sleep(3)

    aLRT = driver.switch_to.alert
    print(aLRT.text[(aLRT.text.index(': ')) + 2:])