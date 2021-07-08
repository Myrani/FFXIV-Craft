import pyautogui
import time
import os


class JobProcessor():
    def __init__(self, joblist):
        self.joblist = joblist

    def setupVisualCues(self):
        self.fabricationButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/fabricate.PNG', confidence=0.9))
        self.outfitButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit.PNG', confidence=0.9))
        self.searchBar = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/search.PNG', confidence=0.9))

        print(self.fabricationButton)
        print(self.outfitButton)
        print(self.searchBar)

    def equipOutfit(self, number):

        pyautogui.press("p")
        self.outfitButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit.PNG', confidence=0.9))
        pyautogui.click(pyautogui.center(self.outfitButton))
        self.currentOutfit = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit_' + number+'.PNG', confidence=0.9))
        pyautogui.press("p")

    def searchItem(self, item):
        pyautogui.press("n")
        time.sleep(1)
        self.searchBar = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/search.PNG', confidence=0.9))
        pyautogui.click(self.searchBar)
        pyautogui.write(item)
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/item_found_color.PNG', confidence=0.9)))

    def fabricate(self):
        self.fabricationButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/fabricate.PNG', confidence=0.9))
        pyautogui.click(self.fabricationButton)
        pyautogui.click(self.fabricationButton)
        sleep(3)
        pyautogui.keyDown(self.currentMacro[0])
        sleep(0.1)
        pyautogui.keyDown(self.currentMacro[1])
        sleep(0.1)imeStop
        pyautogui.keyUp(self.currentMacro[0])
        pyautogui.keyUp(self.currentMacro[1])
        sleep(self.currentTimeStop)
        print("Item :", i+1, " Crafted")

    def doJobs(self):
        for job in self.joblist:
            self.currentOufit = job.outfit
            self.currentItem = job.item
            self.currentQuantity = job.quantity
            self.currentMacro = job.macro
            self.currentTimeStop = job.timeStop

            for i in range(0, self.currentQuantity):
                self.fabricate()

    def start(self):
        print("FFXIV Craft Manager : Online")
        # self.setupVisualCues()
        self.searchItem("Test")
