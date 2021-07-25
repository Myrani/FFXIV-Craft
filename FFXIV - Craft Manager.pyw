import sys
import os

from PyQt5.QtWidgets import QApplication


from Content.Front_End.Windows.MainWindow import MainWindow

# Instantiation du Front_End





if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = MainWindow()

    sys.exit(app.exec_())
