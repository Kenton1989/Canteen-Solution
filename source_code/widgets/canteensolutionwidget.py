from widgets.ui_canteenwidget import Ui_canteenSolutionWidget
from PyQt5.QtWidgets import QWidget

class CanteenSolutionWidget(QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_canteenSolutionWidget()
        self.ui.setupUi(self)
