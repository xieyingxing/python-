import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window() #浏览器窗口最大化
driver.get('file:///D:/谢应兴/python测试代码/pagetest/注册A.html')

ActionChains(driver).context_click(driver.find_element(By.ID, 'userA')).perform()
driver.find_element_by_id('userA').send_keys('admin')
ActionChains(driver).double_click(driver.find_element(By.ID, 'userA')).perform()

time.sleep(3)
driver.quit()