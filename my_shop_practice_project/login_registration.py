# Задание 2
# __________________________________________________________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# # Шаг 1
# driver.get(" http://practice.automationtesting.in/")
# # Шаг 2
# my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
# my_acc_btm.click()
# # Шаг 3
# Email_add = driver.find_element_by_id('reg_email')
# Email_add.send_keys('kuznetsov.michail@bk.ru')
# # Шаг 4
# password = driver.find_element_by_id('reg_password')
# password.send_keys('M!khailKUZ')
# # Шаг 5
# register_btm = driver.find_element_by_class_name('register')
# register_btm.click()
#
# time.sleep(3)
# driver.quit()

# Задание 3
# __________________________________________________________________

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# Шаг 1
driver.get(" http://practice.automationtesting.in/")
# Шаг 2
my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
my_acc_btm.click()
# Шаг 3
Email_add = driver.find_element_by_id('username')
Email_add.send_keys('kuznetsov.michail@bk.ru')
# Шаг 4
password = driver.find_element_by_id('password')
password.send_keys('M!khailKUZ')
# Шаг 5
login_btm = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
login_btm.click()
# Шаг 6
logout_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#page-36 > div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a')))

time.sleep(3)
driver.quit()

# # Задание
# __________________________________________________________________