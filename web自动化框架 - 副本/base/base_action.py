from selenium.webdriver.support.wait import WebDriverWait

# 父类
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)

    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    def click(self, feature):
        return self.find_el(feature).click()

    def clear(self, feature):
        return self.find_el(feature).clear()

    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    # 加了显示等待的元素定位方法
    def find_ele(self, feature, timeout=10, poll=1):
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(*feature))

    def find_eles(self, feature, timeout=10, poll=1):
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(*feature))