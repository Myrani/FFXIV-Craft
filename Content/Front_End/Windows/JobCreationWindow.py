


from PyQt5.QtWidgets import QWidget,QGridLayout,QGroupBox,QHBoxLayout,QVBoxLayout,QPushButton,QMainWindow,QLabel,QLineEdit,QCheckBox
from PyQt5.QtCore import QSize,QCoreApplication


from Content.Front_End.Widgets.CraftMaterial import CraftMaterial
from Content.Back_End.Objects.Job import Job

# Instantiation du Front_End


class JobCreationWindow(QWidget):
    def __init__(self, parent=None):
        super(JobCreationWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.windowLayout = QVBoxLayout()

        self.systemBar = QGroupBox(self)
        self.systemBarLayout = QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(1210, -10, 75, 50)
        self.systemBar.setStyleSheet(
            "QGroupBox {border:0px solid black;}")

        self.jobMenu = QGroupBox(self)
        self.jobMenuLayout = QGridLayout()
        self.jobMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.jobMenu.setLayout(self.jobMenuLayout)
        self.jobMenu.setGeometry(10, 30, 675, 500)
        self.jobMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QLabel{color:white;}")

        self.qualityMenu = QGroupBox(self)
        self.qualityMenuLayout = QVBoxLayout()
        self.qualityMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.qualityMenu.setLayout(self.qualityMenuLayout)
        self.qualityMenu.setGeometry(700, 30, 500, 500)
        self.qualityMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QLabel{color:white;}")

        self.navigationMenu = QGroupBox(self)
        self.navigationMenuLayout = QGridLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(700, 550, 500, 150)
        self.navigationMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6);} QGroupBox > QCheckBox{color:white;}")

        self.windowLayout.addLayout(self.jobMenuLayout)
        self.windowLayout.addLayout(self.navigationMenuLayout)
        self.windowLayout.addLayout(self.qualityMenuLayout)

        self.newJob = Job(11, "string", 0, ["None", "None"], 0, {}, {})
        self.initUIContent()
        self.show()

    def initUIContent(self):

        self.minimizeButton = QPushButton("-")
        self.minimizeButton.setMinimumSize(QSize(20, 20))
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.clicked.connect(
            lambda: QMainWindow.showMinimized(self.nativeParentWidget()))
        self.systemBarLayout.addWidget(self.minimizeButton)

        self.exitButton = QPushButton("X")
        self.exitButton.setMinimumSize(QSize(20, 20))
        self.exitButton.setMaximumSize(QSize(20, 20))
        self.exitButton.clicked.connect(
            lambda: QCoreApplication.exit())
        self.systemBarLayout.addWidget(self.exitButton)

        self.oufitLabel = QLabel("Outfit Number")
        self.oufitDialog = QLineEdit("Outfit")
        self.oufitDialog.textChanged.connect(
            lambda: self.newJob.setOutfit(self.oufitDialog.text()))
        self.jobMenuLayout.addWidget(self.oufitLabel, 0, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.oufitDialog, 1, 0, 1, 1)

        self.itemLabel = QLabel("Item Name")
        self.itemDialog = QLineEdit("Item")
        self.itemDialog.textChanged.connect(
            lambda: self.newJob.setItem(self.itemDialog.text()))

        self.jobMenuLayout.addWidget(self.itemLabel, 2, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.itemDialog, 3, 0, 1, 1)

        self.quantityLabel = QLabel("Item Quantity")
        self.quantityDialog = QLineEdit("Quantity")
        self.quantityDialog.textChanged.connect(
            lambda: self.newJob.setQuantity(self.quantityDialog.text()))

        self.jobMenuLayout.addWidget(self.quantityLabel, 4, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.quantityDialog, 5, 0, 1, 1)

        self.macroLabel = QLabel("Keys to proc the macro")
        self.macroDialog1 = QLineEdit("First Macro")
        self.macroDialog1.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog1.text(), 0))
        self.macroDialog2 = QLineEdit("Second Macro")
        self.macroDialog2.textChanged.connect(
            lambda: self.newJob.setMacro(self.macroDialog2.text(), 1))

        self.jobMenuLayout.addWidget(self.macroLabel, 6, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog1, 7, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.macroDialog2, 7, 1, 1, 1)

        self.timeStopLabel = QLabel("Time between each macro proc")
        self.timeStopDialog = QLineEdit("time")
        self.timeStopDialog.textChanged.connect(
            lambda: self.newJob.setTimeStop(self.timeStopDialog.text()))

        self.jobMenuLayout.addWidget(self.timeStopLabel, 8, 0, 1, 1)
        self.jobMenuLayout.addWidget(self.timeStopDialog, 9, 0, 1, 1)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.navigationMenuLayout.addWidget(self.backButton, 0, 0, 1, 1)

        self.addButton = QPushButton("Add to the list")
        self.addButton.clicked.connect(
            lambda: self.addJob())
        self.navigationMenuLayout.addWidget(self.addButton, 0, 2, 1, 1)

        self.recurrentCheckBox = QCheckBox(
            "Remember this job for an ulterior use ?")
        self.recurrentCheckBox.stateChanged.connect(self.newJob.swapRecurrent)
        self.navigationMenuLayout.addWidget(self.recurrentCheckBox, 1, 2, 1, 1)

        self.craftMaterialQuantityLabel = QLabel(
            "Personalize the quality of each materials")
        self.craftMaterialQuantityDialog = QLineEdit(
            str(self.nativeParentWidget().craftMaterials))
        self.craftMaterialQuantityDialog.textChanged.connect(
            lambda: self.updateCraftMaterialsVariable(self.craftMaterialQuantityDialog.text()))
        self.qualityMenuLayout.addWidget(
            self.craftMaterialQuantityLabel)
        self.qualityMenuLayout.addWidget(
            self.craftMaterialQuantityDialog)

        print(self.nativeParentWidget())
        if isinstance(self.nativeParentWidget().craftMaterials,int):
            for i in range(0, self.nativeParentWidget().craftMaterials):
                self.qualityMenuLayout.addWidget(
                    CraftMaterial(self.newJob, i))

    def updateCraftMaterialsVariable(self, value):
        if value != "":
            self.nativeParentWidget().craftMaterials = int(value)
            self.nativeParentWidget().startJobCreationWindow()

    def addJob(self):
        self.nativeParentWidget().jobList.append(self.newJob)
        if self.newJob.recurrent:
            self.newJob.selfSave()
        self.nativeParentWidget().startQueueWindow()
