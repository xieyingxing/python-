import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///D:/谢应兴/python测试代码/pagetest/注册A.html')

driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_name('passwordA').send_keys('123456')
driver.find_element_by_class_name('telA').send_keys('1888888888')
driver.find_element_by_tag_name('input').send_keys('18888888888@qq.com')
driver.find_elements_by_tag_name('input')[3].send_keys('18888888888@qq.com')
driver.find_element_by_link_text('访问 新浪 网站').click()
driver.find_element_by_partial_link_text('百').click()

# # =======xparth定位
# # 绝对路径定位
# driver.find_element_by_xpath('/html/body/div/fieldset/form/p[1]/input').send_keys('123')
# # 相对路径定位
# driver.find_element_by_xpath('//*[@id="userA"]').send_keys('admin')
#
# # 属性定位
# driver.find_element_by_xpath('//*[@id="userA"]').send_keys('admin')
#
# # 属性与逻辑结合定位
# driver.find_element_by_xpath('//*[@type="text" and @name="user-test"]').send_keys('123456')
#
# # 属性与层级结合
# driver.find_element_by_xpath('//*[@id="p1"]/input').send_keys('123')
#
# # xpath扩展
# # //*[text()="xxx"] 文本内容是xxx的元素
# driver.find_element_by_xpath('//*[text()="打开百度"]').click()
#
# # //*[contains(@属性,"元素")] 属性中含有xxx的元素
# driver.find_element_by_xpath('//*[contains(@class,"login")]').send_keys('123')
#
# # //*[starts-with(@attribute,'xxx')] 属性以xxx开头的元素
# driver.find_element_by_xpath('//*[starts-with(@class,"lo")]').send_keys('123')
#
# #======css定位
# # id定位
# driver.find_element_by_css_selector('#telA').send_keys('admin')
#
# # class定位
# driver.find_element_by_css_selector('.emailA').send_keys('18888888888')
#
# # 元素定位
# driver.find_element_by_css_selector('button').click()
# driver.find_elements_by_css_selector('input')[1].send_keys('123')
#
# # 属性定位
# driver.find_element_by_css_selector('[name="user-test"]').send_keys('123456')
# driver.find_elements_by_css_selector('[name="user-test"]')[1].send_keys('123456')
#
# # 层级定位
# #直接子元素
# driver.find_element_by_css_selector('p[id="p4"]>input').send_keys('123')
# #后代元素
# driver.find_element_by_css_selector('div[class="zc"] input').send_keys('123')
# driver.find_elements_by_css_selector('div[class="zc"] input')[2].send_keys('123')


time.sleep(4)
driver.quit()