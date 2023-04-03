"""
CS521
SiCheng Yi
"""
from stopwatch import StopWatch
import time

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


#Use assert to check it.
assert 10000 <= check.getElapsedTime() <= 11000," Out put is no true."
