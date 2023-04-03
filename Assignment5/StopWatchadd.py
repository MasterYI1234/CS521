"""
CS521
SiCheng Yi
"""
import time 

class StopWatch:
    #initial state
    def __init__(self):
        self.__state = False
        self.__startTime = None
        self.__endTime = None

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