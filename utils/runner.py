import math

import numpy as np

import api
from utils.register import Register


class Runner(object):
    def __init__(self, register:Register=None, tolerance:float = 0.42):
        self.register = register
        self.tolerance = tolerance

    def clear(self):
        self.register.clear()

    def run_register(self, name, face_img):
        """Register a register's face encoding into data base

        Parameters:
            register: data base handler
            face_folder: image file folder
        Returns:

        """
        if not isinstance(face_img, np.ndarray):
            return '请打开摄像头'
        encoding = api.face_encodings(face_img)[0]
        ret, msg = self.register.insert_query(name, str(encoding.tolist()))
        if not ret:
            return f'Register {name} Error, Msg: {msg}'
        else:
            return '注册成功'

    def run_test(self, face_img):
        """
        face recognition
        :param register: data base handler
        :param face_folder: image file folder
        :return: recognize result
        """
        if not isinstance(face_img, np.ndarray):
            return ('请打开摄像头',)
        know_encodings = self.register.get_encodings()
        try:
            image_to_test_encoding = api.face_encodings(face_img)[0]
        except IndexError:
            return ('识别失败，为检测到人脸，请重试，请勿遮挡面部')
        res_name, res_distance = '识别失败，未找到与之匹配的人', math.inf
        for id, (name, encoding) in know_encodings.items():

            face_ret, distance = api.compare_faces(encoding, image_to_test_encoding, tolerance=self.tolerance)
            if face_ret:
                if distance < res_distance:
                    res_name = name
                    res_distance = distance
        self.register.update_query(name=res_name)
        return [res_name]

    def get_detail_with_pension(self):
        return self.register.get_detail_with_pension()
