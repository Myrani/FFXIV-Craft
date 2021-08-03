import pyautogui
import time
import os
import sys
from Content.Back_End.Objects.WorkerSignals import WorkerSignals
from PyQt5.QtCore import QThread,QEventLoop,QTimer

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Content\\Back_End\\") 
        # "."
        # 'Content\\Back_End\\'
    return os.path.join(base_path, relative_path)


class JobProcessor(QThread):
    def __init__(self, joblist, parent=None):
        super(JobProcessor, self).__init__()
        self.joblist = joblist
        self.parent = parent

        print("Parent !", self.parent.parent())
        self.signals = WorkerSignals()

        self.searchBar = None

    def pyqtsleep(self,time):
        loop = QEventLoop()
        QTimer.singleShot(time*1000, loop.exit)
        loop.exec_()
    
    def slowClick(self, lapse):
        pyautogui.mouseDown()
        self.pyqtsleep(lapse)
        pyautogui.mouseUp()

    def doubleClick(self):
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    def changeCurrentJobSpecs(self, job):
        self.currentOufit = job.outfit
        self.currentItem = job.item
        self.currentQuantity = int(job.quantity)
        self.currentMacro = job.macro
        self.currentTimeStop = int(job.timeStop)

    def testVisualCues(self):
        self.fabricationButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\fabricate.PNG'), confidence=0.9)
        self.outfitButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\outfit.PNG'), confidence=0.9)
        self.searchBar = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\search.PNG'), confidence=0.9)

        print(self.fabricationButton)
        print(self.outfitButton)
        print(self.searchBar)


    def notifityCraft(self,i):
            self.signals.changeText.emit(str(self.currentItem) + " Crafted :" +str(i)+"/"+str(self.currentQuantity))

    def AddLabel(self):
        self.signals.addLabel.emit("New job")

    def equipOutfit(self):

        pyautogui.press("p")
        self.pyqtsleep(1)
        self.outfitButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\outfit.PNG'), confidence=0.9)
        pyautogui.click(pyautogui.center(self.outfitButton))
        self.slowClick(0.4)
        self.pyqtsleep(1)
        self.currentOutfitPlace = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\outfit_' + str(self.currentOufit) + '.PNG'), confidence=0.8)
        pyautogui.click(self.currentOutfitPlace)
        self.doubleClick()
        self.pyqtsleep(1)
        pyautogui.press("p")

    def repairOutfit(self):
        pyautogui.press("p")
        self.pyqtsleep(1)
        self.outfitButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\outfit.PNG'), confidence=0.9)
        
        self.pyqtsleep(0.5)
        pyautogui.rightClick(x=self.outfitButton[0]-10,y=self.outfitButton[1]+50)
        self.pyqtsleep(1)
        self.repairButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\repair.PNG'), confidence=0.9)
        pyautogui.moveTo(pyautogui.center(self.repairButton))
        self.slowClick(0.4)
        self.pyqtsleep(1)
        pyautogui.press("p")
        self.pyqtsleep(1)
        self.repairAllButton = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\repair_all.PNG'), confidence=0.8)
        pyautogui.moveTo(pyautogui.center(self.repairAllButton))
        self.slowClick(0.4)
        self.pyqtsleep(1)

    def cleanSearchbar(self):
        pyautogui.press("n")

        pyautogui.click(10, 10)

    def searchItem(self):
        pyautogui.press("n")
        self.pyqtsleep(1)
        if self.searchBar == None:
            self.searchBar = pyautogui.center(
                pyautogui.locateOnScreen(resource_path('Visual_Ressources\\search.PNG'), confidence=0.9))
        pyautogui.click(self.searchBar)
        pyautogui.write(self.currentItem)
        pyautogui.press("enter")
        self.pyqtsleep(2)
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(resource_path('Visual_Ressources\\item_found_color.PNG'), confidence=0.9)))

    def adjustMaterialsQuality(self, job):
        self.pyqtsleep(0.5)
        highQualityLabelPlace = pyautogui.locateOnScreen(resource_path(
            'Visual_Ressources\\HQ.PNG'), confidence=0.9)
        self.pyqtsleep(0.5)
        highQualityItemButtonsList = list(pyautogui.locateAllOnScreen(resource_path(
            'Visual_Ressources\\quality_button.PNG'), confidence=0.9, region=(highQualityLabelPlace[0], highQualityLabelPlace[1], 30, 2000)))

        for key, value in job.highQuality.items():
            for i in range(0, value):
                pyautogui.moveTo(pyautogui.center(
                    highQualityItemButtonsList[key]))
                self.slowClick(0.2)

    def fabricate(self):
        self.fabricationButton = pyautogui.center(
            pyautogui.locateOnScreen(resource_path('Visual_Ressources\\fabricate.PNG'), confidence=0.9))
        pyautogui.click(self.fabricationButton)
        pyautogui.click(self.fabricationButton)
        self.pyqtsleep(3)
        pyautogui.keyDown(self.currentMacro[0])
        self.pyqtsleep(0.1)
        pyautogui.keyDown(self.currentMacro[1])
        self.pyqtsleep(0.1)
        pyautogui.keyUp(self.currentMacro[0])
        pyautogui.keyUp(self.currentMacro[1])
        self.pyqtsleep(self.currentTimeStop)

    def testActivityFeed(self):
        self.AddLabel()
        self.currentItem = "madrier"
        self.currentQuantity = 10
        for i in range(0,11):
            self.notifityCraft(i)
            self.pyqtsleep(0.2)
        self.AddLabel()
        self.currentItem = "lingot"
        self.currentQuantity = 20
        for i in range(0,21):
            self.notifityCraft(i)
            self.pyqtsleep(0.2)
        
    def doJobs(self):
        for job in self.joblist:
            if job.item == "repair":
                print("repair")
                self.repairOutfit()
            else:
                self.AddLabel()
                self.changeCurrentJobSpecs(job)
                self.equipOutfit()
                self.searchItem()
                self.adjustMaterialsQuality(job)
                for i in range(0, self.currentQuantity):
                    self.fabricate()
                    self.notifityCraft(i)
                self.cleanSearchbar()

        print("All jobs done !!!")

    def run(self):
        print("FFXIV Craft Manager : Online")
        self.signals.addLabel.emit("---- Craft Begin ----")
        
        self.pyqtsleep(5)
        
        self.doJobs()




        self.signals.addLabel.emit("---- Craft Ended ----")
