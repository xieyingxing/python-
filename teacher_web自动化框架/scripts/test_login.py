import time
import pytest
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_util import DriverUtil


class TestLogin:

    def setup(self):
        # 浏览器驱动对象获取
        self.driver = DriverUtil.get_driver()
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.driver.get("http://192.168.2.133/")

    def teardown(self):
        # 浏览器驱动对象关闭
        time.sleep(3)
        DriverUtil.close_driver()

    @pytest.mark.parametrize("params", [{"username": "16600000000", "password": "123456", "code": "8888", "msg": "账号不存在!"},
                                        {"username": "13412341234", "password": "abcdef", "code": "8888", "msg": "密码错误!"}])
    def test_login(self, params):
        self.index_page.click_login_link()
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.input_verify_code(params["code"])
        self.login_page.click_login_btn()
        time.sleep(2)
        assert params["msg"] == self.login_page.get_error_msg()

