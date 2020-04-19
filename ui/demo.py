# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(940, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(940, 700))
        MainWindow.setMaximumSize(QtCore.QSize(940, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.open_camera.setGeometry(QtCore.QRect(360, 580, 112, 32))
        self.open_camera.setObjectName("open_camera")
        self.img_win = QtWidgets.QLabel(self.centralwidget)
        self.img_win.setGeometry(QtCore.QRect(20, 80, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_win.sizePolicy().hasHeightForWidth())
        self.img_win.setSizePolicy(sizePolicy)
        self.img_win.setMinimumSize(QtCore.QSize(640, 480))
        self.img_win.setMaximumSize(QtCore.QSize(640, 480))
        self.img_win.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.img_win.setAutoFillBackground(False)
        self.img_win.setStyleSheet("border-color: rgba(29, 29, 29, 100);\n"
"background-color: rgb(212, 212, 212);")
        self.img_win.setText("")
        self.img_win.setObjectName("img_win")
        self.recognize = QtWidgets.QPushButton(self.centralwidget)
        self.recognize.setGeometry(QtCore.QRect(360, 620, 112, 32))
        self.recognize.setObjectName("recognize")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(480, 620, 112, 32))
        self.clear.setObjectName("clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.detail = QtWidgets.QPushButton(self.centralwidget)
        self.detail.setGeometry(QtCore.QRect(480, 580, 112, 32))
        self.detail.setObjectName("detail")
        self.res = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(673, 80, 241, 481))
        self.res.setPlainText("")
        self.res.setObjectName("res")
        self.batch_photo = QtWidgets.QPushButton(self.centralwidget)
        self.batch_photo.setGeometry(QtCore.QRect(250, 580, 112, 32))
        self.batch_photo.setObjectName("batch_photo")
        self.batch_video = QtWidgets.QPushButton(self.centralwidget)
        self.batch_video.setGeometry(QtCore.QRect(250, 620, 112, 32))
        self.batch_video.setObjectName("batch_video")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncamera = QtWidgets.QAction(MainWindow)
        self.actioncamera.setCheckable(True)
        self.actioncamera.setObjectName("actioncamera")
        self.actionfile = QtWidgets.QAction(MainWindow)
        self.actionfile.setCheckable(True)
        self.actionfile.setObjectName("actionfile")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "毕业设计"))
        self.open_camera.setText(_translate("MainWindow", "打开摄像头"))
        self.recognize.setText(_translate("MainWindow", "识别"))
        self.clear.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "人脸识别"))
        self.detail.setText(_translate("MainWindow", "刷新"))
        self.batch_photo.setText(_translate("MainWindow", "照片批量采集"))
        self.batch_video.setText(_translate("MainWindow", "视频批量采集"))
        self.actioncamera.setText(_translate("MainWindow", "camera"))
        self.actionfile.setText(_translate("MainWindow", "file"))

