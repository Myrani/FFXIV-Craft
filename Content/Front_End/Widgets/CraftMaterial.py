from PyQt5.QtWidgets import QWidget,QGridLayout,QGroupBox,QLabel,QLineEdit

class CraftMaterial(QWidget):
    def __init__(self, job, index, parent=None):
        super(CraftMaterial, self).__init__(parent)
        self.index = index
        self.job = job

        self.qualityMenu = QGroupBox(self)
        self.qualityMenuLayout = QGridLayout()
        self.qualityMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.qualityMenu.setGeometry(0, 0, 500, 75)
        self.qualityMenu.setLayout(self.qualityMenuLayout)
        self.qualityMenu.setStyleSheet(
            "background-color: transparent:color :white")

        self.itemLabel = QLabel(
            "Item " + str(self.index+1) + " specs")
        self.lowQualityLabel = QLabel("Low quality materials")
        self.lowQualityDialog = QLineEdit("0")
        self.lowQualityDialog.textChanged.connect(
            lambda: self.job.setLowQuality(self.index, self.lowQualityDialog.text()))
        self.qualityMenuLayout.addWidget(self.itemLabel, 0, 0, 1, 1)
        self.qualityMenuLayout.addWidget(self.lowQualityLabel, 1, 0, 1, 1)
        self.qualityMenuLayout.addWidget(self.lowQualityDialog, 1, 1, 1, 1)

        self.highQualityLabel = QLabel("High quality materials")
        self.highQualityDialog = QLineEdit("0")
        self.highQualityDialog.textChanged.connect(
            lambda: self.job.setHighQuality(self.index, self.highQualityDialog.text()))
        self.qualityMenuLayout.addWidget(self.highQualityLabel, 1, 2, 1, 1)
        self.qualityMenuLayout.addWidget(self.highQualityDialog, 1, 3, 1, 1)
