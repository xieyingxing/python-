from Api.AreaApiDB import AreaDBapi

id = AreaDBapi.select_id_by_name('张三')
id2 = AreaDBapi.select_id_by_name('李四')

Data = {'areaName': '张三', 'priority': '良好'}
Json = {'areaId': id, 'areaName': '李四', 'priority': '良好'}
Params = {'areaId': id2}
