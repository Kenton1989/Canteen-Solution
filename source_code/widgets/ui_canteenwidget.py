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
        sizePolicy.setHeightForWidth(self.timeInfoWidget.sizePolicy().hasHeightForWidth())
        self.timeInfoWidget.setSizePolicy(sizePolicy)
        self.timeInfoWidget.setObjectName("timeInfoWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.timeInfoWidget)
        self.horizontalLayout.setContentsMargins(11, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.promptMsg = QtWidgets.QLabel(self.timeInfoWidget)
        self.promptMsg.setObjectName("promptMsg")
        self.horizontalLayout.addWidget(self.promptMsg)
        self.time = QtWidgets.QLabel(self.timeInfoWidget)
        self.time.setObjectName("time")
        self.horizontalLayout.addWidget(self.time)
        self.changeTimeButton = QtWidgets.QPushButton(self.timeInfoWidget)
        self.changeTimeButton.setObjectName("changeTimeButton")
        self.horizontalLayout.addWidget(self.changeTimeButton)
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
        self.venderList = QtWidgets.QListWidget(self.canteenInfoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setHeightForWidth(self.venderList.sizePolicy().hasHeightForWidth())
        self.venderList.setSizePolicy(sizePolicy)
        self.venderList.setObjectName("venderList")
        self.horizontalLayout_2.addWidget(self.venderList)

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
        self.promptMsg.setText(_translate("canteenSolutionWidget", "The time is set to"))
        self.time.setText(_translate("canteenSolutionWidget", "1970-01-01 00:00:00"))
        self.changeTimeButton.setText(_translate("canteenSolutionWidget", "Change Time"))
