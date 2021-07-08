import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Windows.QueueWindow import QueueWindow
from Content.Front_End.Windows.JobCreationWindow import JobCreationWindow
from Content.Back_End.Objects.Job import Job


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setGeometry(10, 10, 700, 930)
        self.jobList = [Job(11, "Madrier", 1, ["ctrl", "&"])]
        self.startQueueWindow()

    def startQueueWindow(self):
        self.queueWindow = QueueWindow(self.jobList, parent=self)
        self.setCentralWidget(self.queueWindow)
        self.show()

    def startJobCreationWindow(self):
        self.queueWindow = JobCreationWindow()
        self.setCentralWidget(self.queueWindow)
        self.show()
