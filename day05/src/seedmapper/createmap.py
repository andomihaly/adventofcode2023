from loggercontext import LoggerContext

class CreateMap():
    logger = LoggerContext()
    def parseMap(self, input):
        result= dict()
        result["name"]=input[0][0:len(input[0])-1]
        input.pop(0)
        result["map"]=self.parseMapContent(input)
        return result

    def parseMapContent(self, input):
        map=[]
        for line in input:
            numbers=line.split(" ")
            mapPart=[int(numbers[1]),int(numbers[0]),int(numbers[2])]
            map.append(mapPart)
        map.sort(key=lambda x: x[0])
        return map