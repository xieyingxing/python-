import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

# 设置js脚本控制滚动条 滚动到底部
js = 'window.scrollTo(0, 1080)'
# 回到顶部
js1 = 'window.scrollTo(0, 0)'
time.sleep(3)
# 执行js脚本
driver.execute_script(js)
time.sleep(3)
driver.execute_script(js1)


time.sleep(2)
driver.quit()

