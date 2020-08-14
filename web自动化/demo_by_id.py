import time

from selenium import webdriver

#执行浏览器驱动
driver = webdriver.Chrome()

#执行浏览器去访问
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4/'
           'python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81'
           '/pagetest/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')

time.sleep(5)

driver.quit()