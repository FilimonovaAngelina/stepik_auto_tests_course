from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/get_attribute.html
driver.get("http://suninjuly.github.io/get_attribute.html")

# Найти элемент-картинку/ Взять у этого элемента значение атрибута valuex
x_valuex = driver.find_element(By.XPATH, '//img[@id="treasure"]').get_attribute("valuex")
y = calc(x_valuex)

# Ввести ответ в текстовое поле
text_area = driver.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

# Отметить checkbox Выбрать radiobutton Нажать на кнопку Отправить.
for selector in ['//input[@type="checkbox"]', '//input[@id="robotsRule"]', '//button[@type="submit"]']:
    driver.find_element_by_xpath(selector).click()


