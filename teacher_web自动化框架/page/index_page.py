from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class IndexPage(BaseAction):

    # 登录链接
    login_link = By.CLASS_NAME, "red"

    def click_login_link(self):
        return self.click(self.login_link)