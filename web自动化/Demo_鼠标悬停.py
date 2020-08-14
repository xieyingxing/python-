import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window() #浏览器窗口最大化
driver.get('file:///D:/谢应兴/python测试代码/pagetest/注册A.html')

ActionChains(driver).move_to_element(driver.find_element_by_tag_name('button')).perform()

time.sleep(3)
driver.quit()