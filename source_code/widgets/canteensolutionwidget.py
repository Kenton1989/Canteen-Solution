from datetime import datetime

from PyQt5.QtCore import QTimer, QDateTime, Qt, QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtGui import QIcon

from widgets.ui_canteenwidget import Ui_canteenSolutionWidget
class CanteenSolutionWidget(QWidget):

    def __init__(self, vendorsInfo):
        super().__init__()

        self.ui = Ui_canteenSolutionWidget()
        self.ui.setupUi(self)
        self.ui.vendorListItems = []
        self.ui.noAvailableItem = QListWidgetItem('No available vendor')
        self.vendorsInfo = vendorsInfo
        self.__setUpTimeInfoWidget()
        self.__setUpVendorsList()


    def __setUpTimeInfoWidget(self):
        self.setTimeToNow()
        # set a timer and update the time after one second
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.setTimeToNowLoop)
        self.timer.start(1000)
        # At the beginning, the time is default value, so set the default time view.
        self.__setDefaultTimeView()

        self.ui.dateTimeEdit.dateTimeChanged.connect(self.__timeChangedHandler)
        self.ui.setDefaultTimeBtn.clicked.connect(self.setDefaultTime)


    def __setUpVendorsList(self):
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

        self.__updateVendorList()

        self.ui.vendorList.itemClicked.connect(self.showVendorInfo)
        self.ui.vendorTypeBox.currentIndexChanged.connect(self.__updateVendorList)


    def __timeChangedHandler(self, qTimeStamp):
        if self.timer.isActive():
            #if the timer is activated when time is change, it means that
            #the time is changed by user's behaviour, not the timer's signal
            #Then stop the timer to maintain the user-defined time
            self.timer.stop()
            self.__setUserDefinedTimeView()

        self.__updateVendorList()
        self.ui.vendorInfoWidget.updateMenu(qTimeStamp)


    def __setUserDefinedTimeView(self):
        self.ui.timeLabel.setText('Time is set to: ')
        self.ui.setDefaultTimeBtn.show()


    def __setDefaultTimeView(self):
        self.ui.timeLabel.setText('Current Time: ')
        self.ui.setDefaultTimeBtn.hide()


    SHOW_OPENING = 0
    SHOW_CLOSED = 1
    SHOW_ALL = 2
    def __updateVendorList(self):
        noDisplayedVendor = True
        showMode = self.ui.vendorTypeBox.currentIndex()
        timeStamp = self.ui.dateTimeEdit.dateTime().toPyDateTime()

        if showMode == CanteenSolutionWidget.SHOW_OPENING:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    noDisplayedVendor = False
                    if item.isSelected() and item.isHidden():
                        self.showVendorInfo(item)
                    item.setHidden(False)
                else:
                    item.setHidden(True)
                    if item.isSelected():
                        self.showVendorInfo(None)

        elif showMode == CanteenSolutionWidget.SHOW_CLOSED:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    item.setHidden(True)
                    if item.isSelected():
                        self.showVendorInfo(None)
                else:
                    noDisplayedVendor = False
                    if item.isSelected() and item.isHidden():
                        self.showVendorInfo(item)
                    item.setHidden(False)

        else:
            noDisplayedVendor = False
            for item in self.ui.vendorListItems:
                if item.isSelected() and item.isHidden():
                    self.showVendorInfo(item)
                item.setHidden(False)
        
        if noDisplayedVendor:
            self.ui.noAvailableItem.setHidden(False)
        else: self.ui.noAvailableItem.setHidden(True)
    

    def setTimeToNow(self):
        self.ui.dateTimeEdit.setDateTime(QDateTime(datetime.now()))


    def setTimeToNowLoop(self):
        self.setTimeToNow()
        self.timer.start(1000)


    def setDefaultTime(self):
        self.setTimeToNow()
        self.timer.start(1000)
        self.__setDefaultTimeView()


    def setUserDefinedTime(self, timeStamp = None):
        if timeStamp:
            self.ui.dateTimeEdit.setDateTime(QDateTime(timeStamp))

        self.__setUserDefinedTimeView()

    def showVendorInfo(self, vendorItem):
        if vendorItem and vendorItem.data(Qt.UserRole):
            vendor = vendorItem.data(Qt.UserRole)
            qTimeStamp = self.ui.dateTimeEdit.dateTime()
            self.ui.vendorInfoWidget.showInfo(vendor, qTimeStamp)
        else:
            self.ui.vendorInfoWidget.showInfo(None)
