from widgets.ui_mainwindow import Ui_mainWindow
from widgets.queuecalculator import QueueCalculator
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys
class MainWindow(QMainWindow):

    def __init__(self, venderInfo):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self, venderInfo)
        
        self.queueCalculator = QueueCalculator(venderInfo)

        self.ui.actionChangeTime.triggered.connect(self.changeTime)
        self.ui.actionQueueTimeCalculator.triggered.connect(self.openCalculator)
        self.ui.centralWidget.ui.verderInfoWidget.openCalculatorRequest.connect(self.queueCalculator.openWithVender)
        
        #cssFile = open('color.css', 'r')
        #cssText = cssFile.read()
        #self.setStyleSheet(cssText)


    def changeTime(self):
        centralWidget = self.ui.centralWidget
        centralWidget.timer.start(10000000)
        centralWidget.setUserDefinedTimeView()
        centralWidget.ui.dateTimeEdit.setFocus(True)
        centralWidget.ui.dateTimeEdit.selectAll()

    
    def openCalculator(self):
        self.queueCalculator.open