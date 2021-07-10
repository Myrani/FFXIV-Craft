import pyautogui
import time
import os


class JobProcessor():
    def __init__(self, joblist):
        self.joblist = joblist
        self.searchBar = None
    
    def slowClick(self,lapse):
        pyautogui.mouseDown()
        time.sleep(lapse)
        pyautogui.mouseUp()  
    
    def doubleClick(self):
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    def changeCurrentJobSpecs(self,job):
        self.currentOufit = job.outfit
        self.currentItem = job.item
        self.currentQuantity = int(job.quantity)
        self.currentMacro = job.macro
        self.currentTimeStop = int(job.timeStop)

    def testVisualCues(self):
        self.fabricationButton = pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/fabricate.PNG', confidence=0.9)
        self.outfitButton = pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit.PNG', confidence=0.9)
        self.searchBar = pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/search.PNG', confidence=0.9)

        print(self.fabricationButton)
        print(self.outfitButton)
        print(self.searchBar)

    def equipOutfit(self):

        pyautogui.press("p")
        time.sleep(1)
        self.outfitButton = pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit.PNG', confidence=0.9)
        pyautogui.click(pyautogui.center(self.outfitButton))
        self.slowClick(0.4)    
        time.sleep(1)
        self.currentOutfitPlace = pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit_' + self.currentOufit +'.PNG', confidence=0.8)
        pyautogui.click(self.currentOutfitPlace)
        self.doubleClick()
        time.sleep(1)
        pyautogui.press("p")
    
    def cleanSearchbar(self):
        pyautogui.press("n")
        
        pyautogui.click(10,10)
    def searchItem(self):
        pyautogui.press("n")
        time.sleep(1)
        if self.searchBar == None:
            self.searchBar = pyautogui.center(
                pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/search.PNG', confidence=0.9))
        pyautogui.click(self.searchBar)
        pyautogui.write(self.currentItem)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/item_found_color.PNG', confidence=0.9)))

    def fabricate(self):
        self.fabricationButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/fabricate.PNG', confidence=0.9))
        pyautogui.click(self.fabricationButton)
        pyautogui.click(self.fabricationButton)
        time.sleep(3)
        pyautogui.keyDown(self.currentMacro[0])
        time.sleep(0.1)
        pyautogui.keyDown(self.currentMacro[1])
        time.sleep(0.1)
        pyautogui.keyUp(self.currentMacro[0])
        pyautogui.keyUp(self.currentMacro[1])
        time.sleep(self.currentTimeStop)
        print("Item :", " Crafted")

    def doJobs(self):
        for job in self.joblist:
            self.changeCurrentJobSpecs(job)
            self.equipOutfit()
            self.searchItem()
            for i in range(0, self.currentQuantity):
                self.fabricate()
            self.cleanSearchbar()
        
        print("All jobs done !!!")

    def start(self):
        print("FFXIV Craft Manager : Online")
        time.sleep(5)
        self.testVisualCues()
        # self.setupVisualCues()
        
        self.doJobs()

        
        
