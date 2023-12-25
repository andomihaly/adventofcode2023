from createmap import CreateMap

class DtoParser():
    def parse(self, input):
        if (not input[len(input)-1]==""):
            input.append("")
        createMap =  CreateMap()

        self.seeds=self.parseSeeds(input[0])

        self.maps=[]
        firstIndex=1;
        lastIndex=0;
        for i in range(0, len(input)):
            if (input[i]==""):
                lastIndex=i
            if (lastIndex>firstIndex):
                self.maps.append(createMap.parseMap(input[firstIndex+1:lastIndex]))
                firstIndex=lastIndex


    def getSeeds(self):
        return  self.seeds

    def getMaps(self):
        return self.maps

    def parseSeeds(self, seedText):
        seeds=seedText.split(" ")
        seeds.pop(0)
        return [int(i) for i in seeds]