import time
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录

driver = webdriver.Chrome(options = option)
time.sleep(5)
driver.get('https://www.baidu.com')

time.sleep(2)
driver.quit()
