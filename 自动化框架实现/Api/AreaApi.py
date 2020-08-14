from app import Base_Url, Area_Url


class AreaApi:

    def __init__(self,session):
        self.session = session
        self.list_area_url = Base_Url + Area_Url + 'listarea'
        self.add_area_url = Base_Url + Area_Url + 'addarea'
        self.modify_area_url = Base_Url + Area_Url + 'modifyarea'
        self.remove_area_url = Base_Url + Area_Url + 'removearea'

    #1.查询 list area
    def list_area(self):
        response = self.session.get(self.list_area_url)
        return response

    #2.新增 add area
    def add_area(self, data):
        response = self.session.post(self.add_area_url, data=data)
        return response

    #3.修改 modify area
    def modify_area(self, json):
        response = self.session.put(self.modify_area_url, json=json)
        return response

    #4.删除 remove area
    def remove_area(self, params):
        response = self.session.delete(self.remove_area_url, params=params)
        return response