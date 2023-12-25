class CalculateNextSeed():
    def calc(self, map, seed):
        for row in map["map"]:
            if (seed>=row[0] and seed<row[0]+row[2]):
                return seed+row[1]-row[0]
        return seed