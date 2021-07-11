import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton
from Content.Back_End.Objects.JobProcessor import JobProcessor
from Content.Back_End.Objects.PyQtWorker import Worker
# Instantiation du Front_End


class QueueWindow(QtWidgets.QWidget):
    def __init__(self, jobList, parent=None):
        super(QueueWindow, self).__init__(parent)
        self.threadpool = QtCore.QThreadPool()

        self.initUI(jobList)

    def initUI(self, jobList):

        self.systemBar = QtWidgets.QGroupBox(self)
        self.systemBarLayout = QtWidgets.QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(1200, -20, 75, 50)
        self.systemBar.setStyleSheet(
            "QGroupBox {border:0px solid black;}")


        self.headerMenu = QtWidgets.QGroupBox(self)
        self.headerMenuLayout = QtWidgets.QVBoxLayout()
        self.headerMenu.setLayout(self.headerMenuLayout)
        self.headerMenu.setGeometry(0, -40, 400, 100)
        self.headerMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.headerLabel = QtWidgets.QGroupBox(self)
        self.headerLabelLayout = QtWidgets.QVBoxLayout()
        self.headerLabel.setLayout(self.headerLabelLayout)
        self.headerLabel.setGeometry(275, 70, 200, 50)
        self.headerLabel.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.creationMenu = QtWidgets.QGroupBox(self)
        self.creationMenuLayout = QtWidgets.QVBoxLayout()
        self.creationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.creationMenu.setLayout(self.creationMenuLayout)
        self.creationMenu.setGeometry(10, 110, 250, 300)
        self.creationMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(275, 110, 1000, 500)
        self.jobMenu.setStyleSheet("QGroupBox {border:3px solid black;}")

        self.startMenu = QtWidgets.QGroupBox(self)
        self.startMenuLayout = QtWidgets.QVBoxLayout()
        self.startMenu.setLayout(self.startMenuLayout)
        self.startMenu.setGeometry(600, 600, 675, 100)
        self.startMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")


        self.initUIContent(jobList)

        self.show()

    def initUIContent(self, jobList):

        self.minimizeButton = QtWidgets.QPushButton("-")
        self.minimizeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.minimizeButton.setMaximumSize(QtCore.QSize(20, 20))
        self.minimizeButton.clicked.connect(
            lambda: QtWidgets.QMainWindow.showMinimized(self.nativeParentWidget()))
        self.systemBarLayout.addWidget(self.minimizeButton)

        self.exitButton = QtWidgets.QPushButton("X")
        self.exitButton.setMinimumSize(QtCore.QSize(20, 20))
        self.exitButton.setMaximumSize(QtCore.QSize(20, 20))
        self.exitButton.clicked.connect(
            lambda: QtCore.QCoreApplication.exit())
        self.systemBarLayout.addWidget(self.exitButton)

        self.headerMenuLayout.addWidget(QtWidgets.QLabel(
            "FFXIV Craft Manager Beta : Version 0.0.1"))

        self.currentJobLabel = QtWidgets.QLabel("Current Joblist")
        self.currentJobLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentJobLabel.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0.6);color:white;}")
        self.headerLabelLayout.addWidget(self.currentJobLabel)

        self.addJob(jobList)
        self.startButton = QtWidgets.QPushButton("Start the bulk crafting!")
        self.startButton.setStyleSheet(
            "border-style: solid; background-color: black;color : white; ")
        self.startButton.clicked.connect(self.generateJobProcessor)
        self.startMenuLayout.addWidget(self.startButton)

    def addJob(self, jobList):
        for job in jobList:
            self.jobMenuLayout.addWidget(
                JobLabelWithRemove(job))
        self.creationMenuLayout.addWidget(AddJobButton())
        self.creationMenuLayout.addWidget(AddJobFromRecurrentButton())

    def generateJobProcessor(self):
        jobProcessor = JobProcessor(self.nativeParentWidget().jobList)
        self.worker = Worker(JobProcessor(
            self.nativeParentWidget().jobList).start)
        self.threadpool.start(self.worker)
