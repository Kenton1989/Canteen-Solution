from widgets.ui_venderinfo import Ui_venderInfoPage
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidgetItem
from datetime import datetime

class VenderInfoPage(QWidget):

    priceColumnWidth = 130
    rowHeaderColumnWidth = 120

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_venderInfoPage()
        self.ui.setupUi(self)


class VenderInfoWidget(QWidget):
    openCalculatorRequest = pyqtSignal(object)
    def __init__(self):
        super().__init__()

        self.venderInfoPage = VenderInfoPage(self)
        self.emptyPage = QLabel(self)
        
        self.canAPic = QPixmap.fromImage(QImage('test_image\cana.png'))
        self.venderMenu = []
        self.venderImg = QPixmap()
        self.currentVender = None

        self.setupUi()

        self.venderInfoPage.ui.openCalculatorBtn.clicked.connect(self.openCalculator)


    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.emptyPage)
        layout.addWidget(self.venderInfoPage)

        self.emptyPage.setAlignment(Qt.AlignCenter)
        self.adjustEmptyPagePicSize()

        self.venderInfoPage.ui.memuTable.setColumnWidth(1, VenderInfoPage.priceColumnWidth-2)
        self.adjustTableColumnSize()
        self.venderInfoPage.hide()
        #self.setStyleSheet(' { border:1px solid black }')


    def showInfo(self, venderInfo = None, qTimeStamp = None):
        if venderInfo:
            self.emptyPage.hide()
            self.venderInfoPage.show()
            
            if self.currentVender is not venderInfo:
                self.currentVender = venderInfo
                
                #self.venderInfoPage.ui.venderPhoto.resize()
                self.venderImg = QPixmap.fromImage(QImage(venderInfo.photo))
                self.adjustVenderPhotoSize(False)

                basicInfo = self.venderInfoPage.ui.basicInfo
                basicInfo.setItem(0, 0, QTableWidgetItem(venderInfo.name))
                basicInfo.setItem(1, 0, QTableWidgetItem(venderInfo.openingTime))

            self.updateMenu(qTimeStamp, False)
            
            self.adjustTableColumnSize()
        else:
            self.venderInfoPage.hide()
            self.emptyPage.show()
            self.adjustEmptyPagePicSize()


    def updateMenu(self, qTimeStamp, considerIfItIsShow = True):
        if considerIfItIsShow and self.venderInfoPage.isHidden(): return
        
        newMenu = self.currentVender.menu(qTimeStamp.toPyDateTime())
        if newMenu == self.venderMenu:
            return
        else: self.venderMenu = newMenu
        
        menuTable = self.venderInfoPage.ui.memuTable
        menuTable.clearContents()
        menuTable.setRowCount(len(self.venderMenu))
        for i in range(len(self.venderMenu)):
            menuTable.setItem(i, 0, QTableWidgetItem(self.venderMenu[i][0]))
            menuTable.setItem(i, 1, QTableWidgetItem(self.venderMenu[i][1]))


    def resizeEvent(self, e):
        _ = e #avoid unused parameter warning
        self.adjustTableColumnSize()
        self.adjustEmptyPagePicSize()
        self.adjustVenderPhotoSize()


    def adjustTableColumnSize(self):
        basicInfo = self.venderInfoPage.ui.basicInfo
        basicInfo.setColumnWidth(0, basicInfo.size().width()-VenderInfoPage.rowHeaderColumnWidth)
        
        memuTable = self.venderInfoPage.ui.memuTable
        memuTable.setColumnWidth(0, memuTable.size().width()-VenderInfoPage.priceColumnWidth)


    def adjustEmptyPagePicSize(self):
        if self.emptyPage.isHidden(): return

        newPic = self.canAPic.scaled(self.size(), Qt.KeepAspectRatio)
        self.emptyPage.setPixmap(newPic)


    def adjustVenderPhotoSize(self, considerIfItIsShow = True):
        if considerIfItIsShow and self.venderInfoPage.isHidden(): return
        
        photo = self.venderInfoPage.ui.venderPhoto
        (photo.size())
        newPhoto = self.venderImg.scaled(photo.size(), Qt.KeepAspectRatio)
        photo.setPixmap(newPhoto)

    
    def openCalculator(self):
        self.openCalculatorRequest.emit(self.currentVender)
