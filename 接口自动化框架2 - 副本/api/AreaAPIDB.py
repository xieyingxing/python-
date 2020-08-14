from utils.DButils import DButils


class AreaAPIDB:

    @classmethod
    def select_id_by_name(cls, area_name):
        #建立连接
        qiao = DButils.get_qiao()

        #建立游标
        lv = DButils.get_lv(qiao)

        #编写需要执行的sql语句
        sql = "select area_id from t_area where area_name = '{}'".format(area_name)

        #执行sql语句
        lv.execute(sql)

        #获取全部结果
        rows = lv.fetchall()

        #关闭游标，连接
        DButils.close_qiao_lv(lv, qiao)

        #返回获取名字对应的ID
        return rows[0][0]