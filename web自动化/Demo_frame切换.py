import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81'
           '/pagetest/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

# 1. 填写主页面的注册信息
time.sleep(2)
driver.find_element_by_id('userA').send_keys('admin')
# 2. 切换到A注册页面，填写注册页面A中的注册信息
time.sleep(2)
driver.switch_to.frame('idframe1')
driver.find_element_by_id('userA').send_keys('adminA')
# 恢复默认页面
driver.switch_to.default_content()
# 3. 切换到B注册页面，填写注册页面B中的注册信息
time.sleep(2)
driver.switch_to.frame('myframe2')
driver.find_element_by_id('userA').send_keys('adminB')

time.sleep(2)
driver.quit()

