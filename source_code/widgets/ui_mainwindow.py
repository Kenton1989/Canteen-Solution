# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1

from widgets.canteensolutionwidget import CanteenSolutionWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        

        self.centralWidget = CanteenSolutionWidget()
        self.centralWidget.setObjectName("centralWidget")
        mainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = mainWindow.menuBar()
        #self.menuBar.setGeometry(QtCore.QRect(0, 0, 1105, 25))
        self.menuBar.setObjectName("menuBar")
        
        self.menuTool = QtWidgets.QMenu(self.menuBar)
        self.menuTool.setObjectName("menuTool")
        mainWindow.setMenuBar(self.menuBar)
        
        #self.mainToolBar = QtWidgets.QToolBar(mainWindow)
        #self.mainToolBar.setObjectName("mainToolBar")
        #mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuTool.menuAction())

        mainWindow.resize(1200, 750)
        mainWindow.setMinimumSize(QtCore.QSize(750, 600))
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Canteen Solution"))
        self.menuTool.setTitle(_translate("mainWindow", "&Tool"))
