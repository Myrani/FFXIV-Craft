from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class DescriptiveLabel(QtWidgets.QWidget):
    def __init__(self, description, value, parent=None):
        super().__init__(parent=parent)
        self.setMinimumSize(QtCore.QSize(250, 0))
        self.setMaximumSize(QtCore.QSize(250, 75))
        self.description = description
        self.value = value
        self.initUI()

    def initUI(self):

        self.container = QtWidgets.QGroupBox(self)
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.container.setStyleSheet(
            "color: white;background-color: rgba(0, 0, 0, 0.5);")

        self.labelCue = QtWidgets.QLabel(str(self.description))
        self.labelCue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCue.setStyleSheet(
            "color: white;background-color: transparent; ")
        self.layout.addWidget(self.labelCue)

        self.label = QtWidgets.QLabel(str(self.value))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)
