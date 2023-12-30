class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value
    
    def setSuit(self, suit):
        self.suit = suit
    
    def getSuit(self):
        return self.suit
    
    def printCard(self):
        print(self.value, "of", self.suit)