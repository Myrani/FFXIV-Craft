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
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QtWidgets.QPushButton("+ Create a new job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startJobCreationWindow())
        self.layout.addWidget(self.addButton)


class AddJobFromRecurrentButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddJobFromRecurrentButton, self).__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(200, 100))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QtWidgets.QPushButton("+ Add a recurrent job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startRecurrentJobsWindow())
        self.layout.addWidget(self.addButton)


class StartJobsButton(QtWidgets.QWidget):
    def __init__(self, parent):
        super(StartJobsButton, self).__init__()
        self.parent = parent
        self.setFixedSize(QtCore.QSize(200, 100))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QtWidgets.QPushButton("- Start Crafting -")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.parent.generateJobProcessor())
        self.layout.addWidget(self.addButton)
