import time

import pytest

from page.page_index import PageIndex
from page.page_login import PageLogin
from utils.driver_utils import DriverUtils


class TestLogin:

    # 浏览器驱动对象获取
    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.index = PageIndex(self.driver)
        self.login = PageLogin(self.driver)
        self.driver.get('http://192.168.2.133/')

    # 浏览器驱动对象关闭
    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.parametrize('params',[{'username':'13535101252', 'password':'123456', 'code':'8888', 'msg':'账号不存在!'},
                                       {'username':'13535101255', 'password':'1234567', 'code':'8888', 'msg':'密码错误!'}])
    def test_login(self, params):
        # 1. 点击首页的 ‘登录’ 链接，进入登录页面
        self.index.click_login_link()
        # 2. 输入一个不存在的用户名
        self.login.get_username(params['username'])
        # 3. 输入密码
        self.login.get_password(params['password'])
        # 4. 输入验证码
        self.login.get_code(params['code'])
        # 5. 点击登录按钮
        self.login.click_login_button()
        # 6. 获取错误提示信息
        time.sleep(3)
        msg = self.login.get_error_msg()
        print(msg)
        assert params['msg'] == msg
    #
    # def test_login_account_not_exist(self):
    #     # 1. 点击首页的 ‘登录’ 链接，进入登录页面
    #     self.login.click_login_link()
    #     # 2. 输入一个不存在的用户名
    #     self.login.get_username("13535101252")
    #     # 3. 输入密码
    #     self.login.get_password('123456')
    #     # 4. 输入验证码
    #     self.login.get_code('8888')
    #     # 5. 点击登录按钮
    #     self.login.click_login_button()
    #     # 6. 获取错误提示信息
    #     time.sleep(3)
    #     msg = self.login.get_error_msg()
    #     print(msg)
    #     assert '账号不存在!' == msg
    #
    # def test_login_password_error(self):
    #     # 1. 点击首页的 ‘登录’ 链接，进入登录页面
    #     self.login.click_login_link()
    #     # 2. 输入用户名
    #     self.login.get_username("13535101255")
    #     # 3. 输入错误密码
    #     self.login.get_password('1234567')
    #     # 4. 输入验证码
    #     self.login.get_code('8888')
    #     # 5. 点击登录按钮
    #     self.login.click_login_button()
    #     # 6. 获取错误提示信息
    #     time.sleep(3)
    #     msg = self.login.get_error_msg()
    #     print(msg)
    #     assert '密码错误!' == msg
