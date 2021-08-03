
import os
import sys


from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap

from Content.Front_End.Windows.QueueWindow import QueueWindow
from Content.Front_End.Windows.JobCreationWindow import JobCreationWindow
from Content.Front_End.Windows.RecurrentJobsWindow import RecurrentJobsWindow
from Content.Front_End.Widgets.MenuButton import MenuButton

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Content\\Back_End\\") 
        #"."
        #"Content\\Back_End\\"
    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 10, 1280, 720)
        # Persistent parametters
        self.jobList = []
        self.activityList = []
        self.craftMaterials = 0
        self.menuButtons = []



        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setWindowOpacity(0.95)

        self.label_background = QLabel("transparent ", self)
        self.label_background.setGeometry(0, 0, 1280, 720)
        #self.label_background.move(0, 0)
        pixmap = QPixmap(
            resource_path('Visual_Ressources\\FFXIV.jpeg')).scaled(self.size())
        self.label_background.setPixmap(pixmap)

        self.setWindowFlags(Qt.FramelessWindowHint)
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
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def startQueueWindow(self):
        self.queueWindow = QueueWindow(self.jobList,self.activityList,self.menuButtons ,parent=self)
        self.setCentralWidget(self.queueWindow)
        self.show()

    def startJobCreationWindow(self):
        self.jobCreationWindow = JobCreationWindow(parent=self)
        self.setCentralWidget(self.jobCreationWindow)
        self.show()

    def startRecurrentJobsWindow(self):
        self.recurrentJobsWindow = RecurrentJobsWindow(parent=self)
        self.setCentralWidget(self.recurrentJobsWindow)
        self.show()
