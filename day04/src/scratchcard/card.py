class Card():
    def __init__(self):
        self.name = "card"
        self.id = 0
        self.numbers = []
        self.winningNumbers = []

    def score(self):
        hitNumbers=list(set(self.numbers) & set(self.winningNumbers))
        if (len(hitNumbers)==0):
            return 0
        return pow(2,len(hitNumbers)-1)
    def getNumberOfHit(self):
         return  len(list(set(self.numbers) & set(self.winningNumbers)))