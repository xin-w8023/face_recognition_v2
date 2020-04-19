# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5 import QtCore, QtGui
from .demo import Ui_MainWindow


class Ui_MainWindow2(Ui_MainWindow):

    def __init__(self, main_win, runner):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.setupUi(main_win)
        self.timer_camera = QtCore.QTimer()
        self.image = None
        self.start_flag = False
        self.runner = runner
        self.flag = False
        self.init_slots()


    def _open_camera(self):
        if not self.start_flag:
            flag = self.cap.read()
            if not flag:
                raise ValueError("wrong")
            self.open_camera.setText('关闭摄像头')
            self.start_flag = not self.start_flag
            self.timer_camera.start(30)
        else:
            self.start_flag = not self.start_flag
            self.timer_camera.stop()
            self.open_camera.setText('开启摄像头')

    def _capture(self):
        if self.flag:
            res = self.runner.run_register(self.res.toPlainText(), self.image)
            self.res.setPlainText(res)
        else:
            self.res.setPlainText('请打开摄像头')

    def _recognize(self):
        res = self.runner.run_test(self.image)
        QtCore.QCoreApplication.processEvents()
        self.res.setPlainText(",".join(res))

    def _show_camera(self):
        self.flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.img_win.setPixmap(QtGui.QPixmap.fromImage(showImage))


    def _get_detail_with_pension(self):
        res = self.runner.get_detail_with_pension()
        res_str = [''.join(['姓名', '\t', '是否已领退休金'])]
        for item in res:
            res_str += [''.join([item[0], '\t', '是' if item[1] else '否'])]
        self.res.setPlainText('\n'.join(res_str))

    def init_slots(self):
        self.open_camera.clicked.connect(self._open_camera)
        self.timer_camera.timeout.connect(self._show_camera)
        self.capture.clicked.connect(self._capture)
        self.recognize.clicked.connect(self._recognize)
        self.clear.clicked.connect(self.runner.clear)
        self.detail.clicked.connect(self._get_detail_with_pension)

    def __del__(self):
        self.cap.release()
