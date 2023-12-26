import functools


class Calculator():

    def calculate(self, cards):
        ordered = sorted(cards, key=functools.cmp_to_key(self.compare), reverse=True)
        sum = 0;
        for i in range(0, len(ordered)):
            sum += (ordered[i].bet * (i + 1))

        return sum

    def compare(self, x1, x2):
        cardConverter = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11,
                         "3": 12, "2": 13}
        if (x1.rank.value > x2.rank.value):
            return 1
        if (x1.rank.value < x2.rank.value):
            return -1
        for i in range(0, 5):
            if (cardConverter[x1.cards[i]] > cardConverter[x2.cards[i]]):
                return 1
            if (cardConverter[x1.cards[i]] < cardConverter[x2.cards[i]]):
                return -1
        return 0
