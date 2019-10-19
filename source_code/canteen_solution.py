from widgets import mainwindow
from vendor_model import allVendor
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainwindow.MainWindow(allVendor())
    window.show()
    
    sys.exit(app.exec_())

