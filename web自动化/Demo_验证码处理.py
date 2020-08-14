import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
time.sleep(2)
driver.add_cookie({'name':'BDUSS',
                   'value':'VocUNoT05Pa1NpeX5IZmp5NmR6bUlxbkRZQlI3UDc5WmhZaDZKcnFvT3VTbGhmSUFBQUFBJCQAAAAAAAAAAAEAAACOFb1wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK69MF-uvTBfNE'})

driver.refresh()

time.sleep(2)
driver.quit()
