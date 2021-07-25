from PyQt5.QtWidgets import QWidget,QGroupBox,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt,QSize

class DescriptiveLabel(QWidget):
    def __init__(self, description, value, parent=None):
        super().__init__(parent=parent)
        self.setMinimumSize(QSize(250, 0))
        self.setMaximumSize(QSize(250, 75))
        self.description = description
        self.value = value
        self.initUI()

    def initUI(self):

        self.container = QGroupBox(self)
        self.layout = QVBoxLayout(self.container)
        self.container.setStyleSheet(
            "color: white;background-color: rgba(0, 0, 0, 0.5);")

        self.labelCue = QLabel(str(self.description))
        self.labelCue.setAlignment(Qt.AlignCenter)
        self.labelCue.setStyleSheet(
            "color: white;background-color: transparent; ")
        self.layout.addWidget(self.labelCue)

        self.label = QLabel(str(self.value))
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
