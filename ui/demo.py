# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
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
        self.capture = QtWidgets.QPushButton(self.centralwidget)
        self.capture.setGeometry(QtCore.QRect(270, 580, 112, 32))
        self.capture.setObjectName("capture")
        self.open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.open_camera.setGeometry(QtCore.QRect(28, 580, 112, 32))
        self.open_camera.setObjectName("open_camera")
        self.img_win = QtWidgets.QLabel(self.centralwidget)
        self.img_win.setGeometry(QtCore.QRect(20, 50, 640, 480))
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
        self.recognize.setGeometry(QtCore.QRect(390, 580, 112, 32))
        self.recognize.setObjectName("recognize")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(148, 580, 112, 32))
        self.clear.setObjectName("clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.detail = QtWidgets.QPushButton(self.centralwidget)
        self.detail.setGeometry(QtCore.QRect(510, 580, 112, 32))
        self.detail.setObjectName("detail")
        self.res = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(673, 50, 241, 481))
        self.res.setObjectName("res")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "毕业设计"))
        self.capture.setText(_translate("MainWindow", "采集"))
        self.open_camera.setText(_translate("MainWindow", "打开摄像头"))
        self.recognize.setText(_translate("MainWindow", "识别"))
        self.clear.setText(_translate("MainWindow", "清空数据库"))
        self.label.setText(_translate("MainWindow", "人脸识别"))
        self.detail.setText(_translate("MainWindow", "详细信息"))
        self.res.setPlainText(_translate("MainWindow", "info"))

