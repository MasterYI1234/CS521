"""
CS521
SiCheng Yi
"""

#Add all states and capital in dictionary. 
dictionary = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusettes": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New York": "Albany",
        "New Mexico": "Santa Fe",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismark",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennslyvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"}

#Set the count of the correct answer
correct = 0
#Set the the state we make as keys of dictionary, so we just use this key to find the answer of capitals
states = dictionary.keys()

for state in states:
    capital = input("What is the capital of " + state + "? ")
    #If the answer is the same with the capitals, correct+=1.
    if capital.lower() == dictionary[state].lower():
        print("Your answer is correct")
        correct += 1
    else:
        #If not the same, output the correct answer.
        print("The correct answer should be " + dictionary[state])
#Output the count of correct.
print("The correct count is " + str(correct))


