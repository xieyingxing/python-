from app.app import BASE_URL


class AreaAPI:

    def __init__(self, session):
        self.session = session
        self.list_area_url = BASE_URL + 'listarea'
        self.add_area_url = BASE_URL + 'addarea'
        self.modify_area_url = BASE_URL + 'modifyarea'
        self.remove_area_url = BASE_URL + 'removearea'

    #查询list的接口请求
    def list_area(self):
        return self.session.get(self.list_area_url)
        
    #新增add的接口请求
    def add_area(self, data):
        return self.session.post(self.add_area_url, data=data)
    
    #修改modify的接口请求
    def modify_area(self, json):
        return self.session.put(self.modify_area_url, json=json)
    
    #删除remove的接口请求
    def remove_area(self, params):
        return self.session.delete(self.remove_area_url, params=params)
