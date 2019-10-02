from widgets.ui_canteenwidget import Ui_canteenSolutionWidget
from PyQt5.QtCore import QTimer, QDateTime, Qt, QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon
from datetime import datetime
class CanteenSolutionWidget(QWidget):
    
    def __init__(self, vendorsInfo):
        super().__init__()

        self.ui = Ui_canteenSolutionWidget()
        self.ui.setupUi(self)
        self.ui.vendorListItems = []
        self.ui.noAvailableItem = QListWidgetItem('No available vendor')
        self.vendorsInfo = vendorsInfo
        self.setUpTimeInfoWidget()
        self.setUpvendorsList()
        

    def setUpTimeInfoWidget(self):
        self.setTimeToNow()
        #set a timer and update the time every second
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.setTimeToNowLoop)
        self.timer.start(1000)
        #The timer will stop when user change the time
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.timeChangedHandler)
        #At the beginning, the time is default value, the "Set to Default" Button is isHidden
        self.ui.setDefaultTimeBtn.hide()
        self.ui.setDefaultTimeBtn.clicked.connect(self.setDefaultTimeChanging)


    def setUpvendorsList(self):
        vendorList = self.ui.vendorList
        vendorListItems = self.ui.vendorListItems

        self.ui.noAvailableItem.setSizeHint(QSize(0, 70))
        vendorList.addItem(self.ui.noAvailableItem)
        
        for vendor in self.vendorsInfo:
            item = QListWidgetItem(QIcon(vendor.icon), vendor.name, vendorList)
            item.setData(Qt.UserRole, vendor)
            item.setSizeHint(QSize(0, 50))
            vendorList.addItem(item)
            vendorListItems.append(item)

        self.updatevendorList()

        self.ui.vendorList.itemClicked.connect(self.showvendorInfo)
        self.ui.vendorTypeBox.currentIndexChanged.connect(self.updatevendorList)


    def setTimeToNow(self):
        self.ui.dateTimeEdit.setDateTime(QDateTime(datetime.now()))


    def setTimeToNowLoop(self):
        self.setTimeToNow()
        self.timer.start(1000)


    def timeChangedHandler(self, qTimeStamp):
        if self.timer.isActive():
            #The time is changed by user's behaviour, not the timer's signal
            #Then stop the timer to maintain the user-defined time
            self.timer.stop()
            self.setUserDefinedTimeView()
        self.updatevendorList()
        self.ui.verderInfoWidget.updateMenu(qTimeStamp)


    def setUserDefinedTimeView(self):
        self.ui.timeLabel.setText('Time is set to: ')
        self.ui.setDefaultTimeBtn.show()

    
    def setDefaultTimeChanging(self):
        self.setTimeToNow()
        self.ui.setDefaultTimeBtn.hide()
        self.ui.timeLabel.setText('Current Time: ')
        self.timer.start(1000)

    SHOW_OPENING_vendor = 0
    SHOW_CLOSED_vendor = 1
    SHOW_ALL_vendor = 2
    def updatevendorList(self):
        noDisplayedvendor = True
        showMode = self.ui.vendorTypeBox.currentIndex()
        timeStamp = self.ui.dateTimeEdit.dateTime().toPyDateTime()

        if showMode == CanteenSolutionWidget.SHOW_OPENING_vendor:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    noDisplayedvendor = False
                    if item.isSelected() and item.isHidden():
                        self.showvendorInfo(item)
                    item.setHidden(False)
                else:
                    item.setHidden(True)
                    if item.isSelected():
                        self.showvendorInfo(None)

        elif showMode == CanteenSolutionWidget.SHOW_CLOSED_vendor:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    item.setHidden(True)
                    if item.isSelected():
                        self.showvendorInfo(None)
                else:
                    noDisplayedvendor = False
                    if item.isSelected() and item.isHidden():
                        self.showvendorInfo(item)
                    item.setHidden(False)

        else:
            noDisplayedvendor = False
            for item in self.ui.vendorListItems:
                if item.isSelected() and item.isHidden():
                    self.showvendorInfo(item)
                item.setHidden(False)
        
        if noDisplayedvendor:
            self.ui.noAvailableItem.setHidden(False)
        else: self.ui.noAvailableItem.setHidden(True)
    

    def showvendorInfo(self, vendorItem):
        if vendorItem and vendorItem.data(Qt.UserRole):
            vendor = vendorItem.data(Qt.UserRole)
            qTimeStamp = self.ui.dateTimeEdit.dateTime()
            self.ui.verderInfoWidget.showInfo(vendor, qTimeStamp)
        else:
            self.ui.verderInfoWidget.showInfo(None)


