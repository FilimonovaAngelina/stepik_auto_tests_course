from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

# Заполнить текстовые поля: имя, фамилия, email
driver.find_element(By.XPATH, '//input[@name="firstname"]').send_keys("Angelina")
driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys("Filimonova")
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("filimonova807@gmail.com")

# Загрузить файл
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = driver.find_element(By.XPATH, '//input[@type="file"]')
element.send_keys(file_path)

# Нажать кнопку "Submit"
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(10)