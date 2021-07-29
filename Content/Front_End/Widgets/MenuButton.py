from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QSize


class MenuButton(QWidget):

    def __init__(self, parent=None):
        super(MenuButton, self).__init__(parent=parent)

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
        self.menuButton.clicked.connect(lambda: self.windowModulation())
        self.layout.addWidget(self.menuButton)

    def windowModulation(self):
        mainWindowGeometry = self.nativeParentWidget().geometry().getCoords()
        if self.state == False:
            for i in range(0, 150):
                self.nativeParentWidget().setGeometry(
                    mainWindowGeometry[0], mainWindowGeometry[1], mainWindowGeometry[2]+i, mainWindowGeometry[3])
            self.nativeParentWidget().startQueueWindow()
            self.state = True
            return 0
        elif self.state == True:
            for i in range(0, 150):
                self.nativeParentWidget().setGeometry(
                    mainWindowGeometry[0], mainWindowGeometry[1], mainWindowGeometry[2]-i, mainWindowGeometry[3])

            self.nativeParentWidget().startQueueWindow()
            self.state = False
            return 0
