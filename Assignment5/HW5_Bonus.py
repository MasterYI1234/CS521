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
        self.__laptime = None
        self.__save = None

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










#Test file
#Make the class.
check = StopWatch()
print('Elapsed time before start:', check.getElapsedTime())

#Wait 1 sec before start reckon by time, not in reckon by time.
time.sleep(1)

#Start reckon by time.
check.start()
print('Starting now')

#Wait two second.
time.sleep(2)

#Should output little more than 2 sec.
print('lap time after start 2 sec:', check.lap())

time.sleep(3)

#Should output little more than 3 sec.
print('lap time after last lap after 3 sec:', check.lap())

time.sleep(2)

#Output should a little more than 7 second.
print('Elapsed time after start 7 sec:', check.getElapsedTime())

time.sleep(3)

#Stop reckon by time.
check.stop()
print('Stopping now')

#Not in reckon by time.
time.sleep(2)

#Output should a little more than 2 + 3 + 2 + 3 = 10 sec.
print('Elapsed time after sleep 3 sec, then stopping:', check.getElapsedTime())