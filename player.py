class Player:
    def __init__(self, name, money, hand, position):
        self.name = name
        self.money = money
        self.hand = hand
        self.position = position
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setMoney(self, money):
        self.money = money
        
    def getMoney(self):
        return self.money
    
    def setHand(self, hand):
        self.hand = hand
    
    def getHand(self, hand):
        return self.hand
    
    def setPosition(self, position):
        return self.position