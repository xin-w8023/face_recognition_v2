import sqlite3
from typing import Dict, Tuple

import numpy as np


class Register(object):
    def __init__(self, db_name='faces_lib.db', table_name='FACE_LIBRARY'):
        self.db_name = db_name
        self.table_name = table_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()
        self.__create_face_lib()

    def __create_face_lib(self):
        sql = f'CREATE TABLE IF NOT EXISTS {self.table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT , ' \
              f'NAME TEXT NOT NULL, PENSION INTEGER DEFAULT 0, ENCODING TEXT NOT NULL)'

        self.cursor.execute(sql)
        self.connect.commit()

    def update_query(self, name):
        sql = f'UPDATE {self.table_name} SET PENSION=1 WHERE NAME=="{name}"'
        self.cursor.execute(sql)
        self.connect.commit()



    def insert_query(self, name:str, encoding:str, pension=0):
        sql = f'INSERT INTO {self.table_name} (NAME, PENSION, ENCODING) VALUES ("{name}", "{pension}", "{encoding}")'
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            return False, e
        return True, ""

    def get_detail_with_pension(self):
        sql = f'select name, pension from {self.table_name}'
        ret = self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def get_one_detail(self, name):
        sql = f'select name, pension from {self.table_name} where name=="{name}"'
        ret = self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def get_encoding_by_name(self, name) -> np.ndarray:
        sql = f'select id, name, encoding from {self.table_name} where NAME=="{name}"'
        ret = self.cursor.execute(sql)
        # return [item for item in ret]
        return self.__convert_one_to_ndarray(next(ret))[2]

    def get_encodings(self):
        sql = f'select id, name, encoding from {self.table_name}'
        rets = self.cursor.execute(sql)
        return self.__convert_many_to_ndarray(rets)

    def __convert_one_to_ndarray(self, ret:Tuple[int, str, str]) -> Tuple[int, str, np.ndarray]:
        return ret[0], ret[1], np.array([float(e) for e in ret[2].strip('[]').split(', ')], dtype=np.float).reshape((1, -1))

    def __convert_many_to_ndarray(self, rets) -> Dict[int, Tuple[str, np.ndarray]]:
        res = {}
        for ret in rets:
            one_encoding = self.__convert_one_to_ndarray(ret)
            res[one_encoding[0]] = (one_encoding[1], one_encoding[2])
        return res

    def get_all_encodings(self):
        sql = f'select name, encoding from {self.table_name}'
        ret = self.cursor.execute(sql)
        return [item for item in ret]

    def clear(self):
        """clear all recodes"""
        sql = f'DELETE FROM {self.table_name} WHERE ID > 0'
        self.cursor.execute(sql)
        self.connect.commit()
        self.update_id()

    def update_id(self):
        sql = f'UPDATE sqlite_sequence SET seq=0 WHERE name="{self.table_name}"'
        self.cursor.execute(sql)
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()
