from loggercontext import LoggerContext

class Parser():
    logger = LoggerContext()

    def parse(self, input):
        network={}
        for i in range(2,len(input)):
            #BPQ = (VXR, TLN)
            key, value = input[i].split(" = (")
            left, right = value.split(", ")
            right=right.replace(")","")
            network[key]=[left,right]
        self.logger.debug(str(network))
        return network
    def parsePath(self, input):
        self.logger.debug(str(input[0]))
        return tuple(input[0])
