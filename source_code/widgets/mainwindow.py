from widgets.ui_mainwindow import Ui_mainWindow
from widgets.queuecalculator import QueueCalculator
from widgets.openingtimetablewidget import OpeningTimetableWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from widgets.blinking_widget import blink

class MainWindow(QMainWindow):

    def __init__(self, vendorInfo):
        super().__init__()
        # set up basic ui
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self, vendorInfo)
        # set up pop up windows
        self.queueCalculator = QueueCalculator(self, vendorInfo)
        self.openingTimeTable = OpeningTimetableWidget(self, vendorInfo)
        # connect actions in toolbar with functions
        self.ui.actionShowAllOpeningTime.triggered.connect(self.openingTimeTable.show)
        self.ui.actionChangeTime.triggered.connect(self.changeTime)
        self.ui.actionShowOtherVendor.triggered.connect(self.ui.centralWidget.ui.vendorTypeBox.showPopup)
        self.ui.actionQueueTimeCalculator.triggered.connect(self.openCalculator)
        # connect the button in vendorInfoPage to the calculator
        self.ui.centralWidget.ui.vendorInfoWidget.vendorInfoPage.ui.openCalculatorBtn.clicked.connect(self.openCalculator)


    def changeTime(self):
        # shorten the name
        centralWidget = self.ui.centralWidget

        centralWidget.setTimeToNow()
        # change the ui
        centralWidget.setUserDefinedTime()
        # add hint for user
        centralWidget.ui.dateTimeEdit.setFocus(True)
        centralWidget.ui.dateTimeEdit.selectAll()
        centralWidget.ui.timeLabel.setText("Edit the time =>")
        blink(centralWidget.ui.timeLabel)


    def openCalculator(self):
        # check whether the current is selected and shown
        # if yes, open the calculater with selected vendor as default vendor
        # or open the calculator without specificing vendor
        vendorItem = self.ui.centralWidget.ui.vendorList.currentItem()
        if vendorItem and not vendorItem.isHidden():
            vendor = vendorItem.data(Qt.UserRole)
            self.queueCalculator.openWithVendor(vendor)
        else: self.queueCalculator.show()
