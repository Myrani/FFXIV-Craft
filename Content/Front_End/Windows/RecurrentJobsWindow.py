import sys
import os
import pickle

from PyQt5.QtWidgets import QWidget,QGridLayout,QGroupBox,QHBoxLayout,QVBoxLayout,QPushButton,QMainWindow
from PyQt5.QtCore import QSize,QCoreApplication

from Content.Front_End.Widgets.JobLabel import JobLabelWithAdd

# Instantiation du Front_End


class RecurrentJobsWindow(QWidget):
    def __init__(self, parent=None):
        super(RecurrentJobsWindow, self).__init__(parent)
        self.initUI(self.getAllRecurrentJobs())

    def getAllRecurrentJobs(self):
        list_of_jobs = []

        for root, dirs, files in os.walk("Content/Back_End/Recurrent_Jobs/"):
            for file in files:
                list_of_jobs.append(file)
        print(list_of_jobs)

        return list_of_jobs

    def initUI(self, jobList):

        self.systemBar = QGroupBox(self)
        self.systemBarLayout = QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(1210, -10, 75, 50)
        self.systemBar.setStyleSheet(
            "QGroupBox {border:0px solid black;}")


        self.jobMenu = QGroupBox(self)
        self.jobMenuLayout = QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 10, 1200, 500)
        self.jobMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.navigationMenu = QGroupBox(self)
        self.navigationMenuLayout = QGridLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(10, 600, 675, 100)
        self.navigationMenu.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.minimizeButton = QPushButton("-")
        self.minimizeButton.setMinimumSize(QSize(20, 20))
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.clicked.connect(
            lambda: QMainWindow.showMinimized(self.nativeParentWidget()))
        self.systemBarLayout.addWidget(self.minimizeButton)
        self.minimizeButton.setStyleSheet(
            "QGroupBox {border:0px solid black;}")



        self.exitButton = QPushButton("X")
        self.exitButton.setMinimumSize(QSize(20, 20))
        self.exitButton.setMaximumSize(QSize(20, 20))
        self.exitButton.clicked.connect(
            lambda: QCoreApplication.exit())
        self.systemBarLayout.addWidget(self.exitButton)

        for job in jobList:
            with open('Content/Back_End/Recurrent_Jobs/'+job, 'rb') as currentjob:
                task = pickle.load(currentjob)
            self.jobMenuLayout.addWidget(JobLabelWithAdd(task))

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.navigationMenuLayout.addWidget(self.backButton, 0, 0, 1, 1)
