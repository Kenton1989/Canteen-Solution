# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.canteensolutionwidget import CanteenSolutionWidget


class Ui_mainWindow(object):
    def setupUi(self, mainWindow, vendorInfo):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 750)
        mainWindow.setMinimumSize(QtCore.QSize(950, 500))
        self.centralWidget = CanteenSolutionWidget(mainWindow, vendorInfo)
        self.centralWidget.setObjectName("centralWidget")
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        mainWindow.setMenuBar(self.menuBar)
        self.actionChangeTime = QtWidgets.QAction(mainWindow)
        self.actionChangeTime.setObjectName("actionChangeTime")
        self.actionShowAllOpeningTime = QtWidgets.QAction(mainWindow)
        self.actionShowAllOpeningTime.setObjectName("actionShowAllOpeningTime")
        self.actionShowOtherVendor = QtWidgets.QAction(mainWindow)
        self.actionShowOtherVendor.setObjectName("actionShowOtherVendor")
        self.actionQueueTimeCalculator = QtWidgets.QAction(mainWindow)
        self.actionQueueTimeCalculator.setObjectName("actionQueueTimeCalculator")
        self.menuTools.addAction(self.actionShowAllOpeningTime)
        self.menuTools.addAction(self.actionChangeTime)
        self.menuTools.addAction(self.actionShowOtherVendor)
        self.menuTools.addAction(self.actionQueueTimeCalculator)
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Real-time Canteen Information System"))
        self.menuTools.setTitle(_translate("mainWindow", "&Tools"))
        self.actionChangeTime.setText(_translate("mainWindow", "Change Time to ..."))
        self.actionShowAllOpeningTime.setText(_translate("mainWindow", "All stall's opening time"))
        self.actionShowOtherVendor.setText(_translate("mainWindow", "Show other stalls"))
        self.actionQueueTimeCalculator.setText(_translate("mainWindow", "Queue Time Calculator"))
