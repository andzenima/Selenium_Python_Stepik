# lesson_3_2__13

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        self.driver.implicitly_wait(5)
        self.driver.get(link)

        self.driver.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('1_Name')
        self.driver.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('2_Name')
        self.driver.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('mail@example.com')

        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = self.driver.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()