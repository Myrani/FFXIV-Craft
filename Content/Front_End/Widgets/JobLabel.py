from Content.Front_End.Widgets.DescriptiveLabel import DescriptiveLabel
from PyQt5.QtCore import (QSize)
from PyQt5.QtWidgets import (QHBoxLayout,QLabel,QPushButton,QWidget)
import os


class JobLabelWithRemove(QWidget):
    def __init__(self, job, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QSize(650, 100))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.job = job
        self.outfit = job.outfit
        self.item = job.item
        self.quantity = job.quantity
        self.macro = job.macro
        self.timeStop = job.timeStop
        self.lowQuality = job.lowQuality
        self.highQuality = job.highQuality

        self.setLayout(self.layout)
        self.initUI()
        # self.setStyleSheet(
        #    "border-style: solid black 5px ; color: white;background-color: rgba(0, 0, 0, 0.6); ")

        self.container.setStyleSheet("border-style: solid black 5px ")

    def removeJob(self):
        self.nativeParentWidget().jobList.remove(self.job)
        self.nativeParentWidget().startQueueWindow()

    def initUI(self):

        self.outfitLabel = DescriptiveLabel("Outfit", self.outfit)
        self.layout.addWidget(self.outfitLabel)

        self.itemLabel = DescriptiveLabel("Item", self.item)
        self.layout.addWidget(self.itemLabel)

        self.quantityLabel = DescriptiveLabel("Quantity", str(self.quantity))
        self.layout.addWidget(self.quantityLabel)

        self.macroLabel = DescriptiveLabel(
            "Macro", str(self.macro[0]+" + "+self.macro[1]))
        self.layout.addWidget(self.macroLabel)

        self.timeStopLabel = DescriptiveLabel(
            "Time", str(self.timeStop)+" s")
        self.layout.addWidget(self.timeStopLabel)

        self.lowQualityLabel = DescriptiveLabel(
            "LQ", str(self.lowQuality))
        self.layout.addWidget(self.lowQualityLabel)

        self.highQualityLabel = DescriptiveLabel(
            "HQ", str(self.highQuality))
        self.layout.addWidget(self.highQualityLabel)

        self.removeButton = QPushButton("X")
        self.removeButton.setStyleSheet(
            "color: white;background-color: rgba(0, 0, 0, 0.5);")

        self.removeButton.clicked.connect(
            lambda: self.removeJob())

        self.layout.addWidget(self.removeButton)


class JobLabelWithAdd(QWidget):
    def __init__(self, job, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QSize(650, 50))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.job = job
        self.outfit = job.outfit
        self.item = job.item
        self.quantity = job.quantity
        self.macro = job.macro
        self.timeStop = job.timeStop

        self.setLayout(self.layout)
        self.initUI()
        self.setStyleSheet(
            "border-style: solid; color: white;background-color: rgba(0, 0, 0, 0.6); ")

    def addJob(self):
        self.nativeParentWidget().jobList.append(self.job)
        self.nativeParentWidget().startQueueWindow()

    def delete(self):
        os.remove(self.job.file)
        self.nativeParentWidget().startRecurrentJobsWindow()


    def initUI(self):
        self.layout.addWidget(QLabel(str(self.outfit)))
        self.layout.addWidget(QLabel(str(self.item)))
        self.layout.addWidget(QLabel(str(self.quantity)))
        self.layout.addWidget(QLabel(
            str(self.macro[0]+" "+self.macro[1])))
        self.layout.addWidget(QLabel(str(self.timeStop)))
        self.addButton = QPushButton("+")
        self.addButton.clicked.connect(
            lambda: self.addJob())
        self.layout.addWidget(self.addButton)
        self.removeButton = QPushButton("-")
        
        self.removeButton.clicked.connect(
            lambda: self.delete())
        self.layout.addWidget(self.removeButton)


class JobRepairLabelWithAdd(QWidget):
    def __init__(self, job, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QSize(650, 100))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)
        self.job = job
        self.outfit = job.outfit
        self.item = job.item
        self.quantity = job.quantity
        self.macro = job.macro
        self.timeStop = job.timeStop
        self.lowQuality = job.lowQuality
        self.highQuality = job.highQuality

        self.setLayout(self.layout)
        self.initUI()
        # self.setStyleSheet(
        #    "border-style: solid black 5px ; color: white;background-color: rgba(0, 0, 0, 0.6); ")

        self.container.setStyleSheet("border-style: solid black 5px ")

    def removeJob(self):
        self.nativeParentWidget().jobList.remove(self.job)
        self.nativeParentWidget().startQueueWindow()

    def initUI(self):

        self.itemLabel = QLabel(self.item)
        self.itemLabel.setFixedSize(QSize(650,50))
        self.itemLabel.setStyleSheet(
            "color: white;background-color: rgba(0, 0, 0, 0.5);")
        self.layout.addWidget(self.itemLabel)


        self.removeButton = QPushButton("X")
        self.removeButton.setStyleSheet(
            "color: white;background-color: rgba(0, 0, 0, 0.5);")

        self.removeButton.clicked.connect(
            lambda: self.removeJob())

        self.layout.addWidget(self.removeButton)
