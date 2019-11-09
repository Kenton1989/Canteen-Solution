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
		# if some error happens, the error message will be put in the output label
        if self.ui.vendorComboBox.currentIndex() < 0:
            self.errorMsg('Error: No vendor is chosen.')
            return
        vendor = self.ui.vendorComboBox.currentData()
        # get the length of queue from user input.
        queueLen = self.getQueueLen()
        # incase of fail to get a positive number
        if queueLen < 0:
            return
        
        # incase of the extremely large input
        if queueLen > 10000:
            self.errorMsg("Serious? So many people in Canteen A?")
            return

        # calculate the queue time
        queueTime = vendor.queueTime(queueLen)

        if queueTime < 0.1:
            self.output('It is your turn now :)')
        elif queueTime < 1:
            self.output('The queue time is about %.1f seconds' % round(queueTime*60))
        elif queueTime < 1.05:
            self.output('The queue time is about 1 minute.')            
        elif queueTime < 30:
            self.output('The queue time is about %.1f minutes.' % queueTime)
        else:
            self.output('The queue time is about %.1f minutes.\n' % queueTime +
                        'It is recommended to change a stall.')
        


    def getQueueLen(self):
        # return the queue number user input in ui.qNumLineEdit if it can be parsed
        # if input is invalid, print error meaasge in the output label and return BAD_INPUT (-1)
        inputVal = self.ui.qNumLineEdit.text().strip()
        if not inputVal:
            self.errorMsg('Error: The queue length is empty.')
            return QueueCalculator.BAD_INPUT

        try:
            num = int(inputVal)
        except ValueError:
            self.errorMsg('Error: The queue length is not integer.')
            return QueueCalculator.BAD_INPUT

        if num < 0:
            self.errorMsg('Error: The queue length is negative.')
            return QueueCalculator.BAD_INPUT

        return num


    def output(self, msg):
        # print the message on the UI in a label
        self.ui.outputLabel.setText(msg)
    
    
    def errorMsg(self, msg):
        # print the message on the UI in a label
        self.ui.outputLabel.setText(msg)
        # blink to obviously notify
        blink(self.ui.outputLabel)


    def closeEvent(self, e):
        self.setToDefault()
        super().closeEvent(e)

