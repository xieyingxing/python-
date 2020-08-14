import requests

from Api.AreaApi import AreaApi
from Api.AreaApiDB import AreaDBapi


class TestArea:

    #初始化函数
    def setup(self):
        self.session = requests.Session()
        self.area_api = AreaApi(self.session)

    #销毁资源函数
    def tesrdown(self):
        self.session.close()

    #测试查询list列表接口
    def test_list_area(self):
        response = self.area_api.list_area()
        print('响应状态码:',response.status_code)
        print('响应数据：',response.text)

    #测试新增add接口
    def test_add_area(self):
        data = {'areaName': '张三', 'priority': '良好'}
        response = self.area_api.add_area(data=data)
        print('响应状态码:',response.status_code)
        print('响应数据：',response.text)

    #测试修改modify接口
    def test_modify_area(self):
        id = AreaDBapi.select_id_by_name('张三')
        json = {'areaId': id, 'areaName': '李四', 'priority': '良好'}
        response = self.area_api.modify_area(json=json)
        print('响应状态码:',response.status_code)
        print('响应数据：',response.text)

    #测试删除remove接口
    def test_remove_area(self):
        id = AreaDBapi.select_id_by_name('李四')
        params = {'areaId': id}
        response = self.area_api.remove_area(params=params)
        print('响应状态码:',response.status_code)
        print('响应数据：',response.text)
