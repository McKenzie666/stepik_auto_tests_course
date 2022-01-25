from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from math import fabs, sqrt, sin, pi
from selenium.webdriver.support.ui import Select
import os


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    browser.window_handles[1]

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()