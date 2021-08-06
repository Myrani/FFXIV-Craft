from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QCheckBox, QWidget, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import QThreadPool, QSize, QCoreApplication, Qt, pyqtSlot

from Content.Front_End.Widgets.JobLabel import JobLabelWithRemove
from Content.Front_End.Widgets.AddJobButton import AddJobButton, AddJobFromRecurrentButton, StartJobsButton,AddRepairButton
from Content.Front_End.Widgets.MenuButton import MenuButton
from Content.Front_End.Widgets.SystemBar import SystemBar
from Content.Back_End.Objects.JobProcessor import JobProcessor


class SettingsWindow(QWidget):
    def __init__(self,parent=None):
        super(SettingsWindow,self).__init__(parent=parent)
        self.systemBar = SystemBar(self)
        self.systemBar.settingsButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);color :black ;")

        self.settingsMenu = QGroupBox(self)
        self.settingsMenuLayout = QGridLayout()
        self.settingsMenu.setLayout(self.settingsMenuLayout)
        self.settingsMenu.setGeometry(10, 40, 1260, 660)
        self.settingsMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")

        self.initUIContent()
        self.show()
    
    def initUIContent(self):

        self.languageLabel = QLabel("Your FFXIV game language")
        self.languageLabel.setStyleSheet("color:white;")
        
        self.FRCheckBox = QCheckBox("French")
        self.FRCheckBox.stateChanged.connect(lambda :self.changeLanguage("FR",self.FRCheckBox))
        self.FRCheckBox.setStyleSheet("color:white;")
        
        self.ENCheckBox = QCheckBox("English")
        self.ENCheckBox.stateChanged.connect(lambda: self.changeLanguage("EN",self.ENCheckBox))
        self.ENCheckBox.setStyleSheet("color:white;")

        self.settingsMenuLayout.addWidget(self.languageLabel,0,0,1,1)
        self.settingsMenuLayout.addWidget(self.FRCheckBox,1,0,1,1)
        self.settingsMenuLayout.addWidget(self.ENCheckBox,1,1,1,1)
        
        self.fillerLabel = QLabel()
        self.settingsMenuLayout.addWidget(self.fillerLabel,2,0,4,4)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startQueueWindow())
        self.settingsMenuLayout.addWidget(self.backButton,6,6,1,1)

        self.languageCheckBoxList = {self.FRCheckBox,self.ENCheckBox}
        self.languageCheckBoxDict = {"FR":self.FRCheckBox,"EN":self.ENCheckBox}

        self.setUpCurrentLanguage()

    def setUpCurrentLanguage(self):
        self.languageCheckBoxDict[self.nativeParentWidget().parametters["language"]].setChecked(True)

    def changeLanguage(self,language,currentCheckbox):

        if currentCheckbox.isChecked(): 
            self.nativeParentWidget().parametters["language"] = language
            for QCheckBox in self.languageCheckBoxList - {currentCheckbox}:
                QCheckBox.setChecked(False)
