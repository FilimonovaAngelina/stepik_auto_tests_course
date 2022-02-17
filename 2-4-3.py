from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()


# использование time sleep
# time.sleep(1)
# button = browser.find_element(By.ID, "verify").click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# Использование implicit wait
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify").click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text