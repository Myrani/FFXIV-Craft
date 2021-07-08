from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class AddJobButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddJobButton, self).__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(200, 200))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: yellow;")

    def initUI(self):
        self.addButton = QtWidgets.QPushButton(" Add a New Job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startJobCreationWindow())
        self.layout.addWidget(self.addButton)


class AddJobFromRecurrentButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddJobFromRecurrentButton, self).__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(200, 200))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: yellow;")

    def initUI(self):
        self.addButton = QtWidgets.QPushButton(" Add a Recurrent job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startRecurrentJobsWindow())
        self.layout.addWidget(self.addButton)
