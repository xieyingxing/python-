import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/drag.html')

ActionChains(driver).drag_and_drop(driver.find_element(By.ID, 'div1'), driver.find_element_by_id('div2')).perform()

time.sleep(2)
driver.quit()