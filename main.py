# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
#
from PyQt5 import QtWidgets

from ui.test import Ui_MainWindow2
from utils.runner import Runner
from utils.register import Register

if __name__ == '__main__':
    register = Register()
    runner = Runner(register)
    app = QtWidgets.QApplication(sys.argv)
    main_win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2(main_win, runner)
    main_win.show()
    sys.exit(app.exec_())
