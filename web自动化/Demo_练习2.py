import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window() #浏览器窗口最大化
driver.get('file:///D:/谢应兴/python测试代码/pagetest/注册A.html')

# 需求：使用‘注册A.html’页面，完成以下操作：
# 1.获取用户名输入框的大小
print(driver.find_element(By.CSS_SELECTOR, '[type="text"]').size)
# 2.获取页面上第一个超链接的文本内容
print(driver.find_element(By.TAG_NAME, 'a').text)
# 3.获取页面上第一个超链接的地址
print(driver.find_element_by_tag_name("a").get_attribute("href"))
# 4.判断页面中的span标签是否可见
print(driver.find_element_by_tag_name('span').is_displayed())
# 5.判断页面中取消按钮是否可用
print(driver.find_element_by_id("cancelA").is_enabled())
# 6.判断页面中'旅游'对应的复选框是否为选中的状态
print(driver.find_element_by_id("lyA").is_selected())

time.sleep(3)
driver.quit()