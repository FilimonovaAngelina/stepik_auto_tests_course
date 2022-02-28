from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# мат. функция
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")

# Считать значение для переменной x
x = driver.find_element(By.XPATH, '//span[@id="input_value"]').text

# Посчитать математическую функцию от x
x_elem = calc(x)

# Проскроллить страницу вниз
button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

# Ввести ответ в текстовое поле
text = driver.find_element(By.XPATH, '//input[@id="answer"]').send_keys(x_elem)

# Выбрать checkbox "I'm the robot", Переключить radiobutton "Robots rule!", Нажать на кнопку "Submit"
for xpath in ['//input[@type="checkbox"]', '//input[@id="robotsRule"]', '//button[@type="submit"]']:
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.find_element(By.XPATH, xpath).click()

