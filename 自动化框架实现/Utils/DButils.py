import pymysql

from app import *


class Utils:

    # 建立连接（桥）
    @classmethod
    def get_qiao(self):
        return pymysql.Connect(host=IP, port=Port, database=Database, user=User, password=Password, charset=Charset)

    # 建立游标（驴）
    @classmethod
    def get_lv(self, qiao):
        return qiao.cursor()

    # 关闭资源
    @classmethod
    def lv_qiao_close(self, lv, qiao):
        if lv and qiao:
            lv.close()
            qiao.close()