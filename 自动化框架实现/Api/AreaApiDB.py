from Utils.DButils import Utils


class AreaDBapi:

    @classmethod
    def select_id_by_name(cls, area_name):
        qiao = Utils.get_qiao() #建桥
        lv = Utils.get_lv(qiao) #建游标
        sql = 'select area_id from t_area where area_name = "{}"'.format(area_name)
        lv.execute(sql)
        rows = lv.fetchall() #获取全部结果
        Utils.lv_qiao_close(qiao, lv)
        return rows[0][0]