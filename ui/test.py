# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import time

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from .demo import Ui_MainWindow
import numpy as np

class Ui_MainWindow2(Ui_MainWindow):

    def __init__(self, main_win, runner):
        super().__init__()
        self.cap = None
        self.setupUi(main_win)
        self.timer_camera = QtCore.QTimer()
        self.start_flag = False
        self.runner = runner
        self.flag = False
        self.init_slots()

        self._header = [''.join(['姓名', '\t', '是否已领退休金'])]
        self.res.setPlainText(self._get_res_string([]))

    def _open_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
        if not self.start_flag:
            self.open_camera.setText('关闭摄像头')
            self.start_flag = not self.start_flag
            self.timer_camera.start(30)
        else:
            self.start_flag = not self.start_flag
            self.cap.release()
            self.cap = None
            self.timer_camera.stop()
            self.open_camera.setText('开启摄像头')
            show = np.ones((480, 640, 3), dtype=np.uint8)*255
            show = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                     QtGui.QImage.Format_Mono)
            self.img_win.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def _close_camera(self):
        if self.cap:
            self.timer_camera.stop()
            self.cap.release()
            self.cap = None

    def _recognize(self):
        if self.cap is None:
            QtWidgets.QMessageBox().warning(None, '警告', '请打开摄像头', QtWidgets.QMessageBox.Yes)
            return
        flag, image = self.cap.read()
        if not flag:
            QtWidgets.QMessageBox().warning(None, '警告','摄像头读取失败', QtWidgets.QMessageBox.Yes)
            return
        res = self.runner.run_test(image)
        print(res)
        info = '识别失败!'
        if res:
            info = res[0][0] + '识别成功!'
        res_str = self._get_res_string(res)
        self.res.setPlainText(res_str)
        QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def _get_res_string(self, extra_str):
        res_str = self._header.copy()
        for item in extra_str:
            res_str += [''.join([item[0], '\t', '是' if item[1] else '否'])]
        return '\n'.join(res_str)

    def _show_camera(self):
        flag, image = self.cap.read()
        show = cv2.resize(image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.img_win.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def _get_detail_with_pension(self):
        res = self.runner.get_detail_with_pension()
        self.res.setPlainText(self._get_res_string(res))

    def _register_with_photos(self):
        text, okPressed = QtWidgets.QInputDialog().getText(None, '照片采集', '文件夹地址')
        if okPressed:
            if text:
                info = self.runner.batch_register(folder=text, video=False)
                QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)
            else:
                info = '请输入文件夹'
                QtWidgets.QMessageBox().warning(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def _register_with_videos(self):
        text, okPressed = QtWidgets.QInputDialog().getText(None, '视频采集', '文件夹地址')
        print(text, okPressed)
        if okPressed:
            if text:
                info = self.runner.batch_register(folder=text, video=True)
                QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)
            else:
                info = '请输入文件夹'
                QtWidgets.QMessageBox().warning(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def init_slots(self):
        self.open_camera.clicked.connect(self._open_camera)
        self.timer_camera.timeout.connect(self._show_camera)
        self.recognize.clicked.connect(self._recognize)
        self.clear.clicked.connect(self.runner.clear)
        self.detail.clicked.connect(self._get_detail_with_pension)
        self.batch_photo.clicked.connect(self._register_with_photos)
        self.batch_video.clicked.connect(self._register_with_videos)

