from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QRect, QSize


class MenuButton(QWidget):

    def __init__(self, parent=None):
        super(MenuButton, self).__init__(parent)
        print("Menu button ", self.nativeParentWidget())
        
        self.state = False


        self.setFixedSize(QSize(200, 100))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.menuButton = QPushButton("Window Modulation")
        self.menuButton.clicked.connect(self.windowModulation)
        self.layout.addWidget(self.menuButton)

    def windowModulation(self):
        self.baseCoords = self.nativeParentWidget().geometry().getCoords()

        if self.state == False:
            for i in range(0, 150):
                self.nativeParentWidget().setGeometry(QRect(self.baseCoords[0],  self.baseCoords[1],  self.baseCoords[2]+1,  self.baseCoords[3]))
            self.nativeParentWidget().startQueueWindow()

        elif self.state == True:
            for i in range(0, 150):
                self.nativeParentWidget().setGeometry(QRect(self.baseCoords[0],  self.baseCoords[1],  self.baseCoords[2]-1,  self.baseCoords[3]))

            self.nativeParentWidget().startQueueWindow()

        self.state = not self.state



            
