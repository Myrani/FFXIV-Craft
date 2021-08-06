from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QPushButton, QLabel



from Content.Front_End.Widgets.SystemBar import SystemBar



class HelpWindow(QWidget):
    def __init__(self,parent=None):
        super(HelpWindow,self).__init__(parent=parent)
        self.systemBar = SystemBar(self)
        self.systemBar.helpButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);color :black ;")

        self.helpMenu = QGroupBox(self)
        self.helpMenuLayout = QGridLayout()
        self.helpMenu.setLayout(self.helpMenuLayout)
        self.helpMenu.setGeometry(10, 40, 1260, 660)
        self.helpMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")

        self.initUIContent()
        self.show()

    def initUIContent(self):
        self.helpLabel = QLabel("Please for the time being, refer to the Github tutorial ! ->>> <a href=\"https://github.com/Myrani/FFXIV-Craft\#tutorial\">https://github.com/Myrani/FFXIV-Craft#tutorial</a>")
        self.helpLabel.setStyleSheet("color:white;  a>link{color:white;}")
        self.helpLabel.setOpenExternalLinks(True)
        self.helpMenuLayout.addWidget(self.helpLabel,0,0,4,4)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.helpMenuLayout.addWidget(self.backButton,6,6,1,1)