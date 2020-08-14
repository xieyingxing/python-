import requests
#查询全部
respone1 = requests.get('http://localhost:8081/sa/listarea')
print('响应状态码：',respone1.status_code)
print('响应数据：',respone1.text)

#根据areaId查询单个
id = {'areaId':'5'}
respone2 = requests.get('http://localhost:8081/sa/getareabyid',params=id)
print('响应状态码：',respone2.status_code)
print('响应数据：',respone2.text)

#新增
data = {'areaName':'李四','priority':'123'}
respone3 = requests.post('http://localhost:8081/sa/addarea',data=data)
print('响应状态码：',respone3.status_code)
print('响应数据：',respone3.text)

# 修改
json={"areaId":'8',"areaName": "张三","priority": "123"}
respone4 = requests.put('http://localhost:8081/sa/modifyarea',json=json)
print('响应状态码：',respone4.status_code)
print('响应数据：',respone4.text)

# 删除
params={'areaId':'6'}
respone5 = requests.delete('http://localhost:8081/sa/removearea',params=params)
print('响应状态码：',respone5.status_code)
print('响应数据：',respone5.text)

#查询全部
respone6 = requests.get('http://localhost:8081/sa/listarea')
print('响应状态码：',respone6.status_code)
print('最终响应数据：',respone6.text)
