# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from .demo import Ui_MainWindow


class Ui_MainWindow2(Ui_MainWindow):

    def __init__(self, main_win, runner):
        super().__init__()
        self.cap = None
        self.setupUi(main_win)
        self.timer_camera = QtCore.QTimer()
        self.image = None
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

    # def _capture(self):
    #     if self.flag:
    #         res = self.runner.run_register(self.res.toPlainText(), self.image)
    #         self.res.setPlainText(res)
    #     else:
    #         self.res.setPlainText('请打开摄像头')

    def _recognize(self):
        res = self.runner.run_test(self.image)
        info = '识别失败!'
        if res:
            info = '识别成功!'
        res_str = self._get_res_string(res)
        self.res.setPlainText(res_str)
        QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def _get_res_string(self, extra_str):
        res_str = self._header
        for item in extra_str:
            res_str += [''.join([item[0], '\t', '是' if item[1] else '否'])]
        return '\n'.join(res_str)

    def _show_camera(self):
        self.flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.img_win.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def _get_detail_with_pension(self):
        res = self.runner.get_detail_with_pension()
        self.res.setPlainText(self._get_res_string(res))

    def _register_with_photos(self):
        info = self.runner.batch_register(folder=self.res.toPlainText(), video=False)
        QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def _register_with_videos(self):
        info = self.runner.batch_register(folder=self.res.toPlainText(), video=True)
        QtWidgets.QMessageBox().information(None, '提示', info, QtWidgets.QMessageBox.Yes)

    def init_slots(self):
        self.open_camera.clicked.connect(self._open_camera)
        self.timer_camera.timeout.connect(self._show_camera)
        # self.capture.clicked.connect(self._capture)
        self.recognize.clicked.connect(self._recognize)
        self.clear.clicked.connect(self.runner.clear)
        self.detail.clicked.connect(self._get_detail_with_pension)
        self.batch_photo.clicked.connect(self._register_with_photos)
        self.batch_video.clicked.connect(self._register_with_videos)
        self.test.clicked.connect(self.test_dialogue)

    def test_dialogue(self):
        qd = QtWidgets.QInputDialog()
        text, okPressed = qd.getText(None, 'test_title', 'test 提示')
        if okPressed and text:
            print(text)

    def __del__(self):
        self.cap.release()
