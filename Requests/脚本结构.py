#1.导包
import pymysql

# 2.建桥
qiao = pymysql.Connect(host='localhost', port=3306, database='test', user='root', password='123456', charset='utf8')

# 3.xx驴（建立游标）
lv = qiao.cursor()

# 4.执行sql语句
#查询
sql = 'select * from t_area'

# 增加
# sql = 'insert into t_area(area_name,priority) value ("张三","123")'

# 修改
# sql = 'update t_area set area_name = "李四" where area_id ="150"'

# 删除
# sql = 'delete from t_area where area_id = "151"'

lv.execute(sql)
qiao.commit()

# 获取执行结果
print('响应行数:', lv.rowcount)

# 逐行获取结果
# rows1 = lv.fetchone()
# print('第一行数据：',rows1)

# 获取全部数据
rows = lv.fetchall()
a = 0
for row in rows:
    a += 1
    print('第{}行数据:'.format(a),row)


# 5.杀驴
lv.close()

# 6.拆桥
qiao.close()