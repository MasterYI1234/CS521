"""
CS521
SiCheng Yi
project
class2
"""
import time 

class StopWatch:
    #initial state
    def __init__(self):
        self.__state = False
        self.__startTime = None
        self.__endTime = None
        self.__laptime = None
        self.__save = None
        
    def __str__(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def start(self):
        #When at initial state
        if self.__state == False and self.__startTime == None:
          self.__state = True
          self.__startTime = time.time()
        #When at stop state
        if self.__state == False and self.__startTime != None:
           self.__state = True
           self.__startTime = (time.time() - self.__endTime) + self.__startTime
    #When at running state
    def stop(self):
        if self.__state == True:
            self.__state = False
            self.__endTime = time.time()
    
    #Reset to initial state
    def reset(self):
        if self.__state == False and self.__startTime != None:
            self.__state = False
            self.__startTime = None
            self.__endTime = None
            self.__laptime = None
            self.__save = None
    #The lap for time, The output is also millisecond.
    def lap(self):
        #If is the first time for lap.
        if self.__laptime == None and self.__startTime != None:
            self.__save = time.time()
            l = int(self.__save - self.__startTime)
            self.__laptime = self.__save
            return l * 1000
        #If not first time for lap.
        if self.__laptime != None and self.__startTime != None:
           self.__save = time.time()
           l = int(self.__save - self.__laptime)
           self.__laptime = self.__save
           return l * 1000

    #The output is also millisecond
    def getElapsedTime(self):
        #When at initial state
        if self.__state == False and self.__startTime == None:
            return 0
        #When at running state
        if self.__state == True:
            return int(1000 * (time.time() - self.__startTime))
        #When at stop state
        if self.__state == False and self.__startTime != None:
            return int(1000 * (self.__endTime - self.__startTime))









