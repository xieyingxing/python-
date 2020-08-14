import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

# driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入电子邮箱"]').send_keys('123')
# driver.find_element(By.XPATH, '//*[@name="emailA"]').send_keys('123')



time.sleep(4)

driver.quit()