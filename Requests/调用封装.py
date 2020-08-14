from utils.封装 import Utils

qiao = Utils.get_qiao()
lv = Utils.get_lv(qiao)

sql = "select * from t_area"
lv.execute(sql)
qiao.commit()

print('响应行数：',lv.rowcount)

rows = lv.fetchall()
a = 0
for row in rows:
    a += 1
    print('第{}行数据:'.format(a),row)

Utils.lv_qiao_close(lv,qiao)