from PyQt5.QtWidgets import QWidget,QGroupBox,QHBoxLayout,QPushButton
class MenuBar(QWidget):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent=parent)
        self.navigationMenu = QGroupBox(self)
        self.navigationMenuLayout = QHBoxLayout()
        self.navigationMenuLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationMenu.setLayout(self.navigationMenuLayout)
        self.navigationMenu.setGeometry(0, 0, 100, 200)
        self.initUI()

    def initUI(self):
        self.exitButton = QPushButton("X")
        self.exitButton.clicked.connect(lambda: self.close())
        self.navigationMenuLayout.addWidget(self.exitButton)
