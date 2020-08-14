import requests


class TestDemo:

    #初始化函数
    def setup(self):
        self.session = requests.Session()


    #销毁函数资源
    def teardown(self):
        self.session.close()

    #获取验证码
    def test_yzm(self):
        response = self.session.get('http://localhost/index.php?m=Home&c=User&a=verify')
        print('响应状态码：', response.status_code)
        print(response)
        assert 200 == response.status_code

    # 登录
    def test_login(self):
        data = {'username': '13535101255', 'password': '123456', 'verify_code': '8888'}
        response1 = self.session.post('http://localhost/index.php?m=Home&c=User&a=do_login', data=data)
        assert 200 == response1.json().get('status')