import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4/'
           'python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_class_name('telA').send_keys('18888888888')

driver.find_element_by_class_name('emailA').send_keys('18888888888@qq.com')

time.sleep(5)

driver.quit()