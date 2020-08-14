import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

## 隐式等待
# driver.implicitly_wait(7)
# driver.find_element_by_css_selector('[placeholder="延时加载的输入框"]').send_keys('123')

## 显式等待
# wait = WebDriverWait(driver,10,0.5)
# # element = wait.until(lambda x: x.find_element(By.CSS_SELECTOR, '[placeholder="延时加载的输入框"]'))
# # element.send_keys('123')

WebDriverWait(driver,10,0.5).until\
    (lambda x: x.find_element(By.CSS_SELECTOR, '[placeholder="延时加载的输入框"]')).send_keys('123')

time.sleep(2)
driver.quit()