import pyautogui
import time
import os


class JobProcessor():
    def __init__(self, joblist):
        self.joblist = joblist

    def setupVisualCues(self):
        print(os.getcwd())
        self.fabricationButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/fabricate.PNG'))
        self.oufitButton = pyautogui.center(
            pyautogui.locateOnScreen('Content/Back_End/Visual_Ressources/outfit.PNG'))

    def equipOutfit(self):
        pass

    def searchItem(self):
        pass

    def fabricate(self):

        pass

    def doJobs(self):
        for job in self.joblist:
            self.currentOufit = job.outfit
            self.currentItem = job.item
            self.currentQuantity = job.quantity
            self.currentTimeStop = job.timeStop

            for i in range(0, self.currentQuantity):

                time.sleep(self.currentTimeStop)

    def start(self):
        print("Craft Manager Online")
        self.setupVisualCues()
        # self.doJobs()
