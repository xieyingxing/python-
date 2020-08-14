import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A页面，完成以下操作
# 1. 输入用户名：admin1，暂停2秒，删除1
driver1 = driver.find_element_by_id('userA')
driver1.send_keys('admin1')
time.sleep(2)
driver1.send_keys(Keys.BACK_SPACE) ##删除
time.sleep(2)
# 2. 全选用户名：admin，暂停2秒
driver1.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 3. 复制用户名：admin，暂停2秒
driver1.send_keys(Keys.CONTROL, 'c')
time.sleep(2)
# 4. 粘贴到电话框
driver.find_element(By.CSS_SELECTOR, '[class="telA"]').send_keys(Keys.CONTROL, 'v')


time.sleep(2)
driver.quit()