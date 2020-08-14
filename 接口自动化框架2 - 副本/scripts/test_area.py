import requests

from api.AreaAPI import AreaAPI
from data.data import *


class TestArea:

    #初始化函数
    def setup(self):
        self.session = requests.Session()
        self.area_api = AreaAPI(self.session)

    #关闭函数
    def teardown(self):
        self.session.close()

    #测试查询list函数
    def test_list_area(self):
        response = self.area_api.list_area()
        print(area_print(response))


    # 测试新增add接口
    def test_add_area(self):
        response = self.area_api.add_area(area_add_data())
        print(area_print(response))


    #测试修改modify接口
    def test_modify_area(self):
        response = self.area_api.modify_area(area_modify_data())
        print(area_print(response))


    #测试删除remove接口
    def test_remove_area(self):
        response = self.area_api.remove_area(area_remove_data())
        print(area_print(response))

