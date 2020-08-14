import pymysql


qiao = pymysql.Connect(host='localhost', port=3306, database='test', user='root', password='123456', charset='utf8')

lv = qiao.cursor()

try:
    sql1 = "insert into t_area(area_name,priority) value ('王五','123')"
    sql2 = "insert into t_area(area_name,priority) value ('赵大','123')"
    sql3 = "select * from t_area"
    lv.execute(sql1)
    lv.execute(sql2)
    lv.execute(sql3)
    qiao.commit()  #提交
except Exception as a:
    print(a)
    qiao.rollback() #回滚
finally:
    print('响应行数:', lv.rowcount)

    rows = lv.fetchall()
    a = 0
    for row in rows:
        a += 1
        print('第{}行数据:'.format(a), row)

    lv.close()
    qiao.close()


