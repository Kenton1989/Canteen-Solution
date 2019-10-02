from widgets.ui_vendorinfo import Ui_vendorInfoPage
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidgetItem
from datetime import datetime

class vendorInfoPage(QWidget):

    priceColumnWidth = 130
    rowHeaderColumnWidth = 120

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_vendorInfoPage()
        self.ui.setupUi(self)


class vendorInfoWidget(QWidget):
    openCalculatorRequest = pyqtSignal(object)
    def __init__(self):
        super().__init__()

        self.vendorInfoPage = vendorInfoPage(self)
        self.emptyPage = QLabel(self)
        
        self.canAPic = QPixmap.fromImage(QImage('test_image\cana.png'))
        self.vendorMenu = []
        self.vendorImg = QPixmap()
        self.currentvendor = None

        self.setupUi()

        self.vendorInfoPage.ui.openCalculatorBtn.clicked.connect(self.openCalculator)


    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.emptyPage)
        layout.addWidget(self.vendorInfoPage)

        self.emptyPage.setAlignment(Qt.AlignCenter)
        self.adjustEmptyPagePicSize()

        self.vendorInfoPage.ui.memuTable.setColumnWidth(1, vendorInfoPage.priceColumnWidth-2)
        self.adjustTableColumnSize()
        self.vendorInfoPage.hide()
        #self.setStyleSheet(' { border:1px solid black }')


    def showInfo(self, vendorInfo = None, qTimeStamp = None):
        if vendorInfo:
            self.emptyPage.hide()
            self.vendorInfoPage.show()
            
            if self.currentvendor is not vendorInfo:
                self.currentvendor = vendorInfo
                
                #self.vendorInfoPage.ui.vendorPhoto.resize()
                self.vendorImg = QPixmap.fromImage(QImage(vendorInfo.photo))
                self.adjustvendorPhotoSize(False)

                basicInfo = self.vendorInfoPage.ui.basicInfo
                basicInfo.setItem(0, 0, QTableWidgetItem(vendorInfo.name))
                basicInfo.setItem(1, 0, QTableWidgetItem(vendorInfo.openingTime))

            self.updateMenu(qTimeStamp, False)
            
            self.adjustTableColumnSize()
        else:
            self.vendorInfoPage.hide()
            self.emptyPage.show()
            self.adjustEmptyPagePicSize()


    def updateMenu(self, qTimeStamp, considerIfItIsShow = True):
        if considerIfItIsShow and self.vendorInfoPage.isHidden(): return
        
        newMenu = self.currentvendor.menu(qTimeStamp.toPyDateTime())
        if newMenu == self.vendorMenu:
            return
        else: self.vendorMenu = newMenu
        
        menuTable = self.vendorInfoPage.ui.memuTable
        menuTable.clearContents()
        menuTable.setRowCount(len(self.vendorMenu))
        for i in range(len(self.vendorMenu)):
            menuTable.setItem(i, 0, QTableWidgetItem(self.vendorMenu[i][0]))
            menuTable.setItem(i, 1, QTableWidgetItem(self.vendorMenu[i][1]))


    def resizeEvent(self, e):
        _ = e #avoid unused parameter warning
        self.adjustTableColumnSize()
        self.adjustEmptyPagePicSize()
        self.adjustvendorPhotoSize()


    def adjustTableColumnSize(self):
        basicInfo = self.vendorInfoPage.ui.basicInfo
        basicInfo.setColumnWidth(0, basicInfo.size().width()-vendorInfoPage.rowHeaderColumnWidth)
        
        memuTable = self.vendorInfoPage.ui.memuTable
        memuTable.setColumnWidth(0, memuTable.size().width()-vendorInfoPage.priceColumnWidth)


    def adjustEmptyPagePicSize(self):
        if self.emptyPage.isHidden(): return

        newPic = self.canAPic.scaled(self.size(), Qt.KeepAspectRatio)
        self.emptyPage.setPixmap(newPic)


    def adjustvendorPhotoSize(self, considerIfItIsShow = True):
        if considerIfItIsShow and self.vendorInfoPage.isHidden(): return
        
        photo = self.vendorInfoPage.ui.vendorPhoto
        (photo.size())
        newPhoto = self.vendorImg.scaled(photo.size(), Qt.KeepAspectRatio)
        photo.setPixmap(newPhoto)

    
    def openCalculator(self):
        self.openCalculatorRequest.emit(self.currentvendor)
