# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\canteenwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.vendorinfo import vendorInfoWidget

class Ui_canteenSolutionWidget(object):
    def setupUi(self, canteenSolutionWidget):
        canteenSolutionWidget.setObjectName("canteenSolutionWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(canteenSolutionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.timeInfoWidget = QtWidgets.QWidget(canteenSolutionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeInfoWidget.sizePolicy().hasHeightForWidth())
        self.timeInfoWidget.setSizePolicy(sizePolicy)
        self.timeInfoWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.timeInfoWidget.setObjectName("timeInfoWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.timeInfoWidget)
        self.horizontalLayout.setContentsMargins(11, 0, -1, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.timeLabel = QtWidgets.QLabel(self.timeInfoWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(130, 0))
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.timeInfoWidget)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)

        self.setDefaultTimeBtn = QtWidgets.QPushButton(self.timeInfoWidget)
        self.setDefaultTimeBtn.setObjectName("setDefaultTimeBtn")
        self.horizontalLayout.addWidget(self.setDefaultTimeBtn)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.timeInfoWidget)

        self.canteenInfoWidget = QtWidgets.QWidget(canteenSolutionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.canteenInfoWidget.sizePolicy().hasHeightForWidth())
        self.canteenInfoWidget.setSizePolicy(sizePolicy)
        self.canteenInfoWidget.setObjectName("canteenInfoWidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.canteenInfoWidget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.vendorsWidget = QtWidgets.QWidget(self.canteenInfoWidget)
        self.vendorsWidget.setObjectName("vendorsWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.vendorsWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.vendorTypeBox = QtWidgets.QComboBox(self.vendorsWidget)
        self.vendorTypeBox.setObjectName("vendorTypeBox")
        self.vendorTypeBox.addItem("")
        self.vendorTypeBox.addItem("")
        self.vendorTypeBox.addItem("")
        self.verticalLayout_2.addWidget(self.vendorTypeBox)

        self.vendorList = QtWidgets.QListWidget(self.vendorsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendorList.sizePolicy().hasHeightForWidth())
        self.vendorList.setSizePolicy(sizePolicy)
        self.vendorList.setIconSize(QtCore.QSize(40,40))
        self.vendorList.setObjectName("vendorList")

        self.verticalLayout_2.addWidget(self.vendorList)
        self.horizontalLayout_2.addWidget(self.vendorsWidget)

        self.verderInfoWidget = vendorInfoWidget()
        self.verderInfoWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setHeightForWidth(self.verderInfoWidget.sizePolicy().hasHeightForWidth())
        self.verderInfoWidget.setSizePolicy(sizePolicy)
        self.verderInfoWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.verderInfoWidget.setObjectName("verderInfoWidget")
        self.horizontalLayout_2.addWidget(self.verderInfoWidget)

        self.verticalLayout.addWidget(self.canteenInfoWidget)

        self.retranslateUi(canteenSolutionWidget)
        QtCore.QMetaObject.connectSlotsByName(canteenSolutionWidget)

    def retranslateUi(self, canteenSolutionWidget):
        _translate = QtCore.QCoreApplication.translate
        canteenSolutionWidget.setWindowTitle(_translate("canteenSolutionWidget", "Form"))
        self.timeLabel.setText(_translate("canteenSolutionWidget", "Current Time: "))
        self.dateTimeEdit.setDisplayFormat(_translate("canteenSolutionWidget", "yyyy-MM-dd hh:mm:ss"))
        self.setDefaultTimeBtn.setText(_translate("canteenSolutionWidget", "Set To Default"))
        self.vendorTypeBox.setItemText(0, _translate("canteenSolutionWidget", "Opening vendor"))
        self.vendorTypeBox.setItemText(1, _translate("canteenSolutionWidget", "Closed vendor"))
        self.vendorTypeBox.setItemText(2, _translate("canteenSolutionWidget", "All vendor"))
