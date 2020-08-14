from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):

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

    def input_username(self, content):
        return self.input(self.username_input, content)

    def input_password(self, content):
        return self.input(self.password_input, content)

    def input_verify_code(self, content):
        return self.input(self.verify_code_input, content)

    def click_login_btn(self):
        return self.click(self.login_btn)

    def get_error_msg(self):
        return self.find_el(self.msg).text
