import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_css_selector('[id="prompta"]').click()

# 获取弹出框对象
alert = driver.switch_to.alert
# 获取弹出框文本信息
print(alert.text)
# driver.find_element_by_id('id="prompta"').send_keys('123')
time.sleep(2)
# 确认对话框
alert.accept()
time.sleep(2)
# 在用户名输入框输入‘admin’
driver.find_element_by_id('userA').send_keys('admin')

time.sleep(2)
driver.quit()

