from widgets.ui_mainwindow import Ui_mainWindow
from widgets.queuecalculator import QueueCalculator
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys


class MainWindow(QMainWindow):

    def __init__(self, vendorInfo):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self, vendorInfo)
        
        self.queueCalculator = QueueCalculator(vendorInfo)

        self.ui.actionChangeTime.triggered.connect(self.changeTime)
        self.ui.actionQueueTimeCalculator.triggered.connect(self.openCalculator)
        self.ui.centralWidget.ui.verderInfoWidget.openCalculatorRequest.connect(self.queueCalculator.openWithvendor)
        
        # cssFile = open('color.css', 'r')
        # cssText = cssFile.read()
        # self.setStyleSheet(cssText)


    def changeTime(self):
        centralWidget = self.ui.centralWidget
        centralWidget.timer.start(10000000)
        centralWidget.setUserDefinedTimeView()
        centralWidget.ui.dateTimeEdit.setFocus(True)
        centralWidget.ui.dateTimeEdit.selectAll()

    
    def openCalculator(self):
        vendorList = self.ui.centralWidget.ui.verderList
        self.queueCalculator.open()
