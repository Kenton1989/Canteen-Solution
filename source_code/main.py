# Done by Wei Kaitao
# Dislay information on main window, monitor user input until exit.

import sys
from PyQt5.QtWidgets import QApplication
from vendor_model import allVendor
from widgets import mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vendorInfo = allVendor()
    window = mainwindow.MainWindow(vendorInfo)
    window.show()

    sys.exit(app.exec_())

