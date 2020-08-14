import pymysql

from app.app import *


class DButils:

    #建立数据库连接
    @classmethod
    def get_qiao(cls):
        return pymysql.Connect(host=HOST, port= PORT, database=DATABASE, user=USER, password=PASSWORD, charset=CHARSET)

    #建立游标
    @classmethod
    def get_lv(cls,qiao):
        return qiao.cursor()

    #关闭游标，断开连接
    @classmethod
    def close_qiao_lv(cls, lv, qiao):
        if lv and qiao:
            lv.close()
            qiao.close()

