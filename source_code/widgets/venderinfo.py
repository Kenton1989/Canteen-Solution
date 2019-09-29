from widgets.ui_venderinfo import Ui_venderInfoWidget
from PyQt5.QtWidgets import QFrame

class VenderInfoWidget(QFrame):

    def __init__(self, venderInfo = None):
        super().__init__()

        self.ui = Ui_venderInfoWidget()
        self.ui.setupUi(self)
    
    def resizeEvent(self, e):
        _ = e #avoid unused parameter warning
        manuTable = self.ui.manuTable
        self.ui.manuTable.setColumnWidth(0, manuTable.size().width()-manuTable.priceColumnWidth)

