from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class MenuBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent=parent)
        self.navigationMenu = QtWidgets.QGroupBox(self)
        self.navigationMenuLayout = QtWidgets.QHBoxLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(0, 0, 100, 200)
        self.initUI()

    def initUI(self):
        self.exitButton = QtWidgets.QPushButton("X")
        self.exitButton.clicked.connect(lambda: self.close())
        self.navigationMenuLayout.addWidget(self.exitButton)
