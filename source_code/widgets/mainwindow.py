from widgets.ui_mainwindow import Ui_mainWindow
from widgets.queuecalculator import QueueCalculator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from widgets.blinking_widget import blink

class MainWindow(QMainWindow):

    def __init__(self, vendorInfo):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self, vendorInfo)

        self.queueCalculator = QueueCalculator(self, vendorInfo)

        self.ui.actionChangeTime.triggered.connect(self.changeTime)
        self.ui.actionQueueTimeCalculator.triggered.connect(self.openCalculator)
        self.ui.centralWidget.ui.vendorInfoWidget.openCalculatorRequest.connect(self.queueCalculator.openWithVendor)


    def changeTime(self):
        centralWidget = self.ui.centralWidget
        centralWidget.timer.start(10000000)
        centralWidget.setUserDefinedTime()
        centralWidget.ui.dateTimeEdit.setFocus(True)
        centralWidget.ui.dateTimeEdit.selectAll()
        centralWidget.ui.timeLabel.setText("Edit the time =>")
        blink(centralWidget.ui.timeLabel)


    def openCalculator(self):
        vendorItem = self.ui.centralWidget.ui.vendorList.currentItem()
        if vendorItem and not vendorItem.isHidden():
            vendor = vendorItem.data(Qt.UserRole)
            self.queueCalculator.openWithVendor(vendor)
        else: self.queueCalculator.open()
