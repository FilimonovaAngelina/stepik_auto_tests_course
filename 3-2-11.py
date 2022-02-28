from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")

class TestClassName(unittest.TestCase):
    def test_first_name(self):
        first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your name"]').send_keys("Ivan")
        self.assertEqual(first_name, 'Input your name', "page_open_error")

    # def test_last_name(self):
    #     last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your name"]').send_keys("Petrov")
    #     self.assertEqual(last_name, 'Input your name', "name_past_error")

    def test_email(self):
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys("email@mail.ru")
        self.assertEqual(email, 'Input your email', "mail_past_error")

    def test_button(self):
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text_elt, 'Congratulations! You have successfully registered!', "button_click_error")

if __name__ == "__main__":
    unittest.main()



