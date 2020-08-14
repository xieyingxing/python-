"""
    需求: 响应由行头体三部分组成，需要使用 requests 相关实现解析响应中的行头体
"""
# 导包
import requests
# 发送请求接收响应
response = requests.get("http://www.baidu.com/")
# 处理响应
#-----------------------------------------------------------
print("-"*80)
# 行解析
print("URL:", response.url)
print("状态码:", response.status_code)
#-----------------------------------------------------------
print("-"*80)
# 头获取
print("获取所有响应头:", response.headers)
print("获取指定头,内容长度:", response.headers.get("Content-Length"))
print("获取所有cookie:", response.cookies)
print("获取响应的编码集:", response.encoding)
#-----------------------------------------------------------
print("-"*80)
# 体获取
print("以文本的方式获取响应体:", response.text)
print("以二进制方式获取响应体:", response.content)#适用于图片、视频、音频等非文本数据
# print("以JSON方式获取响应体:", response.json())#转换成 JSON，方便以 JSON语法解析数据