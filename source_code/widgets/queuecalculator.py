from widgets.ui_queuecalculator import Ui_queueCalculator
from PyQt5.QtWidgets import QDialog

from widgets.blinking_widget import make_label_can_blink, blink

class QueueCalculator(QDialog):

    BAD_INPUT = -1

    def __init__(self, parent, vendorsInfo):
        super().__init__(parent)

        # store database
        self.vendorsInfo = vendorsInfo
        # set up basic UI
        self.ui = Ui_queueCalculator()
        self.ui.setupUi(self)
        # fill the list of combo box with the database
        self.setupVendorComboBox()
        # let the output can blink
        # when error happens, the hint will more obvious
        make_label_can_blink(self.ui.outputLabel)

        self.ui.calculateBtn.clicked.connect(self.calculateTime)


    def setupVendorComboBox(self):
		# add the data of vendor into the combo box
        comboBox = self.ui.vendorComboBox
        for vendor in self.vendorsInfo:
            comboBox.addItem(vendor.name, vendor)
        comboBox.setCurrentIndex(-1)


    def setToDefault(self):
		# set all the widget to the default value (empty)
		# will be called when the dialog is closed
        self.ui.vendorComboBox.setCurrentIndex(-1)
        self.ui.qNumLineEdit.setText('')
        self.output(' ')
        self.resize(370, 230)


    def openWithVendor(self, vendor):
		# open the dialog and set the content of vendor combo box
		# to the given one
        comboBox = self.ui.vendorComboBox
        self.show()
        comboBox.setCurrentIndex(comboBox.findData(vendor))


    def calculateTime(self):
		# calculate the time to wait and put the result in the output label
		# if something wrong happens, the error message will be put in the output label
        if self.ui.vendorComboBox.currentIndex() < 0:
            self.output('Error: No vendor is chosen.', True)
            return QueueCalculator.BAD_INPUT
        vendor = self.ui.vendorComboBox.currentData()
        # get the length of queue from user input.
        queueLen = self.getQueueLen()
        if queueLen < 0:
            return QueueCalculator.BAD_INPUT

        time = vendor.queueTime(queueLen)

        self.output('The queue time is about %.1f min'%time)



    def getQueueLen(self):
        # return the queue number user input in ui.qNumLineEdit if it can be parsed
		# if input is invalid, print error meaasge in the output label and return BAD_INPUT (-1)
        inputVal = self.ui.qNumLineEdit.text().strip()
        if not inputVal:
            self.output('Error: The queue length is empty.', True)
            return QueueCalculator.BAD_INPUT

        try:
            num = int(inputVal)
        except ValueError:
            self.output('Error: The queue length is not integer.', True)
            return QueueCalculator.BAD_INPUT

        if num < 0:
            self.output('Error: The queue length is negative.', True)
            return QueueCalculator.BAD_INPUT

        return num


    def output(self, meg, isErr = False):
        # print the message on the UI in a label
        self.ui.outputLabel.setText(meg)
        # for error message, blinking will make it more obvious
        if isErr:
            blink(self.ui.outputLabel)


    def closeEvent(self, e):
        _ = e # avoid unused parameter warning
        self.setToDefault()

