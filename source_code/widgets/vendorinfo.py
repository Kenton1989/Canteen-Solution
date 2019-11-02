from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidgetItem

from widgets.ui_vendorinfo import Ui_vendorInfoPage

class vendorInfoPage(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_vendorInfoPage()
        self.ui.setupUi(self)


class vendorInfoWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.vendorInfoPage = vendorInfoPage(self)
        self.welcomePage = QLabel(self)

        self.canAPic = QPixmap.fromImage(QImage('images/can_a.png'))
        # store the data of displaying vendor (default is nothing)
        self.vendorMenu = []
        self.vendorImg = QPixmap()
        self.currentVendor = None

        self.setupUi()


    def setupUi(self):
        # put two page in a widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.welcomePage)
        layout.addWidget(self.vendorInfoPage)
        # set up ui
        self.welcomePage.setAlignment(Qt.AlignCenter)
        self.adjustWelcomePagePicSize()
        self.vendorInfoPage.ui.memuTable.setColumnWidth(1, 128)
        self.adjustTableColumnSize()
        # hide one and keep another one showing
        self.vendorInfoPage.hide()


    def showInfo(self, vendorInfo = None, qTimeStamp = None):
        # show the information provided by vendorInfo
        # if it is None, show the welcome page
        if vendorInfo:
            self.welcomePage.hide()
            self.vendorInfoPage.show()
            # update the information of vendor to be shown
            if self.currentVendor is not vendorInfo:
                self.currentVendor = vendorInfo

                self.vendorImg = QPixmap.fromImage(QImage(vendorInfo.photo))
                # shorten the name
                basicInfo = self.vendorInfoPage.ui.basicInfo
                basicInfo.setItem(0, 0, QTableWidgetItem(vendorInfo.name))
                basicInfo.setItem(1, 0, QTableWidgetItem(vendorInfo.openingTime))
            # update menu
            self.updateMenu(qTimeStamp)
            # update the view
            self.adjustVendorPhotoSize()
            self.adjustTableColumnSize()
        else:
            self.vendorInfoPage.hide()
            self.welcomePage.show()
            self.adjustWelcomePagePicSize()


    def updateMenu(self, qTimeStamp):
        # if the info page is hidden, stop running to minimize the cost
        if self.vendorInfoPage.isHidden():
            return

        # using toPyDateTime is because the database accept python datetime.
        newMenu = self.currentVendor.menu(qTimeStamp.toPyDateTime())
        # if the menu doesn't change, just return
        if newMenu == self.vendorMenu:
            return

        # shorten variable name
        menuTable = self.vendorInfoPage.ui.memuTable
        # update menu table
        self.vendorMenu = newMenu
        menuTable.clearContents()
        menuTable.setRowCount(len(self.vendorMenu))
        for i in range(len(self.vendorMenu)):
            # set food name
            menuTable.setItem(i, 0, QTableWidgetItem(self.vendorMenu[i][0]))
            # set price
            menuTable.setItem(i, 1, QTableWidgetItem(self.vendorMenu[i][1]))


    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.adjustTableColumnSize()
        self.adjustWelcomePagePicSize()
        self.adjustVendorPhotoSize()


    def adjustTableColumnSize(self):
        basicInfo = self.vendorInfoPage.ui.basicInfo
        basicInfo.setColumnWidth(0, basicInfo.size().width()-120)

        memuTable = self.vendorInfoPage.ui.memuTable
        memuTable.setColumnWidth(0, memuTable.size().width()-130)


    def adjustWelcomePagePicSize(self):
        # if the image is hidden, just return to minimize the cost
        if self.welcomePage.isHidden():
            return
        # scale the photo to fill the widget
        newPic = self.canAPic.scaled(self.size(), Qt.KeepAspectRatio)
        self.welcomePage.setPixmap(newPic)


    def adjustVendorPhotoSize(self):
        # if the image is hidden, just return to minimize the cost
        if self.vendorInfoPage.isHidden():
            return
        # scale the photo to fill the widget
        photo = self.vendorInfoPage.ui.vendorPhoto
        newPhoto = self.vendorImg.scaled(photo.size(), Qt.KeepAspectRatio)
        photo.setPixmap(newPhoto)
