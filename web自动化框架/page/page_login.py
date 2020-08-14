from selenium.webdriver.common.by import  By

from base.base_action import BaseAction

# 子类
class PageLogin(BaseAction):

    # 用户名输入框
    username_input = By.ID, "username"
    # 密码输入框
    password_input = By.ID, "password"
    # 验证码输入框
    verify_code_input = By.ID, "verify_code"
    # 登录按钮
    login_btn = By.NAME, "sbtbutton"
    # 消息框
    msg = By.CSS_SELECTOR, ".layui-layer-content"

    # def find_el(self, feature):
    #     return self.driver.find_element(*feature)

    def get_username(self, data):
        return self.find_el(self.username_input).send_keys(data)

    def get_password(self, data):
        return self.find_el(self.password_input).send_keys(data)

    def get_code(self, data):
        return self.find_el(self.verify_code_input).send_keys(data)

    def click_login_button(self):
        return self.find_el(self.login_btn).click()

    def get_error_msg(self):
        msg = self.find_el(self.msg).text
        return msg