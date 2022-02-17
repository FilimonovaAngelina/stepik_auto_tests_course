from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.XPATH, '//input[contains(@class,"city")]')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.XPATH, '//input[@id="country"]')
    input4.send_keys("Russia")
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла