import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

# 选择上海
time.sleep(2)
driver.find_element_by_css_selector('[value="sh"]').click()
# driver.find_element_by_xpath('//*[@id="selectA"]/option[2]').click()
# driver.find_element_by_css_selector('select[id=selectA] option[value="sh"]').click()
# 选择广州'
time.sleep(2)
driver.find_element_by_css_selector('[value="gz"]').click()
# 选择北京
time.sleep(2)
driver.find_element_by_css_selector('[value="sz"]').click()



time.sleep(2)
driver.quit()

