from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    y = calc(int(x))

    answer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    answer.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()