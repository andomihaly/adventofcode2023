import functools


class Calculator():

    def calculate(self, cards):
        ordered = sorted(cards, key=functools.cmp_to_key(self.compare), reverse=True)
        sum = 0;
        for i in range(0, len(ordered)):
            sum += (ordered[i].bet * (i + 1))

        return sum

    def compare(self, x1, x2):
        if (x1.rank.value > x2.rank.value):
            return 1
        if (x1.rank.value < x2.rank.value):
            return -1
        for i in range(0, 5):
            if (x1.cardConverter[x1.cards[i]] > x2.cardConverter[x2.cards[i]]):
                return 1
            if (x1.cardConverter[x1.cards[i]] < x2.cardConverter[x2.cards[i]]):
                return -1
        return 0
