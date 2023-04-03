"""
CS521
SiCheng Yi
"""

import time


class StopWatch:
    #The private data fields startTime and endTime with get methods.
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = time.time()
        
    #A method named start() that resets the startTime to the current time.
    def start(self):
        self.__startTime = time.time()
        
    # A method named stop() that sets the endTime to the current time.
    def stop(self):
        self.__endTime = time.time()
        
    #A method named getElapsedTime() that returns the elapsed time for the stop watch in milliseconds.
    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))
