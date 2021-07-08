import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton

# Instantiation du Front_End


class QueueWindow(QtWidgets.QWidget):
    def __init__(self, jobList, parent=None):
        super(QueueWindow, self).__init__(parent)
        self.initUI(jobList)

    def initUI(self, jobList):
        self.headerMenu = QtWidgets.QGroupBox(self)
        self.headerMenuLayout = QtWidgets.QVBoxLayout()
        self.headerMenu.setLayout(self.headerMenuLayout)
        self.headerMenu.setGeometry(10, 10, 675, 100)

        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 110, 675, 700)

        self.startMenu = QtWidgets.QGroupBox(self)
        self.startMenuLayout = QtWidgets.QVBoxLayout()
        self.startMenu.setLayout(self.startMenuLayout)
        self.startMenu.setGeometry(10, 810, 675, 100)

        self.initUIContent(jobList)

        self.show()

    def initUIContent(self, jobList):

        self.addJob(jobList)
        self.startMenuLayout.addWidget(QtWidgets.QPushButton("Start !"))

    def addJob(self, jobList):
        for job in jobList:
            self.jobMenuLayout.addWidget(
                JobLabelWithRemove(job))
        self.jobMenuLayout.addWidget(AddJobButton())
        self.jobMenuLayout.addWidget(AddJobFromRecurrentButton())
