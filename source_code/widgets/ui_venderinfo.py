# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\venderinfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_venderInfoWidget(object):
    def setupUi(self, venderInfoWidget):
        venderInfoWidget.setObjectName("venderInfoWidget")
        #venderInfoWidget.resize(893, 450)

        self.horizontalLayout = QtWidgets.QHBoxLayout(venderInfoWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.venderPhoto = QtWidgets.QLabel(venderInfoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.venderPhoto.sizePolicy().hasHeightForWidth())
        self.venderPhoto.setSizePolicy(sizePolicy)
        self.venderPhoto.setObjectName("venderPhoto")
        self.venderPhoto.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.venderPhoto)
        
        self.venderInfo = QtWidgets.QWidget(venderInfoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.venderInfo.sizePolicy().hasHeightForWidth())
        self.venderInfo.setSizePolicy(sizePolicy)
        self.venderInfo.setObjectName("venderInfo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.venderInfo)
        self.verticalLayout.setObjectName("verticalLayout")

        self.basicInfo = QtWidgets.QTableWidget(self.venderInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.basicInfo.sizePolicy().hasHeightForWidth())
        self.basicInfo.setSizePolicy(sizePolicy)
        self.basicInfo.setMinimumSize(QtCore.QSize(300, 0))
        self.basicInfo.setMaximumSize(QtCore.QSize(16777215, 78))
        self.basicInfo.setShowGrid(True)
        self.basicInfo.setObjectName("basicInfo")
        self.basicInfo.setColumnCount(0)
        self.basicInfo.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.basicInfo.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.basicInfo.setVerticalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.basicInfo)

        self.manuLabel = QtWidgets.QLabel(self.venderInfo)
        self.manuLabel.setScaledContents(False)
        self.manuLabel.setObjectName("manuLabel")
        self.verticalLayout.addWidget(self.manuLabel)

        self.manuTable = QtWidgets.QTableWidget(self.venderInfo)
        self.manuTable.priceColumnWidth = 128
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.manuTable.sizePolicy().hasHeightForWidth())
        self.manuTable.setSizePolicy(sizePolicy)
        self.manuTable.setMinimumSize(QtCore.QSize(0, 0))
        self.manuTable.setObjectName("manuTable")
        self.manuTable.setColumnCount(2)
        self.manuTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.manuTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.manuTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.manuTable)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.openCalculatorBtn = QtWidgets.QPushButton(self.venderInfo)
        self.openCalculatorBtn.setObjectName("openCalculatorBtn")
        self.horizontalLayout_2.addWidget(self.openCalculatorBtn)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.venderInfo)

        self.retranslateUi(venderInfoWidget)
        QtCore.QMetaObject.connectSlotsByName(venderInfoWidget)

    def retranslateUi(self, venderInfoWidget):
        _translate = QtCore.QCoreApplication.translate
        venderInfoWidget.setWindowTitle(_translate("venderInfoWidget", "VenderInfoWidget"))
        self.venderPhoto.setText(_translate("venderInfoWidget", "VenderPhoto"))
        self.basicInfo.setSortingEnabled(False)
        item = self.basicInfo.verticalHeaderItem(0)
        item.setText(_translate("venderInfoWidget", "Name"))
        item = self.basicInfo.verticalHeaderItem(1)
        item.setText(_translate("venderInfoWidget", "Opening Time"))
        self.manuLabel.setText(_translate("venderInfoWidget", "<b>Manu</b>"))
        item = self.manuTable.horizontalHeaderItem(0)
        item.setText(_translate("venderInfoWidget", "Food"))
        item = self.manuTable.horizontalHeaderItem(1)
        item.setText(_translate("venderInfoWidget", "Price"))
        self.openCalculatorBtn.setText(_translate("venderInfoWidget", "Queue Time Calculator"))
