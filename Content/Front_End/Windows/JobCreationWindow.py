import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.AddJobButton import AddJobButton

from Content.Back_End.Objects.Job import Job

# Instantiation du Front_End


class JobCreationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(JobCreationWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.windowLayout = QtWidgets.QVBoxLayout()

        self.systemBar = QtWidgets.QGroupBox(self)
        self.systemBarLayout = QtWidgets.QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(600, -30, 100, 50)

        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QGridLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 30, 675, 700)

        self.navigationMenu = QtWidgets.QGroupBox(self)
        self.navigationMenuLayout = QtWidgets.QGridLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(10, 710, 675, 200)

        self.windowLayout.addLayout(self.jobMenuLayout)
        self.windowLayout.addLayout(self.navigationMenuLayout)

        self.newJob = Job(11, "string", 0, ["None", "None"], 0)
        self.initUIContent()
        self.show()

    def initUIContent(self):

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

        self.oufitLabel = QtWidgets.QLabel("Outfit Number")
        self.oufitDialog = QtWidgets.QLineEdit("Outfit")
        self.oufitDialog.textChanged.connect(
            lambda: self.newJob.setOutfit(self.oufitDialog.text()))
        self.jobMenuLayout.addWidget(self.oufitLabel, 0, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.oufitDialog, 1, 0, 1, 1)

        self.itemLabel = QtWidgets.QLabel("Item Name")
        self.itemDialog = QtWidgets.QLineEdit("Item")
        self.itemDialog.textChanged.connect(
            lambda: self.newJob.setItem(self.itemDialog.text()))

        self.jobMenuLayout.addWidget(self.itemLabel, 2, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.itemDialog, 3, 0, 1, 1)

        self.quantityLabel = QtWidgets.QLabel("Item Quantity")
        self.quantityDialog = QtWidgets.QLineEdit("Quantity")
        self.quantityDialog.textChanged.connect(
            lambda: self.newJob.setQuantity(self.quantityDialog.text()))

        self.jobMenuLayout.addWidget(self.quantityLabel, 4, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.quantityDialog, 5, 0, 1, 1)

        self.macroLabel = QtWidgets.QLabel("Keys to proc the macro")
        self.macroDialog1 = QtWidgets.QLineEdit("First Macro")
        self.macroDialog1.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog1.text(), 0))
        self.macroDialog2 = QtWidgets.QLineEdit("Second Macro")
        self.macroDialog2.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog2.text(), 1))

        self.jobMenuLayout.addWidget(self.macroLabel, 6, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog1, 7, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog2, 7, 1, 1, 1)

        self.timeStopLabel = QtWidgets.QLabel("Time between each macro proc")
        self.timeStopDialog = QtWidgets.QLineEdit("time")
        self.timeStopDialog.textChanged.connect(
            lambda: self.newJob.setTimeStop(self.timeStopDialog.text()))

        self.jobMenuLayout.addWidget(self.timeStopLabel, 8, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.timeStopDialog, 9, 0, 1, 1)

        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.navigationMenuLayout.addWidget(self.backButton, 0, 0, 1, 1)

        self.addButton = QtWidgets.QPushButton("Add to the list")
        self.addButton.clicked.connect(
            lambda: self.addJob())
        self.navigationMenuLayout.addWidget(self.addButton, 0, 2, 1, 1)

        self.recurrentCheckBox = QtWidgets.QCheckBox(
            "Remember this job for an ulterior use ?")
        self.recurrentCheckBox.stateChanged.connect(self.newJob.swapRecurrent)
        self.navigationMenuLayout.addWidget(self.recurrentCheckBox, 1, 2, 1, 1)

    def addJob(self):
        self.nativeParentWidget().jobList.append(self.newJob)
        if self.newJob.recurrent:
            self.newJob.selfSave()
        self.nativeParentWidget().startQueueWindow()
