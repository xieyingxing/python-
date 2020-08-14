import time

from selenium import webdriver
driver = webdriver.Chrome()
# 账号不存在
# 1. 点击首页的 ‘登录’ 链接，进入登录页面
driver.get('http://localhost:8088/logins')
# 2. 输入一个不存在的用户名
driver.find_element_by_name('userName').send_keys('123')
# 3. 输入密码
driver.find_element_by_name('password').send_keys('123')
# 4. 输入验证码
driver.find_element_by_name('code').send_keys('qwer')
# 5. 点击登录按钮
driver.find_element_by_class_name('btn_login').click()
# 6. 获取错误提示信息
# alert = driver.switch_to.alert
# print(alert.text)
print(driver.find_element_by_css_selector("body > div.cotn_principal > div > div > div.cont_forms.cont_forms_active_login > form > div > div.alert.alert-danger.alert-dismissible").text)

time.sleep(3)
driver.quit()







# 密码错误
# 1. 点击首页的 ‘登录’ 链接，进入登录页面
# 2. 输入用户名
# 3. 输入一个错误的密码
# 4. 输入验证码
# 5. 点击登录按钮
# 6. 获取错误提示信息