from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import QThreadPool, QSize, QCoreApplication, Qt

from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton, StartJobsButton
from Content.Front_End.Widgets.MenuButton import MenuButton

from Content.Back_End.Objects.JobProcessor import JobProcessor


# Instantiation du Front_End


class QueueWindow(QWidget):
    def __init__(self, jobList, parent=None):
        super(QueueWindow, self).__init__(parent)
        self.threadpool = QThreadPool()

        self.initUI(jobList)

    def initUI(self, jobList):

        self.systemBar = QGroupBox(self)
        self.systemBarLayout = QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(1210, -10, 75, 50)
        self.systemBar.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.headerMenu = QGroupBox(self)
        self.headerMenuLayout = QVBoxLayout()
        self.headerMenu.setLayout(self.headerMenuLayout)
        self.headerMenu.setGeometry(0, -40, 400, 100)
        self.headerMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.headerLabel = QGroupBox(self)
        self.headerLabelLayout = QVBoxLayout()
        self.headerLabel.setLayout(self.headerLabelLayout)
        self.headerLabel.setGeometry(210, 70, 200, 50)
        self.headerLabel.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.creationMenu = QGroupBox(self)
        self.creationMenuLayout = QGridLayout()
        self.creationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.creationMenu.setLayout(self.creationMenuLayout)
        self.creationMenu.setGeometry(10, 100, 250, 400)
        self.creationMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.jobMenu = QGroupBox(self)
        self.jobMenuLayout = QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(225, 110, 700, 500)
        self.jobMenu.setStyleSheet("QGroupBox {border:3px solid black;}")

        self.activityFeed = QGroupBox(self)
        self.activityFeedLayout = QVBoxLayout(self)
        self.activityFeedLayout.setContentsMargins(10, 10, 10, 10)
        self.activityFeed.setLayout(self.activityFeedLayout)
        self.activityFeed.setGeometry(930, 110, 300, 500)
        self.activityFeed.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")

        self.activityHeaderLabel = QGroupBox(self)
        self.activityHeaderLabelLayout = QVBoxLayout(self)
        self.activityHeaderLabel.setLayout(self.activityHeaderLabelLayout)
        self.activityHeaderLabel.setGeometry(915, 70, 200, 50)
        self.activityHeaderLabel.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.startMenu = QGroupBox(self)
        self.startMenuLayout = QVBoxLayout(self)
        self.startMenu.setLayout(self.startMenuLayout)
        self.startMenu.setGeometry(600, 600, 675, 100)
        self.startMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.initUIContent(jobList)

        self.show()

    def initUIContent(self, jobList):

        self.addJob(jobList)

        self.minimizeButton = QPushButton("-")
        self.minimizeButton.setMinimumSize(QSize(20, 20))
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.clicked.connect(
            lambda: QMainWindow.showMinimized(self.nativeParentWidget()))
        self.systemBarLayout.addWidget(self.minimizeButton)

        self.exitButton = QPushButton("X")
        self.exitButton.setMinimumSize(QSize(20, 20))
        self.exitButton.setMaximumSize(QSize(20, 20))
        self.exitButton.clicked.connect(
            lambda: QCoreApplication.exit())
        self.systemBarLayout.addWidget(self.exitButton)

        self.headerMenuLayout.addWidget(QLabel(
            "FFXIV Craft Manager Beta : Version 0.0.5"))

        self.currentJobLabel = QLabel("Current Joblist")
        self.currentJobLabel.setAlignment(Qt.AlignCenter)
        self.currentJobLabel.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0.6);color:white;}")
        self.headerLabelLayout.addWidget(self.currentJobLabel)

        self.currentActivityLabel = QLabel("Activity feed")
        self.currentActivityLabel.setAlignment(Qt.AlignCenter)
        self.currentActivityLabel.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0.6);color:white;}")
        self.activityHeaderLabelLayout.addWidget(self.currentActivityLabel)

        self.creationMenuLayout.addWidget(AddJobButton(), 0, 0, 1, 1)
        self.creationMenuLayout.addWidget(
            AddJobFromRecurrentButton(), 1, 0, 1, 1)
        self.creationMenuLayout.addWidget(StartJobsButton(self), 2, 0, 1, 1)
        self.creationMenuLayout.addWidget(
            self.nativeParentWidget().menuButton[0], 3, 0, 1, 1)

    def addJob(self, jobList):
        for job in jobList:
            self.jobMenuLayout.addWidget(
                JobLabelWithRemove(job))

    def generateJobProcessor(self):
        self.worker = JobProcessor(self.nativeParentWidget().jobList, self)
        self.worker.signals.result.connect(self.addActivityOnFeed)
        self.worker.signals.finished.connect(self.addActivityOnFeed)
        self.worker.signals.progress.connect(self.addActivityOnFeed)
        self.threadpool.start(self.worker)

    def addActivityOnFeed(self, message):
        self.activityCue = QLabel(message)
        self.activityCue.setStyleSheet("color : white; ")
        self.activityFeedLayout.addWidget(self.activityCue)
