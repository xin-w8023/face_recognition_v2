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
        try:
            encoding = api.face_encodings(face_img)[0]
        except IndexError:
            return
        all_names = [item[0] for item in self.register.get_detail_with_pension()]
        if name in all_names:
            return '已采集过'
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
            return
        res_name, res_distance = None, math.inf
        for id, (name, encoding) in know_encodings.items():

            face_ret, distance = api.compare_faces(encoding, image_to_test_encoding, tolerance=self.tolerance)
            if face_ret:
                if distance < res_distance:
                    res_name = name
                    res_distance = distance
        res = self.register.get_one_detail(name=res_name)
        self.register.update_query(name=res_name)
        return res

    def batch_register(self, folder, video=False):
        import os
        import glob

        if not video:
            container = []
            for suffix in ('*.jpg', '*.jpeg', '*.png'):
                container += glob.glob(os.path.join(folder, suffix))
            if not container:
                return f'未找到照片(jpg)'
            for img in container:
                _, basename = os.path.split(img)
                name = basename.split('.')[0]
                face_img = api.load_image_file(img)
                res = self.run_register(name, face_img)
                if res not in  ('注册成功', '已采集过'):
                    return f'{name} 注册失败，请检查照片'
            else:
                return '批量注册成功！'
        else:
            import cv2
            container = []
            for suffix in ('*.mp4', '*.avi', '*.mov'):
                container += glob.glob(os.path.join(folder, suffix))
            if not container:
                return f'未找到视频(mp4)'
            for video in container:
                _, basename = os.path.split(video)
                name = basename.split('.')[0]
                cap = cv2.VideoCapture(video)
                while True:
                    ret, img = cap.read()
                    if not ret:
                        return f'{name} 注册失败，请检查视频'
                    else:
                        img = cv2.resize(img, (640, 480))
                        res = self.run_register(name, img)
                        if res in  ('注册成功', '已采集过'):
                            break
                        else:
                            return f'{name} 注册失败，请检查视频'
                cap.release()
            else:
                return '批量注册成功！'

    def get_detail_with_pension(self):
        return self.register.get_detail_with_pension()
