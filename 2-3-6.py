from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

# Нажать кнопку
driver.find_element(By.XPATH, '//button[@type="submit"]').click()


# Переключиться на новую вкладку
driver.switch_to.window(driver.window_handles[1])

# На новой странице решить капчу для роботов, чтобы получить число с ответом
x_element = driver.find_element(By.XPATH,'//span[@id = "input_value"]').text
y = calc(x_element)
text_area = driver.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary")]').click()

alert = driver.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]


# ввод ответа на Stepik
driver.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)

driver.find_element(By.XPATH, '//input[@id="id_login_email"]').send_keys('filimonova807@gmail.com')# здесь вводится e-mail
driver.find_element(By.XPATH, '//input[@id="id_login_password"]').send_keys('Uv63Aj7V')# здесь вводится пароль

driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(3)
driver.get('https://stepik.org/lesson/184253/step/6?thread=solutions&unit=158843')
time.sleep(3)

answer_input = driver.find_element(By.XPATH, '//textarea[contains(@class, "ember")]')
driver.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

button = driver.find_element(By.XPATH, '//button[@class="submit-submission"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
button.click()