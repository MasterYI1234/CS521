"""
CS521
SiCheng Yi
Project
main function
"""

#import two class
from health import health
from stopwatch import StopWatch


#Use the dictionary to set food, the key is food and the value is the calorie of the food.
#Use tuple to set sport.
#If want to add food and sport, just write in to the dictionary and tuple.
food = {"apple":95,"chocolate":155,"milk":103,"bread":79,"coke":182}
sport = ("run","weightlifting")




#An user-defined function to get the food from user and return the calcorie of the food.
def EAT():
    eat=input("Please Enter the food: ")
    cal = food.get(eat)
    print("This food have "+str(cal)+" calorie.\n")
    return cal

  
        



def main():
    ac = health()
    #A while loop to make it is always work without choose exit.
    while(True):
        check = StopWatch()
        #Use the __str()__ to output the time of now.
        print(check)
        print("Main menu")
        print("1: Enter the food you eat\n2: check my calorie and sports\n3: sports now\n4: sports report\n5: exit")
        choice = int(input(""))
        #Use if and else block to make the menu.
        
        #Get the food and add the calcorie.
        if choice == 1:
            cal = EAT()
            ac.addcalorie(cal)
            ac.chcalorie.append(ac.getcalorie())
        
        #Output the calcorie and sports time now.
        elif choice == 2:
            cal = ac.getcalorie()
            times = ac.getsportsTime()
            print("Your calorie is "+str(cal)+" and your sports time is "+str(times)+" .\n")
            
        #Make a sport.
        elif choice == 3:
            print("We have "+str(sport))
            spo = input("Which sport you do?\n")
            if spo in sport:
                ac.dosport.add(spo)
                check.start()
                record = 0
                while(True):
                    print("Enter 0 to end the sprots!")
                    run = eval(input(""))
                    if run == 0:
                        break
                    else:
                        print("Do It!")
                        record += 1
                check.stop()
                
                #Change the time to second.
                sporttime = check.getElapsedTime() / 1000
                print("You have sports "+str(sporttime)+" secounds.")
                ac.addsportsTime(sporttime)
                cal = record * 1
                print("You have reduce "+str(cal)+" calorie.\n")
                ac.spocalorie(cal)
                ac.chcalorie.append(ac.getcalorie())

            #Print the else information.
            else:
                print("Error! Please enter the sport we have.\n")
        
        elif choice == 4:
            #Make a file to do the report.
            filename = "Report.txt"
            #Write in the file.
            file = open(filename, 'w')
            file.write("You have "+str(ac.getcalorie())+" calorie.\n")
            file.write("You do "+str(ac.getsportsTime())+" seconds sports.\n")
            file.write("You do "+str(ac.__len__())+" kind of different sports.\n")
            file.write("It is: ")
            file.write(str(ac.getsport())+"\n")
            file.write("You calories change is: \n")
            #Use the for loop to output calcorie change list element one by one.
            x = 0
            a = ac.chcalorie
            for x in range(len(ac.chcalorie)):
                file.write("                                   "+str(a[x])+"\n")
         

        #Exit. 
        elif choice == 5:
            break
        
        else:
            print("Please enter the right choose!\n")
         




main()


