from Content.Back_End.Objects.Job import Job
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QSize


class AddJobButton(QWidget):
    def __init__(self, parent=None):
        super(AddJobButton, self).__init__(parent=parent)
        self.setFixedSize(QSize(200, 50))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QPushButton("+ Create a new job ")
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startJobCreationWindow())
        self.layout.addWidget(self.addButton)

class AddRepairButton(QWidget):
    def __init__(self, parent=None):
        super(AddRepairButton, self).__init__(parent=parent)

        self.repairJob = Job("","repair","",["",""],"","","")

        self.setFixedSize(QSize(200, 50))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")
    def addRepairButton(self):
        self.nativeParentWidget().jobList.append(self.repairJob)
        self.nativeParentWidget().startQueueWindow()
    def initUI(self):
        self.addButton = QPushButton("+ Add a Repair All")
        self.addButton.clicked.connect(
            lambda: self.addRepairButton())
        self.layout.addWidget(self.addButton)

class AddJobFromRecurrentButton(QWidget):
    def __init__(self, parent=None):
        super(AddJobFromRecurrentButton, self).__init__(parent=parent)
        self.setFixedSize(QSize(200, 50))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QPushButton("+ Add a recurrent job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startRecurrentJobsWindow())
        self.layout.addWidget(self.addButton)


class StartJobsButton(QWidget):
    def __init__(self, parent=None):
        super(StartJobsButton, self).__init__(parent)
        self.parent = parent
        self.setFixedSize(QSize(200, 50))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QPushButton("- Start Crafting -")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.parent.generateJobProcessor())
        self.layout.addWidget(self.addButton)
