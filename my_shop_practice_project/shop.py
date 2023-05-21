# Задание 4
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
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
# my_acc_btm.click()
# Email_add = driver.find_element_by_id('username')
# Email_add.send_keys('kuznetsov.michail@bk.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('M!khailKUZ')
# login_btm = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
# login_btm.click()
# # Шаг 3
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 4
# html_5 = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img')
# html_5.click()
# # Шаг 5
# product_title_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#product-181 > div.summary.entry-summary > h1'),'HTML5 Forms'))
# print(product_title_check)
#
# time.sleep(3)
# driver.quit()
# Задание 5
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
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
# my_acc_btm.click()
# Email_add = driver.find_element_by_id('username')
# Email_add.send_keys('kuznetsov.michail@bk.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('M!khailKUZ')
# login_btm = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
# login_btm.click()
# # Шаг 3
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 4
# html_btm = driver.find_element_by_css_selector('#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a')
# html_btm.click()
# # Шаг 5
# product = driver.find_elements_by_class_name('product')
# count = len(product)
#
# if count == 3:
#     print('Все верно! На странице отображается 3 товара!')
# else:
#     print('Ошибка! На странице отображается:', count, end='товара!')
#
# time.sleep(3)
# driver.quit()

# Задание 6
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
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
# my_acc_btm.click()
# Email_add = driver.find_element_by_id('username')
# Email_add.send_keys('kuznetsov.michail@bk.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('M!khailKUZ')
# login_btm = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
# login_btm.click()
# # Шаг 3
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 4
# select_sorting = driver.find_element_by_class_name('orderby')
# select_sorting = select_sorting.get_attribute('value')
# if select_sorting == 'menu_order':
#     print("В селекотре Sorting выбран вариант сортировки по умолчанию")
# else:
#     print("В селекотре Sorting выбран вариант сортировки не по умолчанию")
# # Шаг 5
# select_sorting = driver.find_element_by_class_name('orderby')
# select = Select(select_sorting)
# select.select_by_value("price-desc")
# # Шаг 6
# select_sorting = driver.find_element_by_class_name('orderby')
# # Шаг 7
# select_sorting = select_sorting.get_attribute('value')
# if select_sorting == 'price-desc':
#     print("В селекотре Sorting выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("В селекотре Sorting не выбран вариант сортировки по цене от большей к меньшей")
#
# time.sleep(3)
# driver.quit()

# Задание 7
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
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# my_acc_btm = driver.find_element_by_css_selector('#menu-item-50 > a')
# my_acc_btm.click()
# Email_add = driver.find_element_by_id('username')
# Email_add.send_keys('kuznetsov.michail@bk.ru')
# password = driver.find_element_by_id('password')
# password.send_keys('M!khailKUZ')
# login_btm = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
# login_btm.click()
# # Шаг 3
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 4
# andr_quick_start = driver.find_element_by_css_selector('#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img')
# andr_quick_start.click()
# # Шаг 5
# book_old_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
# book_old_price_text = book_old_price.text
# assert book_old_price_text == '₹600.00'
# # Шаг 6
# book_new_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
# book_new_price_text = book_new_price.text
# assert book_new_price_text == '₹450.00'
# # Шаг 7
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images')))
# book_cover.click()
# # Шаг 8
# book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a')))
# book_cover_close.click()
#
# time.sleep(3)
# driver.quit()

# Задание 8
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
# driver.implicitly_wait(5)
#
# # Шаг 1
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 3
# add_cart_HTML5_web_dev = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# add_cart_HTML5_web_dev.click()
# time.sleep(3)
# # Шаг 4
# cart_contents = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
# cart_contents_text = cart_contents.text
# assert cart_contents_text == '1 Item'
# cost_contents = driver.find_element_by_css_selector('#wpmenucartli > a > span.amount')
# cost_contents = cost_contents.text
# assert cost_contents == '₹180.00'
# # Шаг 5
# cart = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
# cart.click()
# # Шаг 6
# subtotal = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span')
# subtotal_text = subtotal.text
# assert subtotal_text is not None
# # Шаг 7
# total = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span')
# total_text = total.text
# assert total_text is not None
#
#
# time.sleep(3)
# driver.quit()

# Задание 9
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
# driver.implicitly_wait(5)
#
# # Шаг 1
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# # Шаг 3
# driver.execute_script("window.scrollBy(0, 300);")
# add_cart_HTML5_web_dev = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# add_cart_HTML5_web_dev.click()
# time.sleep(3)
# add_cart_JS_Data = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# add_cart_JS_Data.click()
# # Шаг 4
# time.sleep(3)
# cart_btm = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
# cart_btm.click()
# # Шаг 5
# delete_cart_HTML_web_dev = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a')
# time.sleep(3)
# delete_cart_HTML_web_dev.click()
# # Шаг 6
# undo_btm = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a')
# undo_btm.click()
# # Шаг 7
# quantity = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# quantity.clear()
# quantity.send_keys('3')
# # Шаг 8
# update_basket = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button')
# update_basket.click()
# # Шаг 9
# quantity_update = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# quantity_update_result = quantity_update.get_attribute('value')
# assert quantity_update_result == '3'
# time.sleep(3)
# # Шаг 10
# apply_coupon = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button')
# time.sleep(3)
# apply_coupon.click()
# # Шаг 11
# error_message = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > ul > li')
# error_message_text = error_message.text
# assert error_message_text == 'Please enter a coupon code.'
#
# time.sleep(3)
# driver.quit()

# Задание 10
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
# driver.implicitly_wait(5)
#
# # Шаг 1
# driver.get("http://practice.automationtesting.in/")
# # Шаг 2
# shop_btm = driver.find_element_by_css_selector('#menu-item-40 > a')
# shop_btm.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # Шаг 3
# add_cart_HTML5_web_dev = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# add_cart_HTML5_web_dev.click()
# # Шаг 4
# time.sleep(1)
# cart_btm = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
# cart_btm.click()
# # Шаг 5
# proceed_to_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > div > a')))
# proceed_to_check.click()
# # Шаг 6
# first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_first_name')))
# first_name.send_keys('Mikhail')
# last_name = driver.find_element_by_css_selector('#billing_last_name')
# last_name.send_keys('Kuznetsov')
# email_add = driver.find_element_by_css_selector('#billing_email')
# email_add.send_keys('Misha9404@yandex.ru')
# phone = driver.find_element_by_css_selector('#billing_phone')
# phone.send_keys('1234567890')
# country_select = driver.find_element_by_link_text('Russia')
# country_select.click()
# find_country_select = driver.find_element_by_css_selector('#s2id_autogen1_search')
# find_country_select.send_keys('Russia')
# select_country = driver.find_element_by_css_selector('#select2-results-1 > li')
# select_country.click()
# address = driver.find_element_by_css_selector('#billing_address_1')
# address.send_keys('Pushkina, 13')
# town = driver.find_element_by_css_selector('#billing_city')
# town.send_keys('St.Petersburg')
# state = driver.find_element_by_css_selector('#billing_state')
# state.send_keys('Russia')
# postcode = driver.find_element_by_css_selector('#billing_postcode')
# postcode.send_keys('187015')
# # Шаг 7
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check_payments = driver.find_element_by_css_selector('#payment_method_cheque')
# check_payments.click()
# # Шаг 8
# place_order_btm = driver.find_element_by_css_selector('#place_order')
# place_order_btm.click()
# # Шаг 9
# commerce_order = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
# # Шаг 19
# check_payment = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td'),'Check Payments'))
#
# time.sleep(3)
# driver.quit()