

from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import QSize, QCoreApplication


from Content.Front_End.Widgets.CraftMaterial import CraftMaterial
from Content.Back_End.Objects.Job import Job
from Content.Front_End.Widgets.SystemBar import SystemBar

# Instantiation du Front_End


class JobCreationWindow(QWidget):
    def __init__(self, parent=None):
        super(JobCreationWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.windowLayout = QVBoxLayout()

        self.systemBar = SystemBar(self)
        
        print(self.nativeParentWidget())
        self.jobMenu = QGroupBox(self)
        self.jobMenuLayout = QGridLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 50, 675, 500)
        self.jobMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QLabel{color:white;} QGroupBox > QPushButton {border-style:solid;color:white;background-color:rgba(0, 0, 0, 0.6);} QGroupBox > QPushButton::hover{background-color: rgba(255, 255, 255, 0.6);color :black ;}")

        self.qualityMenu = QGroupBox(self)
        self.qualityMenuLayout = QVBoxLayout()
        self.qualityMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.qualityMenu.setLayout(self.qualityMenuLayout)
        self.qualityMenu.setGeometry(700, 50, 500, 500)
        self.qualityMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QLabel{color:white;}")

        self.navigationMenu = QGroupBox(self)
        self.navigationMenuLayout = QGridLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(700, 560, 500, 150)
        self.navigationMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QCheckBox{color:white;} QGroupBox > QPushButton {border-style:solid;color:white;background-color:rgba(0, 0, 0, 0.6);} QGroupBox > QPushButton::hover{background-color: rgba(255, 255, 255, 0.6);color :black ;}")

        self.windowLayout.addLayout(self.jobMenuLayout)
        self.windowLayout.addLayout(self.navigationMenuLayout)
        self.windowLayout.addLayout(self.qualityMenuLayout)

        self.initUIContent()
        self.show()

    def initUIContent(self):

        self.oufitLabel = QLabel("Outfit Number")
        self.oufitDialog = QLineEdit(str(self.nativeParentWidget().newJob.getOutfit()))
        self.oufitDialog.setPlaceholderText("number")
        self.oufitDialog.textChanged.connect(
            lambda: self.nativeParentWidget().newJob.setOutfit(self.oufitDialog.text()))
        self.jobMenuLayout.addWidget(self.oufitLabel, 0, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.oufitDialog, 1, 0, 1, 1)

        self.itemLabel = QLabel("Item")
        self.itemDialog = QLineEdit(str(self.nativeParentWidget().newJob.getItem()))
        self.itemDialog.setPlaceholderText("Item")
        self.itemDialog.textChanged.connect(
            lambda: self.nativeParentWidget().newJob.setItem(self.itemDialog.text()))

        self.jobMenuLayout.addWidget(self.itemLabel, 2, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.itemDialog, 3, 0, 1, 1)

        self.quantityLabel = QLabel("Quantity")
        self.quantityDialog = QLineEdit(str(self.nativeParentWidget().newJob.getQuantity()))
        self.quantityDialog.setPlaceholderText("Custom")
        self.quantityDialog.textChanged.connect(
            lambda: self.nativeParentWidget().newJob.setQuantity(self.quantityDialog.text()))

        self.jobMenuLayout.addWidget(self.quantityLabel, 4, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.quantityDialog, 5, 0, 1, 1)

        self.macroLabel = QLabel("Keys to proc the macro")
        self.macroDialog1 = QLineEdit(str(self.nativeParentWidget().newJob.getMacro(0)))
        self.macroDialog1.setPlaceholderText("First Macro")
        self.macroDialog1.textChanged.connect(
            lambda: self.nativeParentWidget().newJob.setMacro(self.macroDialog1.text(), 0))
        self.macroDialog2 = QLineEdit(str(self.nativeParentWidget().newJob.getMacro(1)))    
        self.macroDialog2.setPlaceholderText("Second Macro")
        self.macroDialog2.textChanged.connect(
            lambda: self.nativeParentWidget().newJob.setMacro(self.macroDialog2.text(), 1))

        self.jobMenuLayout.addWidget(self.macroLabel, 6, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog1, 7, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog2, 7, 1, 1, 1)

        self.timeStopLabel = QLabel("Time between each macro proc")
        self.timeStopDialog = QLineEdit(str(self.nativeParentWidget().newJob.getTimeStop()))
        #self.timeStopDialog.setPlaceholderText()
        self.timeStopDialog.editingFinished.connect(
            lambda: self.updateTime(self.timeStopDialog.text()))

        self.defaultDialog35s = QPushButton("35 Seconds")
        self.defaultDialog35s.setFixedSize(QSize(300,25))
        self.defaultDialog35s.clicked.connect(
            lambda: self.updateTime("35"))

        self.defaultDialog70s = QPushButton("70 Seconds")
        self.defaultDialog70s.setFixedSize(QSize(300,25))

        self.defaultDialog70s.clicked.connect(
            lambda: self.updateTime("70"))

        self.jobMenuLayout.addWidget(self.defaultDialog35s, 9, 1, 1, 1)
        self.jobMenuLayout.addWidget(self.defaultDialog70s, 9, 1, 2, 1)

        self.jobMenuLayout.addWidget(self.timeStopLabel, 8, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.timeStopDialog, 9, 0, 1, 1)

        self.backButton = QPushButton("Back")
        self.backButton.setFixedSize(QSize(200,50))
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.navigationMenuLayout.addWidget(self.backButton, 0, 0, 1, 1)

        self.addButton = QPushButton("Add to the list")
        self.addButton.setFixedSize(QSize(200,50))
        self.addButton.clicked.connect(
            lambda: self.addJob())
        self.navigationMenuLayout.addWidget(self.addButton, 0, 2, 1, 1)

        self.recurrentCheckBox = QCheckBox(
            "Remember this job for an ulterior use ?")
        self.recurrentCheckBox.stateChanged.connect(self.nativeParentWidget().newJob.swapRecurrent)
        self.navigationMenuLayout.addWidget(self.recurrentCheckBox, 1, 2, 1, 1)

        self.craftMaterialQuantityLabel = QLabel(
            "Number of materials for the craft")
        self.craftMaterialQuantityDialog = QLineEdit(
            str(self.nativeParentWidget().craftMaterials))
        self.craftMaterialQuantityDialog.textChanged.connect(
            lambda: self.updateCraftMaterialsVariable(self.craftMaterialQuantityDialog.text()))
        self.qualityMenuLayout.addWidget(
            self.craftMaterialQuantityLabel)
        self.qualityMenuLayout.addWidget(
            self.craftMaterialQuantityDialog)

        print(self.nativeParentWidget())
        if isinstance(self.nativeParentWidget().craftMaterials, int):
            for i in range(0, self.nativeParentWidget().craftMaterials):
                self.qualityMenuLayout.addWidget(
                    CraftMaterial(i))
    
    def updateTime(self,time):
        self.nativeParentWidget().newJob.setTimeStop(time)
        self.timeStopDialog.setText(time)
        self.nativeParentWidget().startJobCreationWindow()

    def updateCraftMaterialsVariable(self, value):
        if value != "":
            self.nativeParentWidget().craftMaterials = int(value)
            self.nativeParentWidget().startJobCreationWindow()

    def addJob(self):
        self.nativeParentWidget().jobList.append(self.nativeParentWidget().newJob)
        if self.nativeParentWidget().newJob.recurrent:
            self.nativeParentWidget().newJob.selfSave()
        self.nativeParentWidget().newJob = Job(1, "", 0, ["", ""], 0, {}, {})
        self.nativeParentWidget().startQueueWindow()
