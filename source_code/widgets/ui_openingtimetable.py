# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\openingtimetable.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_openingTimeTableWidget(object):
    def setupUi(self, openingTimeTableWidget):
        openingTimeTableWidget.setObjectName("openingTimeTableWidget")
        openingTimeTableWidget.resize(540, 320)
        self.horizontalLayout = QtWidgets.QHBoxLayout(openingTimeTableWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openingTimeTable = QtWidgets.QTableWidget(openingTimeTableWidget)
        self.openingTimeTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.openingTimeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.openingTimeTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.openingTimeTable.setObjectName("openingTimeTable")
        self.openingTimeTable.setColumnCount(2)
        self.openingTimeTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.openingTimeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.openingTimeTable.setHorizontalHeaderItem(1, item)
        self.openingTimeTable.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.openingTimeTable)

        self.retranslateUi(openingTimeTableWidget)
        QtCore.QMetaObject.connectSlotsByName(openingTimeTableWidget)

    def retranslateUi(self, openingTimeTableWidget):
        _translate = QtCore.QCoreApplication.translate
        openingTimeTableWidget.setWindowTitle(_translate("openingTimeTableWidget", "Opening Time of All Stalls"))
        item = self.openingTimeTable.horizontalHeaderItem(0)
        item.setText(_translate("openingTimeTableWidget", "Store"))
        item = self.openingTimeTable.horizontalHeaderItem(1)
        item.setText(_translate("openingTimeTableWidget", "Opening Time"))
