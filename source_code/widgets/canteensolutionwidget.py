from widgets.ui_canteenwidget import Ui_canteenSolutionWidget
from PyQt5.QtCore import QTimer, QDateTime, Qt, QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon
from datetime import datetime
class CanteenSolutionWidget(QWidget):
    
    def __init__(self, vendersInfo):
        super().__init__()

        self.ui = Ui_canteenSolutionWidget()
        self.ui.setupUi(self)
        self.ui.venderListItems = []
        self.noAvailableItem = QListWidgetItem('No available vender')
        self.vendersInfo = vendersInfo
        self.setUpTimeInfoWidget()
        self.setUpVendersList()
        

    def setUpTimeInfoWidget(self):
        self.setTimeToNow()
        #set a timer and update the time every second
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.setTimeToNowLoop)
        self.timer.start(1000)
        #The timer will stop when user change the time
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.timeChangedHandler)
        #At the beginning, the time is default value, the "Set to Default" Button is hidden
        self.ui.setDefaultTimeBtn.hide()
        self.ui.setDefaultTimeBtn.clicked.connect(self.setDefaultTimeChanging)


    def setUpVendersList(self):
        venderList = self.ui.venderList
        venderListItems = self.ui.venderListItems

        self.noAvailableItem.setSizeHint(QSize(0, 50))
        venderList.addItem(self.noAvailableItem)
        
        for vender in self.vendersInfo:
            item = QListWidgetItem(QIcon(vender.icon), vender.name, venderList)
            item.setData(Qt.UserRole, vender)
            item.setSizeHint(QSize(0, 50))
            venderList.addItem(item)
            venderListItems.append(item)

        self.updateVenderList()

        self.ui.venderList.itemClicked.connect(self.showVenderInfo)
        self.ui.venderTypeBox.currentIndexChanged.connect(self.updateVenderList)


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
        self.updateVenderList()
        self.ui.verderInfoWidget.updateMenu(qTimeStamp)


    def setUserDefinedTimeView(self):
        self.ui.timeLabel.setText('Time is set to: ')
        self.ui.setDefaultTimeBtn.show()

    
    def setDefaultTimeChanging(self):
        self.setTimeToNow()
        self.ui.setDefaultTimeBtn.hide()
        self.ui.timeLabel.setText('Current Time: ')
        self.timer.start(1000)

    SHOW_OPENING_VENDER = 0
    SHOW_CLOSED_VENDER = 1
    SHOW_ALL_VENDER = 2
    def updateVenderList(self):
        noDisplayedVender = True
        showMode = self.ui.venderTypeBox.currentIndex()
        timeStamp = self.ui.dateTimeEdit.dateTime().toPyDateTime()

        if showMode == CanteenSolutionWidget.SHOW_OPENING_VENDER:
            for item in self.ui.venderListItems:
                vender = item.data(Qt.UserRole)
                if vender.isOpening(timeStamp):
                    noDisplayedVender = False
                    item.setHidden(False)
                    if item.isSelected():
                        self.showVenderInfo(item)
                else:
                    item.setHidden(True)
                    if item.isSelected():
                        self.showVenderInfo(None)

        elif showMode == CanteenSolutionWidget.SHOW_CLOSED_VENDER:
            for item in self.ui.venderListItems:
                vender = item.data(Qt.UserRole)
                if vender.isOpening(timeStamp):
                    item.setHidden(True)
                    if item.isSelected():
                        self.showVenderInfo(None)
                else:
                    noDisplayedVender = False
                    item.setHidden(False)
                    if item.isSelected():
                        self.showVenderInfo(item)

        else:
            noDisplayedVender = False
            for item in self.ui.venderListItems:
                item.setHidden(False)
                if item.isSelected():
                    self.showVenderInfo(item)
        
        if noDisplayedVender:
            self.noAvailableItem.setHidden(False)
        else: self.noAvailableItem.setHidden(True)
    

    def showVenderInfo(self, venderItem):
        if venderItem and venderItem.data(Qt.UserRole):
            vender = venderItem.data(Qt.UserRole)
            qTimeStamp = self.ui.dateTimeEdit.dateTime()
            self.ui.verderInfoWidget.showInfo(vender, qTimeStamp)
        else:
            self.ui.verderInfoWidget.showInfo(None)


