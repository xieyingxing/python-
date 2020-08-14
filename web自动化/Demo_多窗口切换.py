import time

from selenium import webdriver

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# 需求：打开注册页面A
driver.get('file:///D:/谢应兴/python测试代码/pagetest/注册A.html')
print('当前的页面句柄：',driver.current_window_handle)
# 1. 新窗口打开新浪
driver.find_element_by_id('fw').click()
handles = driver.window_handles
print('所有窗口的句柄：',handles)
# 2. 在新浪搜索框输入'新浪搜索'
## 切换到指定的窗口
driver.switch_to.window(handles[1])
# driver.find_element_by_class_name('inp-txt').send_keys('新浪搜索')
driver.find_element_by_class_name("inp-txt").clear()
driver.find_element_by_class_name("inp-txt").send_keys("1111111111111")
time.sleep(2)
# 3. 在注册页输入用户名admin
driver.switch_to.window(handles[0])
driver.find_element_by_id('userA').send_keys('admin')




# driver.find_element_by_id('fw').click()
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_name('SerchKey').clear()
# driver.find_element_by_name('SerchKey').send_keys('xxxxxx')
# time.sleep(2)
# driver.find_element_by_name('SearchSubButton').click()


time.sleep(2)
driver.quit()