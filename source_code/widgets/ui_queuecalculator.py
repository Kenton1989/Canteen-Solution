# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\queuecalculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_queueCalculator(object):
    def setupUi(self, queueCalculator):
        queueCalculator.setObjectName("queueCalculator")
        queueCalculator.resize(370, 230)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(queueCalculator)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vendorHLayout = QtWidgets.QHBoxLayout()
        self.vendorHLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vendorHLayout.setObjectName("vendorHLayout")
        self.vendorLabel = QtWidgets.QLabel(queueCalculator)
        self.vendorLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.vendorLabel.setObjectName("vendorLabel")
        self.vendorHLayout.addWidget(self.vendorLabel)
        self.vendorComboBox = QtWidgets.QComboBox(queueCalculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.vendorComboBox.sizePolicy().hasHeightForWidth())
        self.vendorComboBox.setSizePolicy(sizePolicy)
        self.vendorComboBox.setObjectName("vendorComboBox")
        self.vendorHLayout.addWidget(self.vendorComboBox)
        self.verticalLayout_2.addLayout(self.vendorHLayout)
        self.qNumHLayout = QtWidgets.QHBoxLayout()
        self.qNumHLayout.setObjectName("qNumHLayout")
        self.qNumLabel = QtWidgets.QLabel(queueCalculator)
        self.qNumLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.qNumLabel.setObjectName("qNumLabel")
        self.qNumHLayout.addWidget(self.qNumLabel)
        self.qNumLineEdit = QtWidgets.QLineEdit(queueCalculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.qNumLineEdit.sizePolicy().hasHeightForWidth())
        self.qNumLineEdit.setSizePolicy(sizePolicy)
        self.qNumLineEdit.setObjectName("qNumLineEdit")
        self.qNumHLayout.addWidget(self.qNumLineEdit)
        self.verticalLayout_2.addLayout(self.qNumHLayout)
        self.outputLabel = QtWidgets.QLabel(queueCalculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputLabel.sizePolicy().hasHeightForWidth())
        self.outputLabel.setSizePolicy(sizePolicy)
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_2.addWidget(self.outputLabel)
        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.buttonHLayout.setObjectName("buttonHLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonHLayout.addItem(spacerItem)
        self.calculateBtn = QtWidgets.QPushButton(queueCalculator)
        self.calculateBtn.setObjectName("calculateBtn")
        self.buttonHLayout.addWidget(self.calculateBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonHLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.buttonHLayout)

        self.retranslateUi(queueCalculator)
        QtCore.QMetaObject.connectSlotsByName(queueCalculator)

    def retranslateUi(self, queueCalculator):
        _translate = QtCore.QCoreApplication.translate
        queueCalculator.setWindowTitle(_translate("queueCalculator", "Queue Time Calculator"))
        self.vendorLabel.setText(_translate("queueCalculator", "vendor"))
        self.qNumLabel.setText(_translate("queueCalculator", "Queue Length"))
        self.calculateBtn.setText(_translate("queueCalculator", "Calculate"))
