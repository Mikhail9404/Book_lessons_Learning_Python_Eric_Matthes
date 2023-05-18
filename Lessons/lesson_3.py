# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# login = driver.find_element_by_id("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_id("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_id("btnLogin")
# login_btn.click()
# PimModule_btn = driver.find_element_by_id("menu_pim_viewPimModule")
# PimModule_btn.click()
# time.sleep(3)
#
# pending_approval = driver.find_element_by_id("ohrmList_chkSelectRecord_54")
# pending_approval_checked = pending_approval.get_attribute("checked")
# print("value of pending approval checkbox: ", pending_approval_checked)
# if pending_approval_checked is not None:
#     print("Чекбокс отмечен")
# else:
#     print("Чекбокс НЕ отмечен")

# scheduled = driver.find_element_by_id("leaveList_chkSearchFilter_2")
# scheduled_checked = scheduled.get_attribute("checked")
# print("value of sheduled checkbox: ", scheduled_checked)
# # if scheduled_checked is None:
# #     print("Атрибута нет")
# # else:
# #     print("Атрибут есть")
#
# element = driver.find_element_by_id("leaveList_cmbSubunit") # "element" это просто название переменной, можно задать и другое
# select = Select(element) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
# select.select_by_value("2") # ищем элемент с текстом "Sales" ; в этом и предыдущем методе добавлять .click() не нужно


# driver.quit()
#______________________________

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# # Шаг №2
# login = driver.find_element_by_id("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_id("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_id("btnLogin")
# login_btn.click()
#
# # Шаг №3
# PimModule_btn = driver.find_element_by_id("menu_pim_viewPimModule")
# PimModule_btn.click()
# choice_name = driver.find_element_by_css_selector('#resultTable > tbody > tr:nth-child(3) > td:nth-child(3) > a')
# choice_name.click()
# time.sleep(3)
#
# # Шаг №4
# radio_gender = driver.find_element_by_css_selector("[type = 'radio']")
# radio_gender_disabled = radio_gender.get_attribute("disabled")
# print("Наличие атрибута disable: ", radio_gender_disabled)
#
# if radio_gender_disabled is None:
#     print("Радиокнопка с противоположным полом сотрудника в данный момент доступна для выбора")
# else:
#     print("Радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора")
#
# # Шаг №5
# selector_cmbNation = driver.find_element_by_id("personal_cmbNation")
# selector_cmbNation_disabled = selector_cmbNation.get_attribute("disabled")
#
# if selector_cmbNation_disabled is None:
#     print("Селектор Nationality в данный момент доступен для выбора")
# else:
#     print("Селектор Nationality в данный момент недоступен для выбора")
#
# # Шаг №6
# button_edit = driver.find_element_by_id('btnSave')
# button_edit.click()
# time.sleep(3)
#
# # Шаг №7
# radio_optGender = driver.find_element_by_id('personal_optGender_2')
# radio_optGender.click()
# time.sleep(3)
#
# # Шаг №8
# optGender_checked = radio_optGender.get_attribute('checked')
# if optGender_checked is not None:
#     print("Радиокнопка гендера выбрана на противоположный пол")
# else:
#     print("Радиокнопка гендера не выбрана на противоположный пол")
#
# # Шаг №9
# select_nationality = driver.find_element_by_id("personal_cmbNation")
# select = Select(select_nationality)
# select.select_by_value("193")
# time.sleep(3)
#
# # Шаг №10
# select_nationality_zimbabwean = select_nationality.get_attribute('value')
# if select_nationality_zimbabwean == '193':
#     print("В селекотре Nationality выбрана последняя страна в списке")
# else:
#     print("В селекотре Nationality выбрана не последняя страна в списке")
#
# # Шаг №11
# radio_optGender_default = driver.find_element_by_id('personal_optGender_1')
# radio_optGender_default.click()
# select_nationality = driver.find_element_by_id("personal_cmbNation")
# select = Select(select_nationality)
# select.select_by_value("0")
# time.sleep(3)
#
# # Шаг №12
# button_edit.click()
# time.sleep(3)
#
# driver.quit()

#______________________________________

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 2
# driver.get("http://demo.automationtesting.in/Register.html")
# # Шаг 3
# first_name = driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(1) > div:nth-child(2) > input")
# first_name.send_keys("Mikhail")
# last_name = driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(1) > div:nth-child(3) > input")
# last_name.send_keys("Kuznetsov")
# email = driver.find_element_by_css_selector("#eid > input")
# email.send_keys("Misha9404@yandex.ru")
# phone = driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(4) > div > input")
# phone.send_keys("9118249700")
# gender = driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(1) > input")
# gender.click()
# select_year = driver.find_element_by_id("yearbox")
# select = Select(select_year)
# select.select_by_value("1994")
# select_month = driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(11) > div:nth-child(3) > select")
# select = Select(select_month)
# select.select_by_value("April")
# select_day = driver.find_element_by_id("daybox")
# select = Select(select_day)
# select.select_by_value("4")
# first_password = driver.find_element_by_id("firstpassword")
# first_password.send_keys("Qw544739")
# second_password = driver.find_element_by_id("secondpassword")
# second_password.send_keys("Qw544739")
# # Шаг 4
# file = ('C:\\Users\\misha\\OneDrive\\Рабочий стол\\Testing\\Example.jpg')
# upload = driver.find_element_by_id("imagesrc")
# upload.send_keys(file)
# # Шаг 5
# driver.execute_script("window.scrollBy(0, 300);")
# # Шаг 6
# submit_btn = driver.find_element_by_id("submitbtn")
# submit_btn.click()
# # Шаг №7
# current_page = driver.current_url
# expected_address = 'http://demo.automationtesting.in/WebTable.html'
# if current_page == expected_address:
#     print('Адрес страницы совпадает!')
# else:
#     print('Адрес страницы не совпадает, фактический:', current_page)
#     print('Ожидаемый:', expected_address)
#
# time.sleep(3)
# driver.quit()
# __________________________________

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 1
# driver.get('http://demo.automationtesting.in/WebTable.html')
# # Шаг 2
# switch_to_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > a')
# switch_to_btn.click()
# aletrs_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li.dropdown.open > ul > li:nth-child(1) > a')
# aletrs_btn.click()
# # Шаг 3
# click_alert_btn = driver.find_element_by_css_selector('#OKTab > button')
# click_alert_btn.click()
# # Шаг 4
# alert = driver.switch_to.alert
# alert_text = alert.text
# if alert_text == 'I am an alert box!':
#     print('Текст ошибки: I am an alert box!')
# else:
#     print('Ошибка! Текста ошибки:', alert_text)
# alert.accept()
# # Шаг 5
# current_page = driver.current_url
# print('Адрес текущей ссылки:', current_page)
# # Шаг 6
# driver.execute_script("window.open();")
# new_window = driver.window_handles[1]
# driver.switch_to.window(new_window)
# driver.get(current_page)
#
# # Шаг 7
# alert_btn1 = driver.find_element_by_css_selector('body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(2) > a')
# alert_btn1.click()
# time.sleep(3)
# alert_btn2 = driver.find_element_by_css_selector('#CancelTab > button')
# alert_btn2.click()
# time.sleep(3)
# # Шаг 8
# confirm = driver.switch_to.alert
# confirm.dismiss()
# # Шаг 9
# driver.execute_script("window.open();")
# new_window_2 = driver.window_handles[2]
# driver.switch_to.window(new_window_2)
# driver.get(current_page)
# # Шаг 10
# alert_btn3 = driver.find_element_by_css_selector('body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(3) > a')
# alert_btn3.click()
# alert_btn4 = driver.find_element_by_css_selector('#Textbox > button')
# alert_btn4.click()
# time.sleep(3)
# # Шаг 11
# prompt = driver.switch_to.alert
# prompt.send_keys("Ура! Задание выполнено!")
# prompt.accept()
#
# time.sleep(3)
# driver.quit()
#_________________________________
# Закрытие рекламы на сайтах

# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Пользователи\misha\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://demo.automationtesting.in/WebTable.html")
#_______________________________

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 1
# driver.get("http://demo.automationtesting.in/WebTable.html")
# # Шаг 2
# more_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > a')
# more_btn.click()
# loader_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > ul > li:nth-child(6) > a')
# loader_btn.click()
# # Шаг 3
# run_changes_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#loader")))
# # Шаг 4
# run_btn = driver.find_element_by_id('loader')
# run_btn.click()
# # Шаг 5
# some_element = WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#myModal > div > div > div.modal-body > p"), "Lorem"))
# # Шаг 6
# save_chang_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '#myModal > div > div > div.modal-footer > button.btn.btn-primary')))
# # Шаг 7
# save_btn = driver.find_element_by_css_selector('#myModal > div > div > div.modal-footer > button.btn.btn-primary')
# save_btn.click()
#
# time.sleep(3)
# driver.quit()
#______________________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 1
# driver.get("http://demo.automationtesting.in/WebTable.html")
# # Шаг 2
# driver.implicitly_wait(5)
# # Шаг 3
# more_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > a')
# more_btn.click()
# dyn_dat_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > ul > li:nth-child(2) > a')
# dyn_dat_btn.click()
# # Шаг 4
# h_window = driver.find_element_by_css_selector('body > section > div:nth-child(1) > div > div > h3')
# h_window_text = h_window.text
# assert "Loading the data Dynamically" in h_window_text
# print(h_window_text)
# # Шаг 5
# get_dyn_dat_btn = driver.find_element_by_id('save')
# get_dyn_dat_btn.click()
# time.sleep(3)
# # Шаг 6
# photo = driver.find_element_by_css_selector('#loading > img')
# photo_src = photo.get_attribute('src')
# print(photo_src)
#
# time.sleep(3)
# driver.quit()
#________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 1
# driver.get("http://demo.automationtesting.in/WebTable.html")
# # Шаг 2
# driver.implicitly_wait(5)
# # Шаг 3
# more_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > a')
# more_btn.click()
# file_up = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > ul > li:nth-child(4) > a')
# file_up.click()
# # Шаг 4
# file = ('C:\\Users\\misha\\OneDrive\\Рабочий стол\\Testing\\Example.jpg')
# upload = driver.find_element_by_id("input-4")
# upload.send_keys(file)
# time.sleep(3)
# # Шаг 5
# remove_btn = driver.find_element_by_css_selector('body > section > div:nth-child(1) > div > div > div.file-input > button.btn.btn-default.fileinput-remove.fileinput-remove-button > span')
# remove_btn.click()
# time.sleep(3)
# # Шаг 6
# file_2 = ('C:\\Users\\misha\\OneDrive\\Рабочий стол\\Testing\\Example_empty.png')
# upload.send_keys(file_2)
# time.sleep(3)
# # Шаг 7
# close_btn = driver.find_element_by_css_selector('body > section > div:nth-child(1) > div > div > div.file-input.has-error > div.file-preview > div.file-drop-disabled > div.kv-fileinput-error.file-error-message > span')
# close_btn.click()
# # Шаг 7 (доп. условие)
# upload_btn = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "body > section > div:nth-child(1) > div > div > div.file-input.has-error > button.btn.btn-default.fileinput-upload.fileinput-upload-button > span")) )
#
#
# time.sleep(3)
# driver.quit()
#_______________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# # Шаг 1
# driver.get("http://demo.automationtesting.in/WebTable.html")
# # Шаг 2
# driver.implicitly_wait(5)
# # Шаг 3
# more_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > a')
# more_btn.click()
# jquery = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(9) > ul > li:nth-child(5) > a')
# jquery.click()
# # Шаг 4
# start_download_btn_check = WebDriverWait(driver, 10).until_not(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button')))
# # Шаг 5
# start_dwn_load_btn = driver.find_element_by_id('downloadButton')
# start_dwn_load_btn.click()
# # Шаг 6
# cancel_dwn_load_btn = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(By.CSS_SELECTOR, 'body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button'),'Cancel Download')
# # Шаг 7
# close_btn_text = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset > button"), "Cancel Download"))
# close_btn.click()
# # Шаг 8
# start_dwn_load_btn.click()
# window_text = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete!"))
#
#
# time.sleep(3)
# driver.quit()
#______________________________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Пользователи\misha\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.create_options()
# driver.maximize_window()
# # Шаг 1
# driver.get("http://demo.automationtesting.in/WebTable.html")
# # Шаг 2
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# # Шаг 3
# sw_to_wind_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > a')
# sw_to_wind_btn.click()
# windows_btn = driver.find_element_by_css_selector('#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > ul > li:nth-child(2) > a')
# windows_btn.click()
# # Шаг 4
# click_btn = driver.find_element_by_css_selector('#Tabbed > a > button')
# click_btn.click()
# # Шаг 5
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(3)
# # Шаг 6
# mult_wind_btn = driver.find_element_by_css_selector('body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(3) > a')
# mult_wind_btn.click()
# time.sleep(3)
# click_2_btn = driver.find_element_by_css_selector('#Multiple > button')
# click_2_btn.click()
# # Шаг 7
# driver.switch_to.window(driver.window_handles[2])
# time.sleep(3)
# # Шаг 8
# link_check = WebDriverWait(driver, 10).until(EC.url_to_be('http://demo.automationtesting.in/Index.html'))
# # Шаг 9
# number_of_tabs = wait.until(EC.number_of_windows_to_be(3))
# print(number_of_tabs)
# # Шаг 10
# email = driver.find_element_by_css_selector('#email')
# email.send_keys('Misha9404@yandex.ru')
# btn_go = driver.find_element_by_css_selector('#enterimg')
# btn_go.click()
# # Шаг 11
# link_check = WebDriverWait(driver, 10).until(EC.url_to_be('http://demo.automationtesting.in/Register.html'))
#
# time.sleep(3)
# driver.quit()
#________________________________
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Пользователи\misha\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.create_options()
# driver.maximize_window()
# # Шаг 1
# driver.get("https://www.google.ru/")
# driver.find_element_by_id("button")
#
# driver.quit()
#__________________

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

pageurl = 'https://www.google.com'
driver.get(pageurl)
x = 'some value'
driver.execute_script("alert('{}')".format(x))