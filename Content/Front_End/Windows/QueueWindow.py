from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import QThreadPool, QSize, QCoreApplication, Qt, pyqtSlot

from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove, JobRepairLabelWithAdd
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton, StartJobsButton,AddRepairButton
from Content.Front_End.Widgets.MenuButton import MenuButton
from Content.Front_End.Widgets.SystemBar import SystemBar
from Content.Back_End.Objects.JobProcessor import JobProcessor
import sip

# Instantiation du Front_End


class QueueWindow(QWidget):
    def __init__(self, jobList,activityList,menuList, parent=None):
        super(QueueWindow, self).__init__(parent)
        self.threadpool = QThreadPool()
        self.parentWidget = self.parentWidget()
        self.initUI(jobList,activityList,menuList)

    def initUI(self, jobList,activityList,menuList):
        
        self.systemBar = SystemBar(self)

        self.headerMenu = QGroupBox(self)
        self.headerMenuLayout = QVBoxLayout()
        self.headerMenu.setLayout(self.headerMenuLayout)
        self.headerMenu.setGeometry(0, 690, 1280, 30)
        self.headerMenu.setStyleSheet(
            "QGroupBox { border:0px solid black;background-color:rgba(0,0,0,0.6);} QLabel{color:white} ")

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
        self.creationMenu.setGeometry(0, 100, 250, 400)
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

        self.initUIContent(jobList,activityList,menuList)

        self.show()

    def initUIContent(self, jobList,activityList,menuList):


        self.headerMenuLayout.addWidget(QLabel(
            "FFXIV Craft Manager Beta : Version 0.1.15"))


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

        self.creationMenuLayout.addWidget(AddJobButton(self), 0, 0, 1, 1)
        self.creationMenuLayout.addWidget(AddJobFromRecurrentButton(), 1, 0, 1, 1)
        self.creationMenuLayout.addWidget(AddRepairButton(self), 2, 0, 1, 1)
        self.creationMenuLayout.addWidget(StartJobsButton(self), 3, 0, 1, 1)



        self.addJob(jobList)
        self.addActivities(activityList)



    def addJob(self, jobList):
        for job in jobList:
            if job.item != "repair":
                self.jobMenuLayout.addWidget(JobLabelWithRemove(job))
            else:
                self.jobMenuLayout.addWidget(JobRepairLabelWithAdd(job))
    def addActivities(self,activitiesList):
        for activity in activitiesList:
            if not sip.isdeleted(activity):
                self.activityFeedLayout.addWidget(activity)

    def generateJobProcessor(self):
        self.worker = JobProcessor(self.nativeParentWidget().jobList,self.nativeParentWidget().parametters["language"], parent=self)
        self.worker.signals.changeText.connect(self.addActivityOnFeed)
        self.worker.signals.addLabel.connect(self.addLabel)
        self.worker.run()

    def addLabel(self,message):
        object = QLabel(message)
        self.parent().activityList.append(object)
        self.parent().activityList[-1].setStyleSheet("color : white;")
        self.parent().startQueueWindow()
    
    def addActivityOnFeed(self,message):
        self.parent().activityList[-1].setText(message)
        self.parent().startQueueWindow()
        return None