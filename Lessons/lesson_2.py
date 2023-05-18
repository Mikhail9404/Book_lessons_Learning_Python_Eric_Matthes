# import time
# from selenium import webdriver # Импортируем webdriver(набор команд для управления браузером)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # Вызываем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# time.sleep(5) # Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# driver.get("https://google.ru") # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# time.sleep(5)
# textfield = driver.find_element_by_xpath("//input[@name='q']") # Метод find_element_by_xpath позволяет найти нужный элемент на сайте
# textfield.send_keys("погода на завтра") # Напишем текст в поле поиска
# time.sleep(5)
# submit_button = driver.find_element_by_xpath("//div[@jsname='VlcLAe']//input[@class='gNO89b']") # Укажем путь к кнопке поиска
# submit_button.click() # Нажмём на кнопку поиска с помощью команды .click(). После нажатия на кнопку должны появиться результаты поиска
# time.sleep(5)
# driver.quit() # Добавим команду, с помощью которой браузер будет сам закрываться после проведения теста

#------------------------------------------------

# Пример теста с использованием метода: # в тесте проверим, нашёлся ли на страничке логотип google
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.get("https://dns-shop.ru") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# logo = driver.find_element_by_id("header-logo") # укажем путь к логотипу (можно было написать и без части "logo=", почему так лучше, разберём в дальнейшем)
# driver.quit() # закроем драйвер в конце теста

#________________________________________________

# import time
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# # Логин в систему
# driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# login = driver.find_element_by_id("txtUsername") # объявляем переменную login, задаём ей значение селектора поля логин
# login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
# password = driver.find_element_by_id("txtPassword") # объявляем переменную password, задаём ей значение селектора поля пароль
# password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find…. .send_keys(..))
# login_btn = driver.find_element_by_id("btnLogin") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
# login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
# time.sleep(3)
# driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver

#________________________________________________
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("file:///C:/Users/misha/Downloads/doggo_memes%20(1).html")
# # elementByPartialLinkText = driver.find_element_by_partial_link_text('one thing') # -
# # elementByTitle = driver.find_element_by_css_selector[@title="one-thing"] # -
# # elementByID = driver.find_element_by_id('blocks') # +
# # elementByClass = driver.find_element_by_class_name("lead blocks-page") # -
# # elementByClass = driver.find_element_by_name("main") # +
# # driver.find_element(By.PARTIAL_LINK_TEXT, 'one thing') # -
# # elementByClass = driver.find_element_by_tag_name('article') # +
# # elementByClass = driver.find_element_by_class_name('card-text second')
# # elementByPartialLinkText = driver.find_element_by_partial_link_text('Bar doggo')
# elementByCSSSelector = driver.find_element_by_css_selector('p.card-text second')
# driver.find_element(By.CLASS_NAME, 'card-text second')
#
# driver.quit()
#________________________________
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("file:///C:/Users/misha/Downloads/doggo_memes.html")
# driver.find_elements_by_css_selector('body > main > div > div > div > div:nth-child(4) > div > div > div > div > button:nth-child(1)')
# # a = len(count)
# # print(a)
#
# driver.quit()
#_____________________________________
# import time
# from selenium import webdriver
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
# time.sleep(3)
# PimModule_btn = driver.find_element_by_id("menu_pim_viewPimModule")
# PimModule_btn.click()
# AddEmployee_btn = driver.find_element_by_id("menu_pim_addEmployee")
# AddEmployee_btn.click()
# first_name = driver.find_element_by_id("firstName")
# first_name.send_keys("Mikhail")
# last_name = driver.find_element_by_id("lastName")
# last_name.send_keys("Kuznetsov")
# time.sleep(3)
# btnSave = driver.find_element_by_id('btnSave')
# btnSave.click()
# time.sleep(3)
#
# driver.quit()
#_______________________________________________
# import time
# from selenium import webdriver
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
# time.sleep(3)
# PimModule_btn = driver.find_element_by_id("menu_pim_viewPimModule")
# PimModule_btn.click()
# chkbox_record = driver.find_element_by_id("ohrmList_chkSelectRecord_2") # Значение "Record_55" будет меняться при удалении пользователя
# chkbox_record.click()
# btn_Delete = driver.find_element_by_id('btnDelete')
# btn_Delete.click()
# btn_Ok = driver.find_element_by_id('dialogDeleteBtn')
# btn_Ok.click()
# time.sleep(3)
#
# driver.quit()
#____________________________________________
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

login = driver.find_element_by_id("user-name")
login.send_keys("standard_user")
password = driver.find_element_by_id("password")
password.send_keys("secret_sauce")
login_btn = driver.find_element_by_id("login-button")
login_btn.click()
btn_Backpack = driver.find_element_by_id('add-to-cart-sauce-labs-backpack')
btn_Backpack.click()
# btn_Jacket = driver.find_element_by_id('add-to-cart-sauce-labs-fleece-jacket') # 4 товар, для проверки подсчета
# btn_Jacket.click()
btn_BikeLight = driver.find_element_by_id('add-to-cart-sauce-labs-bike-light')
btn_BikeLight.click()
btn_Bolt_T_Shirt = driver.find_element_by_id('add-to-cart-sauce-labs-bolt-t-shirt')
btn_Bolt_T_Shirt.click()
time.sleep(3)
btn_shopping_cart_container = driver.find_element_by_id('shopping_cart_container')
btn_shopping_cart_container.click()
cart_item_label = driver.find_elements_by_class_name('cart_item_label')
count = len(cart_item_label)

if count == 3:
    print('Все верно! В корзине 3 товара!')
else:
    print('Ошибка! Количество товара в корзине:', count, end='!')

time.sleep(3)
driver.quit()