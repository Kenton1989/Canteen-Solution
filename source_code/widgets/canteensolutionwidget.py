# Done by Wei Kaitao

from datetime import datetime

from PyQt5.QtCore import QTimer, QDateTime, Qt, QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from widgets.ui_canteenwidget import Ui_canteenSolutionWidget
from widgets.blinking_widget import make_label_can_blink

class CanteenSolutionWidget(QWidget):

    def __init__(self, parent, vendorsInfo):
        super().__init__(parent)

        # store database
        self.vendorsInfo = vendorsInfo
        # create basic ui
        self.ui = Ui_canteenSolutionWidget()
        self.ui.setupUi(self)
        # set up the widget managing time
        self.timer = QTimer(self)
        self.setUpTimeInfoWidget()
        # the item to be desplayed when there are
        # no vendors match the requirement of time
        self.ui.noAvailableItem = QListWidgetItem('No available stall')
        # the  item of vender list that will vary as the database varies
        self.ui.vendorListItems = []
        self.setUpVendorsList()


    def setUpTimeInfoWidget(self):
        # set the time informaiton stores in the time widget to now
        self.setTimeToNow()

        # set a timer and update the time after one second
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.setTimeToNowLoop)
        self.timer.start(1000)

        # At the beginning, the time is default value (current time),
        # so set the default time view.
        self.setDefaultTimeView()

        # Add blinking function to the label to hint the user
        # when he/she wants to customize time information.
        make_label_can_blink(self.ui.timeLabel)

        # update the infomation of the pages
        # whenever the stored time infomation changes
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.timeChangedHandler)

        self.ui.setDefaultTimeBtn.clicked.connect(self.setDefaultTime)


    def setUpVendorsList(self):
        # shorten the names for latter use
        vendorList = self.ui.vendorList

        # add the item showing no wanted store
        self.ui.noAvailableItem.setSizeHint(QSize(0, 70))
        vendorList.addItem(self.ui.noAvailableItem)

        # read the database and create a item for each vendor
        for vendor in self.vendorsInfo:
            item = QListWidgetItem(vendor.name, vendorList)
            item.setData(Qt.UserRole, vendor)
            item.setSizeHint(QSize(0, 50))
            vendorList.addItem(item)
            self.ui.vendorListItems.append(item)

        # update the information according to the time informaiton
        self.updateVendorList()

        # switch the info page of stalls when a item is clicked
        self.ui.vendorList.itemClicked.connect(self.showVendorInfo)

        # update the list when the requirement of stalls changes
        self.ui.vendorTypeBox.currentIndexChanged.connect(self.updateVendorList)


    def timeChangedHandler(self, qTimeStamp):
        if self.timer.isActive():
            # if the timer is activated when time is change, it means that
            # the time is changed by user's behaviour, not the timer's signal
            # Then stop the timer to maintain the user-defined time
            self.timer.stop()
            self.setUserDefinedTimeView()

        # whenever the time information changes,
        # vendor list and menu may change
        self.updateVendorList()
        self.ui.vendorInfoWidget.updateMenu(qTimeStamp)


    # A simple function to adjust the UI
    # when the time info is default
    def setUserDefinedTimeView(self):
        self.ui.timeLabel.setText('Time is set to: ')
        self.ui.setDefaultTimeBtn.show()


    # A simple function to adjust the UI
    # when the time is set by user
    def setDefaultTimeView(self):
        self.ui.timeLabel.setText('Current Time: ')
        self.ui.setDefaultTimeBtn.hide()

    # set the number representing the showing mode
    SHOW_OPENING = 0
    SHOW_CLOSED = 1
    SHOW_ALL = 2

    def updateVendorList(self):
        noDisplayedVendor = True # To judge whether the list to be present is empty
        # determine what stalls are to be shown
        showMode = self.ui.vendorTypeBox.currentIndex()
        # transform the QTime because the database only accepts python datetime
        timeStamp = self.ui.dateTimeEdit.dateTime().toPyDateTime()

        if showMode == CanteenSolutionWidget.SHOW_OPENING:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    item.setHidden(False)
                    # recover the hidden page of the stall
                    # if the item is selected before
                    if item.isSelected() and item.isHidden():
                        self.showVendorInfo(item)
                    noDisplayedVendor = False
                else:
                    item.setHidden(True)
                    # hide the infomation if the selected stall
                    # is removed from the list
                    if item.isSelected():
                        self.showVendorInfo(None)

        elif showMode == CanteenSolutionWidget.SHOW_CLOSED:
            for item in self.ui.vendorListItems:
                vendor = item.data(Qt.UserRole)
                if vendor.isOpening(timeStamp):
                    item.setHidden(True)
                    # hide the infomation if the selected stall
                    # is removed from the list
                    if item.isSelected():
                        self.showVendorInfo(None)
                else:
                    noDisplayedVendor = False
                    # recover the hidden page of the stall
                    # if the item is selected before
                    if item.isSelected() and item.isHidden():
                        self.showVendorInfo(item)
                    item.setHidden(False)

        else: # mode: showing all stalls
            # in case of the database is empty
            noDisplayedVendor = len(self.ui.vendorListItems) == 0
            for item in self.ui.vendorListItems:
                # recover the hidden page of the stall
                # if the item is selected before
                if item.isSelected() and item.isHidden():
                    self.showVendorInfo(item)
                item.setHidden(False)

        # display the special item to indicate
        # no stalls fulfills the requirement of time
        if noDisplayedVendor:
            self.ui.noAvailableItem.setHidden(False)
        else: self.ui.noAvailableItem.setHidden(True)


    def setTimeToNow(self):
        # set the stored time information to current time
        self.ui.dateTimeEdit.setDateTime(QDateTime(datetime.now()))


    def setTimeToNowLoop(self):
        # used by timer to update time every second
        self.setTimeToNow()
        self.timer.start(1000)


    def setDefaultTime(self):
        # set the time to default value (current time)
        self.setTimeToNow()
        # start timer to regularly update time
        self.timer.start(1000)
        # change the view to default shape
        self.setDefaultTimeView()


    def setUserDefinedTime(self, timeStamp = None):
        # set the time to user defined time and change the view
        if timeStamp:
            self.ui.dateTimeEdit.setDateTime(QDateTime(timeStamp))

        self.setUserDefinedTimeView()

    def showVendorInfo(self, vendorItem):
        # show the information of item by
        # passing the stored infomation to the vendorInfoWidget
        if vendorItem and vendorItem.data(Qt.UserRole):
            vendor = vendorItem.data(Qt.UserRole)
            qTimeStamp = self.ui.dateTimeEdit.dateTime()
            self.ui.vendorInfoWidget.showInfo(vendor, qTimeStamp)
        else:
            self.ui.vendorInfoWidget.showInfo(None)
