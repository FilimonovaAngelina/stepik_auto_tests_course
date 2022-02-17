from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#функция для вычисления суммы
def sum(x,y):
    return x+y

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

#Найдем числа, которые нужно сложить методом, вытащим .text
num1 = driver.find_element(By.XPATH, '//span[@id="num1"]').text
num2 = driver.find_element(By.XPATH, '//span[@id="num2"]').text

#Сумма
x, y = int(num1), int(num2)
num = sum(x, y)

#Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(num))

# Нажать кнопку "Submit"
text_area = driver.find_element(By.XPATH, '//button[@type="submit"]').click()




