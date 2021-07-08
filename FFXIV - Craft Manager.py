import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Windows.MainWindow import MainWindow

# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainWindow()

    sys.exit(app.exec_())
