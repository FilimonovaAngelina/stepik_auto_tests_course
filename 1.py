from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")

input1 = driver.find_element_by_tag_name("input")
input1.send_keys("Ivan")

input2 = driver.find_element_by_name("last_name")
input2.send_keys("Petrov")

input3 = driver.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")

input4 = driver.find_element_by_id("country")
input4.send_keys("Russia")

button = driver.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)	
# закрываем браузер после всех манипуляций	
driver.quit()

