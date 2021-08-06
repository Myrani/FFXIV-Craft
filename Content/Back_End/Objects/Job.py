import pickle
import sys
import os

class Job():
    def __init__(self, outfit, item, quantity, macro, timestop, lowQuality, highQuality):
        self.outfit = outfit
        self.item = item
        self.quantity = quantity
        self.macro = macro
        self.timeStop = timestop
        self.recurrent = False
        self.lowQuality = lowQuality
        self.highQuality = highQuality

    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".") 
            #"."
            #"Content\\Back_End\\"
        return os.path.join(base_path, relative_path)



    def setOutfit(self, content):
        self.outfit = content
    def getOutfit(self):
        return self.outfit

    def setItem(self, content):
        self.item = content
    def getItem(self):
        return self.item

    def setQuantity(self, content):
        self.quantity = content
    def getQuantity(self):
        return self.quantity
    
    def setMacro(self, content, indent):
        self.macro[indent] = content
    def getMacro(self,index):
        return self.macro[index]


    def setTimeStop(self, content):
        print(content)
        self.timeStop = content
    def getTimeStop(self):
        return self.timeStop
    
    def setLowQuality(self, index, content):
        self.lowQuality[index] = int(content)
        print(self.lowQuality)

    def setHighQuality(self, index, content):
        self.highQuality[index] = int(content)
        print(self.highQuality)

    def swapRecurrent(self):
        self.recurrent = not self.recurrent
        print(self.recurrent)

    def selfSave(self):
        
        self.file = self.resource_path("Recurrent_Jobs\\"+str(self.outfit)+self.item+str(self.quantity))+".pkl"
        
        with open(self.resource_path("Recurrent_Jobs\\"+str(self.outfit)+self.item+str(self.quantity)+".pkl"), 'wb') as file:
            pickle.dump(self, file)

        return None
