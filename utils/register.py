import sqlite3
from typing import Dict, Tuple

import numpy as np


class Register(object):
    """操作数据库的类"""

    def __init__(self, db_name='faces_lib.db', table_name='FACE_LIBRARY'):
        """初始化函数

        :param db_name: 数据库名
        :param table_name: 表名
        """
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()
        self.__create_face_lib()

    def __create_face_lib(self):
        """创建表：如果不存在，则创建；否则，无动作
        :return:
        """

        sql = f'CREATE TABLE IF NOT EXISTS {self.table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT , ' \
              f'NAME TEXT NOT NULL, PENSION INTEGER DEFAULT 0, ENCODING TEXT NOT NULL)'

        self.cursor.execute(sql)
        self.connect.commit()

    def update_query(self, name):
        """根据name，更新表，将name的是否领取退休金设置为1"""

        sql = f'UPDATE {self.table_name} SET PENSION=1 WHERE NAME=="{name}"'
        self.cursor.execute(sql)
        self.connect.commit()

    def insert_query(self, name: str, encoding: str, pension=0):
        """插入数据，字段名: name, encoding, pension"""

        sql = f'INSERT INTO {self.table_name} (NAME, PENSION, ENCODING) VALUES ("{name}", "{pension}", "{encoding}")'
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            return False, e
        return True, ""

    def get_detail_with_pension(self):
        """获取表中所有的姓名和是否领取退休金信息"""

        sql = f'select name, pension from {self.table_name}'
        ret = self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def get_one_detail(self, name):
        """获取指定人名的退休金信息"""

        sql = f'select name, pension from {self.table_name} where name=="{name}"'
        ret = self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def get_encoding_by_name(self, name) -> np.ndarray:
        """获取指定人名的人脸特征"""

        sql = f'select id, name, encoding from {self.table_name} where NAME=="{name}"'
        ret = self.cursor.execute(sql)
        # return [item for item in ret]
        return self.__convert_one_to_ndarray(next(ret))[2]

    def get_encodings(self):
        """获取所有人脸特征"""

        sql = f'select id, name, encoding from {self.table_name}'
        rets = self.cursor.execute(sql)
        return self.__convert_many_to_ndarray(rets)

    def __convert_one_to_ndarray(self, ret: Tuple[int, str, str]) -> Tuple[int, str, np.ndarray]:
        """将一个人脸特征转换为ndarray类型"""

        return ret[0], ret[1], np.array([float(e) for e in ret[2].strip('[]').split(', ')], dtype=np.float).reshape((1, -1))

    def __convert_many_to_ndarray(self, rets) -> Dict[int, Tuple[str, np.ndarray]]:
        """将多个人脸特征转换为ndarray类型"""

        res = {}
        for ret in rets:
            one_encoding = self.__convert_one_to_ndarray(ret)
            res[one_encoding[0]] = (one_encoding[1], one_encoding[2])
        return res

    def get_all_encodings(self):
        """获取所有人脸特征"""

        sql = f'select name, encoding from {self.table_name}'
        ret = self.cursor.execute(sql)
        return [item for item in ret]

    def clear(self):
        """删除所有数据"""

        sql = f'DELETE FROM {self.table_name} WHERE ID > 0'
        self.cursor.execute(sql)
        self.connect.commit()
        self.update_id()

    def update_id(self):
        """清除数据库之后，更新主键"""

        sql = f'UPDATE sqlite_sequence SET seq=0 WHERE name="{self.table_name}"'
        self.cursor.execute(sql)
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()
