import json

# 读取文件
with open('data.json', 'r', encoding='utf-8') as f:
    dict = json.load(f)
    print(dict)
    print(type(dict))

# 写文件
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, ensure_ascii=False)











# 定义一个字典对象
# dict_str = {'name':'张三', 'age':'18', 'school':None}
# 字典翻译为JSON
# json_str = json.dumps(dict_str)
# print(json_str)
# print(type(json_str))
#
# # 定义一个JSON字符串
# json_str1 = '{"name": "zhangsan", "age": 18, "is_man": false, "school": null}'
# # JSON字符串翻译为字典
# dict_str1 = json.loads(json_str1)
# print(dict_str1)
# print(type(dict_str1))


