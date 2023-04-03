"""
CS521
SiCheng Yi
Project
"""
from health import health
from stopwatch import StopWatch
import time 


#food = [["apple",95],["chocolate",155],["milk",103],["bread",79],["coke",182]]
food = {"Apple":95,"Chocolate":155,"Milk":103,"Bread":79,"Coke":182}
sport = ("Run","Weightlifting")

def EAT():
    eat=input("Please Enter the food: ")
    cal = food.get(eat)
    print("This food have "+str(cal)+" calorie.")
    return cal
#    for i in range(len(food)):
#        if eat.lower() == food[i][0].lower():
#            cal = food[i][1]
#            print("This food have "+str(cal)+" calorie.")
#            return cal
        
#    print("Don't have this food.")
  
        







def main():
    ac = health()
    while(True):
        
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print("Main menu")
        print("1: Enter the food you eat\n2: check my calorie and sports\n3: sports now\n4: sports report\n5: exit")
        choice = int(input(""))
        if choice == 1:
            cal = EAT()
            ac.addcalorie(cal)
        
        if choice == 2:
            cal = ac.getcalorie()
            times = ac.getsportsTime()
            print("Your calorie is "+str(cal)+" and your sports time is "+str(times)+" .")
            
        
        if choice == 3:
            print("We have "+str(sport))
            spo = input("Which sport you do?")
            
            check = StopWatch()
            check.start()
            while(True):
                print("Enter 0 to end the sprots!")
                run = eval(input(""))
                if run == 0:
                    break
                else:
                    print("Do It!")
            check.stop()
            sporttime = check.getElapsedTime() / 1000
            print("You have sports "+str(sporttime)+" secounds.")
            ac.addsportsTime(sporttime)
        
        if choice == 4:
            filename = "Report.txt"
            file = open(filename, 'w')
            file.write("111")
         

         
        if choice == 5:
            break
         




main()


