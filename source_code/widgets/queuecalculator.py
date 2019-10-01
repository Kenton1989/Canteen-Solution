from widgets.ui_queuecalculator import Ui_queueCalculator
from PyQt5.QtWidgets import QDialog
import re

class QueueCalculator(QDialog):
    
    BAD_INPUT = -1

    def __init__(self, vendersInfo):
        super().__init__()

        self.ui = Ui_queueCalculator()
        self.ui.setupUi(self)
        self.vendersInfo = vendersInfo

        self.setupVenderComboBox()
        self.ui.calculateBtn.clicked.connect(self.calculateTime)


    def setupVenderComboBox(self):
        comboBox = self.ui.venderComboBox
        for vender in self.vendersInfo:
            comboBox.addItem(vender.name, vender)
        comboBox.setCurrentIndex(-1)


    def setToDefault(self):
        self.ui.venderComboBox.setCurrentIndex(-1)
        self.ui.qNumLineEdit.setText('')
        self.output('')
        self.resize(370, 230)


    def openWithVender(self, vender):
        comboBox = self.ui.venderComboBox
        self.open()
        comboBox.setCurrentIndex(comboBox.findData(vender))


    def calculateTime(self):        
        if self.ui.venderComboBox.currentIndex() < 0:
            self.output('Error: No vender is chosen.')
            return QueueCalculator.BAD_INPUT
        vender = self.ui.venderComboBox.currentData()
        
        queueLen = self.getQueueLen()
        if queueLen < 0:
            return QueueCalculator.BAD_INPUT

        time = vender.queueTime(queueLen)

        self.output('The queue time is about %.1f min'%time)


    #return the queue number user inputed in ui.qNumLineEdit if it can be parsed
    #return BAD_INPUT (-1) if input is invalid
    def getQueueLen(self):
        
        inputVal = self.ui.qNumLineEdit.text().strip()
        if not inputVal:
            self.output('Error: The queue length is empty.')
            return QueueCalculator.BAD_INPUT

        try:
            num = int(inputVal)
        except ValueError:
            self.output('Error: The queue length is not integer.')
            return QueueCalculator.BAD_INPUT
        
        if num < 0:
            self.output('Error: The queue length is negative.')

        return num
    

    def output(self, meg):
        self.ui.outputLabel.setText(meg)


    def closeEvent(self, e):
        self.setToDefault()

