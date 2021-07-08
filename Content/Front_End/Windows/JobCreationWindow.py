import sys


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Content.Front_End.Widgets.JobLabel import JobLabel
from Content.Front_End.Widgets.AddJobButton import AddJobButton

from Content.Back_End.Objects.Job import Job

# Instantiation du Front_End


class JobCreationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(JobCreationWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.jobMenu = QtWidgets.QGroupBox(self)
        self.jobMenuLayout = QtWidgets.QGridLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 110, 675, 700)

        self.newJob = Job(11, "string", 0, ["None", "None"])
        self.initUIContent()
        self.show()

    def initUIContent(self):
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
        self.macroDialog1 = QtWidgets.QLineEdit("Macro")
        self.macroDialog1.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog1.text(), 0))
        self.macroDialog2 = QtWidgets.QLineEdit("Macro")
        self.macroDialog2.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog2.text(), 1))

        self.jobMenuLayout.addWidget(self.macroLabel, 6, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog1, 7, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog2, 7, 1, 1, 1)
