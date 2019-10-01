# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\canteenwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.venderinfo import VenderInfoWidget

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

        self.VendersWidget = QtWidgets.QWidget(self.canteenInfoWidget)
        self.VendersWidget.setObjectName("VendersWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.VendersWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.venderTypeBox = QtWidgets.QComboBox(self.VendersWidget)
        self.venderTypeBox.setObjectName("venderTypeBox")
        self.venderTypeBox.addItem("")
        self.venderTypeBox.addItem("")
        self.venderTypeBox.addItem("")
        self.verticalLayout_2.addWidget(self.venderTypeBox)

        self.venderList = QtWidgets.QListWidget(self.VendersWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.venderList.sizePolicy().hasHeightForWidth())
        self.venderList.setSizePolicy(sizePolicy)
        self.venderList.setIconSize(QtCore.QSize(40,40))
        self.venderList.setObjectName("venderList")

        self.verticalLayout_2.addWidget(self.venderList)
        self.horizontalLayout_2.addWidget(self.VendersWidget)

        self.verderInfoWidget = VenderInfoWidget()
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
        self.venderTypeBox.setItemText(0, _translate("canteenSolutionWidget", "Opening Vender"))
        self.venderTypeBox.setItemText(1, _translate("canteenSolutionWidget", "Closed Vender"))
        self.venderTypeBox.setItemText(2, _translate("canteenSolutionWidget", "All Vender"))
