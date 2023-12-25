import re
from loggercontext import LoggerContext

class BoatRacesParser():
    logger = LoggerContext()
    def parse(self, input):
        times=re.findall(r'\d+',input[0])
        self.logger.debug(str(times))
        distances=re.findall(r'\d+',input[1])
        self.logger.debug(str(distances))
        races=[]
        for i in range(0,len(times)):
            races.append([int(times[i]),int(distances[i])])
        return races