from enum import Enum


class CamelCardRank(Enum):
    FiveOfAKind = 1
    FourOfAKind = 2
    FullHouse = 3
    ThreeOfAKind = 4
    TwoPair = 5
    OnePair = 6
    HighCard = 7


class CamelCard:
    cardConverter = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11,
                     "3": 12, "2": 13}

    def __init__(self, cards, bet):
        self.cards = tuple(cards)
        self.bet = int(bet)
        self.generateMap()
        self.calculateRank()

    def calculateRank(self):
        self.rank = CamelCardRank.HighCard
        if (self.numberOfSameCards[0] == 5):
            self.rank = CamelCardRank.FiveOfAKind
        elif (self.numberOfSameCards[0] == 4):
            self.rank = CamelCardRank.FourOfAKind
        elif (self.numberOfSameCards[0] == 3 and self.numberOfSameCards[1] == 2):
            self.rank = CamelCardRank.FullHouse
        elif (self.numberOfSameCards[0] == 3 and self.numberOfSameCards[1] == 1):
            self.rank = CamelCardRank.ThreeOfAKind
        elif (self.numberOfSameCards[0] == 2 and self.numberOfSameCards[1] == 2):
            self.rank = CamelCardRank.TwoPair
        elif (self.numberOfSameCards[0] == 2 and self.numberOfSameCards[1] == 1):
            self.rank = CamelCardRank.OnePair

    def generateMap(self):
        self.createOrderedCardList(self.createLetterDict())

    def createLetterDict(self):
        map = {}
        for letter in self.cards:
            map[letter] = 0
        for letter in self.cards:
            map[letter] += 1
        return map

    def createOrderedCardList(self, map):
        self.numberOfSameCards = []
        for item in map:
            self.numberOfSameCards.append(map[item])
        self.numberOfSameCards = sorted(self.numberOfSameCards, reverse=True)


class CamelCardWithJoker(CamelCard):
    cardConverter = {"A": 1, "K": 2, "Q": 3, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11,
                     "3": 12, "2": 13, "J": 14}

    def generateMap(self):
        map = self.createLetterDict()
        # count joker and remove from the cards
        joker = 0;
        if "J" in map:
            joker = map["J"]
            del map["J"]

        self.createOrderedCardList(map)

        # add joker in the best place
        if (joker > 0):
            if (joker==5):
                self.numberOfSameCards.append(5)
            elif (self.numberOfSameCards[0] > 3):
                self.numberOfSameCards[0] = 5
            else:
                self.numberOfSameCards[0] += joker
