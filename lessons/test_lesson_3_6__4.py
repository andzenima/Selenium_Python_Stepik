# lesson_3_6__3

import time
import math
import pytest
from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def credentials():
    with open("a_credentials.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    login, password = lines[0], lines[1]
    return login, password

def read_links():
    with open("a_links.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@pytest.fixture(params=read_links())
def link(request):
    return request.param

# 0 -------------------------------------
def wait_and_click(driver, locator, timeout=10, overlay_selector=".modal-dialog-bg"):
    # Ждём, пока пропадёт возможный оверлей (если он есть)
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, overlay_selector))
        )
    except:
        pass  # если оверлея нет — продолжаем

    # Ждём, пока элемент станет кликабельным
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    # Кликаем через JS (надежнее, чем обычный click)
    driver.execute_script("arguments[0].click();", element)
    return element
# 0 -------------------------------------


def test_login_stepik(driver, credentials, link):
    driver.get(link)
    login, password = credentials
    driver.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    driver.find_element(By.ID, "id_login_email").send_keys(login)
    driver.find_element(By.ID, "id_login_password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog__content")))

# 1 -------------------------------------

    # try:
    #     driver.find_element(By.CSS_SELECTOR, ".again-btn").click()
    #     try:
    #         time.sleep(2)
    #         driver.find_element(By.CSS_SELECTOR, ".modal-popup__container button:first-child").click()
    #     except NoSuchElementException:
    #         print("\n>>>>>> Нажата кнопка 'Решить снова'.")
    # except NoSuchElementException:
    #     print("\n>>>>>> Кнопки 'Решить снова' или 'Начать сначала(сброс)' не найдены.")
    #
    # answer = math.log(int(time.time()))
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, ".string-quiz__textarea").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, ".string-quiz__textarea").send_keys(answer)
    # # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    # # time.sleep(2)

# 2 -------------------------------------

    # try:
    #     driver.find_element(By.CSS_SELECTOR, ".again-btn").click()
    #     try:
    #         el1 = WebDriverWait(driver, 3).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-popup__container button:first-child")))
    #         el1.click()
    #     except NoSuchElementException:
    #         print("\n>>>>>> Нажата кнопка 'Решить снова'.")
    # except NoSuchElementException:
    #     print("\n>>>>>> Кнопки 'Решить снова' или 'Начать сначала(сброс)' не найдены.")


    # el2 = WebDriverWait(driver, 3).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".string-quiz__textarea")))
    # el2.click()
    #
    # answer = math.log(int(time.time()))
    #
    # el3 = WebDriverWait(driver, 3).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".string-quiz__textarea")))
    # el3.send_keys(answer)
    #
    # el4 = WebDriverWait(driver, 3).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    # el4.click()

# 3 -------------------------------------

    try:
        wait_and_click(driver, (By.CSS_SELECTOR, ".again-btn"))
        try:
            wait_and_click(driver, (By.CSS_SELECTOR, ".modal-popup__container button:first-child"))
        except NoSuchElementException:
            print("\n>>>>>> Нажата кнопка 'Решить снова'.")
    except NoSuchElementException:
        print("\n>>>>>> Кнопки 'Решить снова' или 'Начать сначала(сброс)' не найдены.")

    answer = math.log(int(time.time()))

    wait_and_click(driver, (By.CSS_SELECTOR, ".string-quiz__textarea"))
    driver.find_element(By.CSS_SELECTOR, ".string-quiz__textarea").send_keys(answer)

    wait_and_click(driver, (By.CSS_SELECTOR, ".submit-submission"))

    message = driver.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert message == "Correct!", f">>>>>> Получено послание от НЛО: '{message}'."