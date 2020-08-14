import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A页面，完成以下操作
# 1.通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('admin')
driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '[class="telA"]').send_keys('18611111111')
driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys('123@qq.com')
# 2.间隔3秒，修改电话号码为：18600000000
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '[class="telA"]').clear()
driver.find_element(By.CSS_SELECTOR, '[class="telA"]').send_keys('18600000000')
# 3.间隔3秒，点击‘注册’按钮
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'button').click()
# 4.间隔3秒，关闭浏览器
time.sleep(3)
driver.quit()