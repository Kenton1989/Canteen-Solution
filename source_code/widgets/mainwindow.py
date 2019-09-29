from widgets.ui_mainwindow import Ui_mainWindow
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        #cssFile = open('color.css', 'r')
        #cssText = cssFile.read()
        self.setStyleSheet('.VenderInfoWidget { border: 1px solid black }')


