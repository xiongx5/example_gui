#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
# from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

from time import sleep
import time
from trigger_chain_gui import Ui_MainWindow
import sys, os

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setStyleSheet("background-color: Lightpink;")
        # self.setStyleSheet("background-color: Lightskyblue;")
        # self.setStyleSheet("background-color: Lightgreen;")

        self.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        # self.setStyle(QtGui.QStyleFactory.create('motif'))
        # self.setStyle(QtGui.QStyleFactory.create('Windows'))
        # self.setStyle(QtGui.QStyleFactory.create('cde'))
        # self.setStyle(QtGui.QStyleFactory.create('Plastique'))
        # self.setStyle(QtGui.QStyleFactory.create('windowsvista'))
        self.qtimer=QtCore.QTimer()
        self.home()


    def home(self):
        QtCore.QObject.connect(self.qtimer, QtCore.SIGNAL("timeout()"), self.update_result)
        QtCore.QObject.connect(self.ui.btn_debug0,QtCore.SIGNAL("clicked()"),self.debug0)
        QtCore.QObject.connect(self.ui.btn_exit,QtCore.SIGNAL("clicked()"),QtCore.QCoreApplication.instance().quit)
        QtCore.QObject.connect(self.ui.btn_clear_log,QtCore.SIGNAL("clicked()"),self.clear_log)

        self.qtimer.start(100) #ms

    def debug0(self):
        self.log('jhhh')

    def update_result(self):
        pass

    def log(self,text):
        self.ui.textBrowser_log.append(text)

    def clear_log(self):
        self.ui.textBrowser_log.clear()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

