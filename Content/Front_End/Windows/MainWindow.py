import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import os
from Content.Front_End.Windows.QueueWindow import QueueWindow
from Content.Front_End.Windows.JobCreationWindow import JobCreationWindow
from Content.Front_End.Windows.RecurrentJobsWindow import RecurrentJobsWindow
from Content.Back_End.Objects.Job import Job


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setGeometry(10, 10, 1280, 720)
        self.jobList = []
        self.craftMaterials = 0

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.setWindowOpacity(0.95)

        self.label_background = QtWidgets.QLabel("transparent ", self)
        self.label_background.setGeometry(0, 0, 1280, 720)
        #self.label_background.move(0, 0)
        pixmap = QtGui.QPixmap(
            'Content/Back_End/Visual_Ressources/FFXIV.jpeg').scaled(self.size())
        self.label_background.setPixmap(pixmap)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("background-color:#6d3a91;")

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
        self.jobCreationWindow = JobCreationWindow(parent=self)
        self.setCentralWidget(self.jobCreationWindow)
        self.show()

    def startRecurrentJobsWindow(self):
        self.recurrentJobsWindow = RecurrentJobsWindow()
        self.setCentralWidget(self.recurrentJobsWindow)
        self.show()
