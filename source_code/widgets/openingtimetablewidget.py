# Done by Wei Kaitao

from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from widgets.ui_openingtimetable import Ui_openingTimeTableWidget


class OpeningTimetableWidget(QDialog):
    def __init__(self, parent, vendorInfo):
        super().__init__(parent)
        # create ui
        self.ui = Ui_openingTimeTableWidget()
        self.ui.setupUi(self)
        # import infomation
        self.vendorInfo = vendorInfo
        self.setupTimeTable()
        # fix ui
        self.adjustColumnSize()

    def setupTimeTable(self):
        # shorten variable name
        table = self.ui.openingTimeTable

        table.setRowCount(len(self.vendorInfo))
        # loop through venderInfo,
        # and display info. of each vendor in one row
        row = 0
        for vendor in self.vendorInfo:
            table.setItem(row, 0, QTableWidgetItem(vendor.name))
            table.setItem(row, 1, QTableWidgetItem(vendor.openingTime))
            row += 1

    def adjustColumnSize(self):
        # shorten name
        table = self.ui.openingTimeTable
        storeNameWidth = max(200, int(table.width()*2/5)-1)
        openingTimeWidth = max(300, int(table.width()*3/5)-1)
        table.setColumnWidth(0, storeNameWidth)
        table.setColumnWidth(1, openingTimeWidth)

    def resizeEvent(self, e):
        self.adjustColumnSize()
        super().resizeEvent(e)
