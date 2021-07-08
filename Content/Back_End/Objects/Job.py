import pickle
import os


class Job():
    def __init__(self, outfit, item, quantity, macro, timestop):
        self.outfit = outfit
        self.item = item
        self.quantity = quantity
        self.macro = macro
        self.timeStop = timestop
        self.recurrent = False

    def setOutfit(self, content):
        self.outfit = content

    def setItem(self, content):
        self.item = content

    def setQuantity(self, content):
        self.quantity = content

    def setMacro(self, content, indent):
        self.macro[indent] = content
        print(self.macro[indent])

    def setTimeStop(self, content):
        self.timeStop = content

    def swapRecurrent(self):
        self.recurrent = not self.recurrent
        print(self.recurrent)

    def selfSave(self):
        print(os.getcwd())
        with open('Content/Back_End/Recurrent_Jobs/'+str(self.outfit)+self.item+str(self.quantity)+'.pkl', 'wb') as file:
            pickle.dump(self, file)

        return None
