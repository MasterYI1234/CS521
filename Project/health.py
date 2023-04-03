"""
CS521
SiCheng Yi
Project
class1
"""


class health:
    #initial state
    dosport = set()
    chcalorie = [0]
    
    def __init__(self):
        self.__calorie = 0
        self.__sportsTime = 0

        
    
    #A magic class method to get the long of dosport set.
    def __len__(self):
        return len(self.dosport)
    
    #Get the final calorie
    def getcalorie(self):
        return self.__calorie
    
    #Get the sports time
    def getsportsTime(self):
        return self.__sportsTime
    
    #Put the sports in set
    def getsport(self):
        return health.dosport
    
    #Put the chcalorie change in list
    def getchalorie(self):
        return health.chcalorie
    
    
    #Change the final calorie
    def addcalorie(self,cal):
        self.__calorie += cal
        return self.__calorie
    
    #Change the final chalorie
    def spocalorie(self,cal):
        self.__calorie -= cal
        return self.__calorie
    
    
    #Change the final sports time
    def addsportsTime(self,times):
        self.__sportsTime += times
        return self.__sportsTime

