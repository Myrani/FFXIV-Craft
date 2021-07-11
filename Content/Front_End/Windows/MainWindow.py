import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Windows.QueueWindow import QueueWindow
from Content.Front_End.Windows.JobCreationWindow import JobCreationWindow
from Content.Front_End.Windows.RecurrentJobsWindow import RecurrentJobsWindow
from Content.Back_End.Objects.Job import Job


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setGeometry(10, 10, 700, 930)
        self.jobList = []

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.setWindowOpacity(0.8)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:#6d3a91;")

        self.startQueueWindow()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def startQueueWindow(self):
        self.queueWindow = QueueWindow(self.jobList, parent=self)
        self.setCentralWidget(self.queueWindow)
        self.show()

    def startJobCreationWindow(self):
        self.jobCreationWindow = JobCreationWindow()
        self.setCentralWidget(self.jobCreationWindow)
        self.show()

    def startRecurrentJobsWindow(self):
        self.recurrentJobsWindow = RecurrentJobsWindow()
        self.setCentralWidget(self.recurrentJobsWindow)
        self.show()
