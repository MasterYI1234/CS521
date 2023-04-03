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
        
        
        
        
        
#Test file
#Make the class.
 #The output is also millisecond
check = StopWatch()
print('Elapsed time before start:', check.getElapsedTime())

#Wait 1 sec before start reckon by time.
time.sleep(1)

#Start reckon by time.
check.start()
print('Starting now')

#Wait two second.
time.sleep(2)

#Output should a little more than 2 second.
print('Elapsed time after start 2 sec:', check.getElapsedTime())

time.sleep(3)

#Stop reckon by time.
check.stop()
print('Stopping now')

time.sleep(2)

#Output should a little more than 2 + 3 = 5 sec.
print('Elapsed time after sleep 3 sec, then stopping:', check.getElapsedTime())

#Continue reckon by time
check.start()
print('ReStarting now')
print('Elapsed time when start after stop 2 sec:', check.getElapsedTime())

time.sleep(2)

check.stop()
print('Stopping now')
#Out put should a little more than 2 + 3 + 2 = 7 sec.
print('Elapsed time when restart 2 sec then stopping:', check.getElapsedTime())

#Reset reckon by time.
check.reset()
#Output should be 0.
print('Elapsed time after reset:', check.getElapsedTime())





