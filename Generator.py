from const import INTERVAL
from Drawer import *

class Generator:
    
    def __init__(self, numberOfPoints):
        self.numberOfPoints = numberOfPoints
        self.points = {}

    def __initializePoints(self):
        step = INTERVAL / self.numberOfPoints
        t = 0
        while (t < INTERVAL):
            self.points[t] = self.__generate(t)
            t += step 

    def getPoints(self):
        self.__initializePoints()
        return self.points

    @staticmethod  
    def __generate(t):
        return 0 if (t < 25 or t > 35) else 1
