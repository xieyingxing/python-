from api.AreaAPIDB import AreaAPIDB

area_name = '张三'
area_name2 = '老六'

#打印数据
def area_print(response):
    return '响应状态码：',response.status_code,'响应数据:',response.text

#新增数据
def area_add_data():
    return {'areaName':area_name, 'priority':'1'}

#修改数据
def area_modify_data():
    id = AreaAPIDB.select_id_by_name(area_name)
    return {'areaId': id, 'areaName':area_name2, 'priority':'2'}

#删除数据
def area_remove_data():
    id = AreaAPIDB.select_id_by_name(area_name2)
    return {'areaId': id}


