from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class JobLabelWithRemove(QtWidgets.QWidget):
    def __init__(self, job, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(650, 50))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.job = job
        self.outfit = job.outfit
        self.item = job.item
        self.quantity = job.quantity
        self.macro = job.macro
        self.timeStop = job.timeStop

        self.setLayout(self.layout)
        self.initUI()
        self.setStyleSheet(
            "border-style: solid; color: white;background-color: rgba(0, 0, 0, 0.6); ")

    def removeJob(self):
        self.nativeParentWidget().jobList.remove(self.job)
        self.nativeParentWidget().startQueueWindow()

    def initUI(self):
        self.layout.addWidget(QtWidgets.QLabel(str(self.outfit)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.item)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.quantity)))
        self.layout.addWidget(QtWidgets.QLabel(
            str(self.macro[0]+" "+self.macro[1])))
        self.layout.addWidget(QtWidgets.QLabel(str(self.timeStop)))
        self.removeButton = QtWidgets.QPushButton("X")

        self.removeButton.clicked.connect(
            lambda: self.removeJob())

        self.layout.addWidget(self.removeButton)


class JobLabelWithAdd(QtWidgets.QWidget):
    def __init__(self, job, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QtCore.QSize(650, 50))
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.container)

        self.job = job
        self.outfit = job.outfit
        self.item = job.item
        self.quantity = job.quantity
        self.macro = job.macro
        self.timeStop = job.timeStop

        self.setLayout(self.layout)
        self.initUI()
        self.setStyleSheet(
            "border-style: solid; color: white;background-color: rgba(0, 0, 0, 0.6); ")

    def addJob(self):
        self.nativeParentWidget().jobList.append(self.job)
        self.nativeParentWidget().startQueueWindow()

    def initUI(self):
        self.layout.addWidget(QtWidgets.QLabel(str(self.outfit)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.item)))
        self.layout.addWidget(QtWidgets.QLabel(str(self.quantity)))
        self.layout.addWidget(QtWidgets.QLabel(
            str(self.macro[0]+" "+self.macro[1])))
        self.layout.addWidget(QtWidgets.QLabel(str(self.timeStop)))
        self.addButton = QtWidgets.QPushButton("+")

        self.addButton.clicked.connect(
            lambda: self.addJob())

        self.layout.addWidget(self.addButton)
