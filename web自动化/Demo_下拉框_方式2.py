import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%B0%A2%E5%BA%94%E5%85%B4'
           '/python%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/pagetest/%E6%B3%A8%E5%86%8CA.html')

select = Select(driver.find_element_by_id('selectA'))

# 选择上海 #角标定位
time.sleep(2)
select.select_by_index(1)
# 选择广州 #根据值（value）定位
time.sleep(2)
select.select_by_value('gz')
# 选择北京 #文本定位
time.sleep(2)
select.select_by_visible_text('北京')



time.sleep(2)
driver.quit()

