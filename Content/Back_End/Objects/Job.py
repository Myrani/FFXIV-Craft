class Job():
    def __init__(self, outfit, item, quantity, macro):
        self.outfit = outfit
        self.item = item
        self.quantity = quantity
        self.macro = macro

    def setOutfit(self, content):
        self.outfit = content

    def setItem(self, content):
        self.item = content

    def setQuantity(self, content):
        self.item = content

    def setMacro(self, content, indent):
        self.macro[indent] = content
        print(self.macro[indent])
