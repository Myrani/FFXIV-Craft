from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class JobLabel(QtWidgets.QWidget):
    def __init__(self, outfit, item, quantity, macro, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(650, 50))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)
        self.outfit = outfit
        self.item = item
        self.quantity = quantity
        self.macro = macro

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid;")

    def initUI(self):
        self.layout.addWidget(QtWidgets.QLabel(str(self.outfit)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.item)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.quantity)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.macro[0])))
        self.layout.addWidget(QtWidgets.QPushButton("X"))
