from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")

# Нажать кнопку
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

# Принять confirm
confirm = driver.switch_to.alert
confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
x_element = driver.find_element_by_id("input_value").text
y = calc(x_element)
text_area = driver.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary")]').click()
