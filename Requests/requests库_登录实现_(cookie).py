import requests

# 获取验证码 获取cookie
#
response1 = requests.get('http://localhost/index.php?m=Home&c=User&a=verify')
print('状态码：',response1.status_code)
id = response1.cookies.get('PHPSESSID')
print(id)
print('='*100)

# 登录
data={'username':'13535101255','password':'123456','verify_code':'8888'}
cookie = {'PHPSESSID':id}
response2 = requests.post('http://localhost/index.php?m=Home&c=User&a=do_login',data=data,cookies=cookie)
print('响应状态码：',response2.status_code)
print('响应数据：',response2.text)
print('='*100)


# 打开我的订单
response3 = requests.get('http://localhost/Home/Order/order_list.html',cookies=cookie)
print('响应状态码：',response3.status_code)
print('响应数据：',response3.text)

