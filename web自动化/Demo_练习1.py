import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.maximize_window() #浏览器窗口最大化
driver.get('https://www.baidu.com')

driver1 = driver.find_element(By.CSS_SELECTOR, '[id="kw"]')
driver1.send_keys('12306')
time.sleep(2)
driver1.clear()
driver1.send_keys('10010')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
# driver.refresh() ##刷新
print(driver.title)
print(driver.current_url)
# print(driver.get_cookie('BAIDUID'))
# print(driver.get_cookies())

time.sleep(3)
driver.quit()

