from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class AddJobButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(200, 200))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: yellow;")

    def initUI(self):
        self.layout.addWidget(QtWidgets.QPushButton(" Add New Job"))
