"""
CS521
SiCheng Yi
"""

#Add all states and capital. 
capitals=[["Alabama","Montgomery"],["Alaska","Juneau"],["Arizona","Phoenix"],
["Arkansas","Little Rock"],["California","Sacramento"],["Colorado","Denver"],
["Connecticut","Hartford"],["Delaware","Dover"],["Florida","Tallahassee"],
["Georgia","Atlanta"],["Hawaii","Honolulu"],["Idaho","Boise"],["Illinois","Springfield"],
["Indiana","Indianapolis"],["Iowa","Des Moines"],["Kansas","Topeka"],["Kentucky","Frankfort"],
["Louisiana","Baton Rouge"],["Maine","Augusta"],["Maryland","Annapolis"],["Massachusetts","Boston"],
["Michigan","Lansing"],["Minnesota","St.Paul"],["Mississippi","Jackson"],["Missouri","Jefferson City"],
["Montana","Helena"],["Nebraska","Lincoln"],["Nevada","Carson City"],["New hampshire","Concord"],
["New jersey","Trenton"],["New mexico","Santa Fe"],["New York","Albany"],["North Carolina","Raleigh"],
["North Dakota","Bismarck"],["Ohio","Columbus"],["Oklahoma","Oklahoma City"],["Oregon","Salem"],
["Pennsylvania","Harrisburg"],["Rhode island","Providence"],["South carolina","Columbia"],
["South dakota","Pierre"],["Tennessee","Nashville"],["Texas","Austin"],["Utah","Salt Lake City"],
["Vermont","Montpelier"],["Virginia","Richmond"],["Washington","Olympia"],["West Virginia","Charleston"],
["Wisconsin","Madison"],["Wyoming","Cheyenne"]]

#Set the count of the correct answer
correct=0
for i in range(len(capitals)):   
    cap=input("What is the capital of "+capitals[i][0]+"? ")
    #If the answer is the same with the capitals, correct+=1.
    if cap.lower() == capitals[i][1].lower():
        correct+=1
        print("Your answer is correct")
    else:
        #If not the same, output the correct answer.
        print("The correct answer should be",capitals[i][1])

#Output the count of correct.
print("The correct count is",correct)