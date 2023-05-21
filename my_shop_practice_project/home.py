# Задание 1
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
driver.get("http://practice.automationtesting.in/")
# Шаг 2
driver.execute_script("window.scrollBy(0, 600);")
# Шаг 3
selenium_ruby = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img')
selenium_ruby.click()
# Шаг 4
reviews_btm = driver.find_element_by_css_selector('#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a')
reviews_btm.click()
# Шаг 5
rating_5_stars = driver.find_element_by_css_selector('#commentform > p.comment-form-rating > p > span > a.star-5')
rating_5_stars.click()
# Шаг 6
your_review = driver.find_element_by_css_selector('#comment')
your_review.send_keys('Nice book!')
# Шаг 7
name = driver.find_element_by_id('author')
name.send_keys('Mikhail')
# Шаг 8
email = driver.find_element_by_id('email')
email.send_keys('Misha9404@yandex.ru')
# Шаг 9
submit = driver.find_element_by_id('submit')
submit.click()

time.sleep(3)
driver.quit()

