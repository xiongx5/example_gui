# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/trigger_chain_gui_main.ui'
#
# Created: Fri Feb 21 10:55:56 2020
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(967, 836)
        self.btn_exit = QtGui.QPushButton(MainWindow)
        self.btn_exit.setGeometry(QtCore.QRect(770, 710, 121, 51))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.btn_clear_log = QtGui.QPushButton(MainWindow)
        self.btn_clear_log.setGeometry(QtCore.QRect(770, 670, 121, 28))
        self.btn_clear_log.setObjectName(_fromUtf8("btn_clear_log"))
        self.textBrowser_log = QtGui.QTextBrowser(MainWindow)
        self.textBrowser_log.setGeometry(QtCore.QRect(550, 210, 341, 441))
        self.textBrowser_log.setObjectName(_fromUtf8("textBrowser_log"))
        self.btn_debug0 = QtGui.QPushButton(MainWindow)
        self.btn_debug0.setGeometry(QtCore.QRect(190, 660, 121, 28))
        self.btn_debug0.setObjectName(_fromUtf8("btn_debug0"))
        self.btn_debug1 = QtGui.QPushButton(MainWindow)
        self.btn_debug1.setGeometry(QtCore.QRect(190, 690, 121, 28))
        self.btn_debug1.setObjectName(_fromUtf8("btn_debug1"))
        self.btn_debug2 = QtGui.QPushButton(MainWindow)
        self.btn_debug2.setGeometry(QtCore.QRect(190, 720, 121, 28))
        self.btn_debug2.setObjectName(_fromUtf8("btn_debug2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NSW sTGC Trigger Chain Test Control ", None))
        self.btn_exit.setText(_translate("MainWindow", "Exit", None))
        self.btn_clear_log.setText(_translate("MainWindow", "Clear Log", None))
        self.btn_debug0.setText(_translate("MainWindow", "debug0", None))
        self.btn_debug1.setText(_translate("MainWindow", "debug1", None))
        self.btn_debug2.setText(_translate("MainWindow", "debug2", None))

