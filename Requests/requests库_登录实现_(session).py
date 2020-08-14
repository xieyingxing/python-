import requests

# 创建 session 对象
session = requests.Session()

# 获取验证码
response1 = session.get('http://localhost/index.php?m=Home&c=User&a=verify')
print('响应状态码：',response1.status_code)
print(response1)
print('='*100)

# 登录
data={'username':'13535101255','password':'123456','verify_code':'8888'}
response2 = session.post('http://localhost/index.php?m=Home&c=User&a=do_login',data=data)
print('响应状态码：',response2.status_code)
# print('响应数据：',response2.text)
print(response2.text.encode('utf-8').decode('unicode_escape'))
print('='*100)

# 打开我的订单
# response3 = session.get('http://localhost/Home/Order/order_list.html')
# print('响应状态码：',response3.status_code)
# print('响应数据：',response3.text)