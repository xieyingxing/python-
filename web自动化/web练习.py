import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get('http://localhost/')
# 账号不存在
# 1. 点击首页的 ‘登录’ 链接，进入登录页面
driver.find_element_by_class_name('red').click()
# 2. 输入一个不存在的用户名
driver.find_element_by_id('username').send_keys('13535101252')
# 3. 输入密码
driver.find_element_by_id('password').send_keys('123456')
# 4. 输入验证码
driver.find_element_by_id('verify_code').send_keys('8888')
# 5. 点击登录按钮
driver.find_element_by_name('sbtbutton').click()
# 6. 获取错误提示信息
msg = driver.find_element_by_css_selector(".layui-layer-content").text
print(msg)


# time.sleep(3)
# driver.quit()







# # 密码错误
# # 1. 点击首页的 ‘录’ 链接，进入登录页面
# driver.find_element_by_class_name('red').click()
# # 2. 输入用户名
# driver.find_element_by_id('username').send_keys('13535101255')
# # 3. 输入一个错误的密码
# driver.find_element_by_id('password').send_keys('1234')
# # 4. 输入验证码
# driver.find_element_by_id('verify_code').send_keys('8888')
# # 5. 点击登录按钮
# driver.find_element_by_name('sbtbutton').click()
# # 6. 获取错误提示信息
# a = driver.find_element_by_css_selector('.layui-layer-content').text
# print(a)

time.sleep(3)
driver.quit()
