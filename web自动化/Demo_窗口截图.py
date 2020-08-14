import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_id('userA').send_keys('admin')
time.sleep(2)
# driver.get_screenshot_as_file('./png/123.png')
# imgpath = './png/xyx_{}.png'.format(time.strftime("%Y%m%d%H%M%S"))
driver.get_screenshot_as_file('./png/xyx_{}.png'.format(time.strftime("%Y%m%d%H%M%S")))

driver.quit()
