class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def printCard(self):
        print(self.value, "of", self.suit)