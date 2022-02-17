from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id("input_value").text
y = calc(x_element)

text_area = browser.find_element(By.XPATH, '//input[@id="answer"]')
text_area.send_keys(y)

for selector in ['//input[@type="checkbox"]', '//input[@id="robotsRule"]', '//button[@type="submit"]']:
    browser.find_element_by_xpath(selector).click()




