"""
CS521
SiCheng Yi
Project
class1
"""

from health import health

a = health()


#Check the initial value
print(a.getcalorie())
print(a.getsportsTime())
print(a.__len__())
print(a.getchalorie())


print("Add the value.")


#Change the value
a.chcalorie.append(1)
a.dosport.add("run")

a.addcalorie(12)
a.addsportsTime(33)


print(a.getcalorie())
print(a.getsportsTime())
print(a.__len__())
print(a.getchalorie())
print(a.getsport())


#Use assert to chack it
assert a.getcalorie() == 12," Out put is no true."
assert a.getsportsTime() == 33," Out put is no true."
assert a.__len__() == 1," Out put is no true."
assert a.getchalorie() == [0,1]," Out put is no true."
assert a.getsport() == {'run'}," Out put is no true."



print("Minus calorie")

a.spocalorie(4)


print(a.getcalorie())
assert a.getcalorie() == 8," Out put is no true."
