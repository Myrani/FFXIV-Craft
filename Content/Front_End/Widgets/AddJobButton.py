from PyQt5.QtWidgets import QWidget,QHBoxLayout,QPushButton
from PyQt5.QtCore import QSize



class AddJobButton(QWidget):
    def __init__(self, parent=None):
        super(AddJobButton, self).__init__(parent=parent)
        self.setFixedSize(QSize(200, 200))
        self.container = QWidget()
        self.layout = QHBoxLayout(self.container)

        self.setLayout(self.layout)
        self.initUI()

        self.setStyleSheet(
            "border-style: solid; background-color: rgba(0, 0, 0, 0.6);color : white; ")

    def initUI(self):
        self.addButton = QPushButton("+ Create a new job ")
        print(self.nativeParentWidget())
        self.addButton.clicked.connect(
            lambda: self.nativeParentWidget().startJobCreationWindow())
        self.layout.addWidget(self.addButton)


class AddJobFromRecurrentButton(QWidget):
    def __init__(self, parent=None):
        super(AddJobFromRecurrentButton, self).__init__(parent=parent)
        self.setFixedSize(QSize(200, 100))
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
    def __init__(self, parent):
        super(StartJobsButton, self).__init__()
        self.parent = parent
        self.setFixedSize(QSize(200, 100))
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
