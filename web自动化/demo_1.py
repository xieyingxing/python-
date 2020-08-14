import time

from selenium import webdriver

#驱动浏览器对象
driver = webdriver.Chrome()

#使谷歌浏览器浏览百度
driver.get('https://www.baidu.com/s?wd=阿迪')

driver.find_element_by_link_text('阿迪达斯adidas中国官方网站').click()

driver.find_element_by_xpath('//*[@id="6"]/h3/a').click()

#暂停5秒
time.sleep(5)

#关闭浏览器

driver.quit()