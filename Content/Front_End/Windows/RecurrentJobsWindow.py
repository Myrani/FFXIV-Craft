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
        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QVBoxLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 110, 675, 700)

        for job in jobList:
            with open('Content/Back_End/Recurrent_Jobs/'+job, 'rb') as currentjob:
                task = pickle.load(currentjob)
            self.jobMenuLayout.addWidget(JobLabelWithAdd(task))
