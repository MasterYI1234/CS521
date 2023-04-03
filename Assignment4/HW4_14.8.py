"""
CS521
SiCheng Yi
"""
#Ask for a input txt file name and open it
f = open(input("Enter the name of the text file(.txt): "))
#Check all words. put it in the line.
lines = f.readlines()
lines = [line.lower() for line in lines]

#Check the words by space and list it
words = set()
for line in lines:
    for word in line.split():
        words.add(word)
words = list(words)
#Sort the word
words.sort()

#Print the words
i = 0
for x in words:
    print(x, end=' ')
    i += 1
    if i == 10:
        print()
        i = 0

#Clost the file.
f.close()