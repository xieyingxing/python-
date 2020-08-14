import pytest   #数据参数化


class TestDome:

    @pytest.mark.parametrize('data',[{'name':'张三','password':'123'},{'name':'李四','password':'456'}])
    def test_1(self,data):
        print(data['name']+'----'+data['password'])
