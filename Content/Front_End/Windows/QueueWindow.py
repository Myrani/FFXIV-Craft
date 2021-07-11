import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton
from Content.Back_End.Objects.JobProcessor import JobProcessor

# Instantiation du Front_End


class QueueWindow(QtWidgets.QWidget):
    def __init__(self, jobList, parent=None):
        super(QueueWindow, self).__init__(parent)
        self.initUI(jobList)

    def initUI(self, jobList):

        self.systemBar = QtWidgets.QGroupBox(self)
        self.systemBarLayout = QtWidgets.QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(600, -30, 100, 50)

        self.headerMenu = QtWidgets.QGroupBox(self)
        self.headerMenuLayout = QtWidgets.QVBoxLayout()
        self.headerMenu.setLayout(self.headerMenuLayout)
        self.headerMenu.setGeometry(10, 50, 675, 100)

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
        self.startButton = QtWidgets.QPushButton("Start !")
        self.startButton.clicked.connect(self.generateJobProcessor)
        self.startMenuLayout.addWidget(self.startButton)

        self.minimizeButton = QtWidgets.QPushButton("-")
        self.minimizeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.minimizeButton.setMaximumSize(QtCore.QSize(20, 20))
        self.minimizeButton.clicked.connect(
            lambda: QtCore.QCoreApplication.translate())
        self.systemBarLayout.addWidget(self.minimizeButton)

        self.exitButton = QtWidgets.QPushButton("X")
        self.exitButton.setMinimumSize(QtCore.QSize(20, 20))
        self.exitButton.setMaximumSize(QtCore.QSize(20, 20))
        self.exitButton.clicked.connect(
            lambda: QtCore.QCoreApplication.exit())
        self.systemBarLayout.addWidget(self.exitButton)

    def addJob(self, jobList):
        for job in jobList:
            self.jobMenuLayout.addWidget(
                JobLabelWithRemove(job))
        self.jobMenuLayout.addWidget(AddJobButton())
        self.jobMenuLayout.addWidget(AddJobFromRecurrentButton())

    def generateJobProcessor(self):
        jobProcessor = JobProcessor(self.nativeParentWidget().jobList)
        jobProcessor.start()
