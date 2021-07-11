import sys
import os
import pickle

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.JobLabel import JobLabelWithAdd

# Instantiation du Front_End


class RecurrentJobsWindow(QtWidgets.QWidget):
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

        self.systemBar = QtWidgets.QGroupBox(self)
        self.systemBarLayout = QtWidgets.QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(1200, -30, 100, 50)

        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 10, 1200, 500)

        self.navigationMenu = QtWidgets.QGroupBox(self)
        self.navigationMenuLayout = QtWidgets.QGridLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(10, 600, 675, 100)

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

        for job in jobList:
            with open('Content/Back_End/Recurrent_Jobs/'+job, 'rb') as currentjob:
                task = pickle.load(currentjob)
            self.jobMenuLayout.addWidget(JobLabelWithAdd(task))

        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.navigationMenuLayout.addWidget(self.backButton, 0, 0, 1, 1)
