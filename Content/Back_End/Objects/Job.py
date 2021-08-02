import pickle


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

    def setOutfit(self, content):
        self.outfit = content

    def setItem(self, content):
        self.item = content

    def setQuantity(self, content):
        self.quantity = content

    def setMacro(self, content, indent):
        self.macro[indent] = content

    def setTimeStop(self, content):
        print(content)
        self.timeStop = content

    def setLowQuality(self, index, content):
        self.lowQuality[index] = int(content)
        print(self.lowQuality)

    def setHighQuality(self, index, content):
        self.highQuality[index] = int(content)
        print(self.highQuality)

    def swapRecurrent(self):
        self.recurrent = not self.recurrent

    def selfSave(self):

        with open('Content/Back_End/Recurrent_Jobs/'+str(self.outfit)+self.item+str(self.quantity)+'.pkl', 'wb') as file:
            pickle.dump(self, file)

        return None
