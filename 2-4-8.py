from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math




def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))


# Нажать на кнопку "Book"
book_submit = driver.find_element(By.ID, "book").click()


# Решить уже известную нам математическую задачу
x_element = driver.find_element(By.XPATH, '//span[@id = "input_value"]').text
y = calc(x_element)
text_area = driver.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(y)


button = driver.find_element(By.XPATH, '//button[@id = "solve"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()