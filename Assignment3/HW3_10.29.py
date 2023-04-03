"""
cs521
10.29
"""

import random

#Set the list of wards
words = ["write", "that", "program", "like"]

#Set the playagain enter is 'y',I just set if not 'y' then it is not play again. Set wrong time from 0 to start.
playAgain = 'y'
wrong = 0

#Take a word from the list.
#Then make the loop for ask player to guess, if guess write, show the letter in the word and output.
#If guess wrong wrong time++ and output.
while playAgain == 'y':
    w = words[random.randint(0,3)]
    w = list(w)
    res = ['*'] * len(w)
    print("(Guess) Enter a letter in word", ''.join(res), end=' ')
    f = 0
    while True:
        guess = input()
        if guess not in res:
            if guess in w:
                for i in w:
                    if i == guess:
                        res[w.index(i)] = guess
                        w[w.index(i)] = '_'
                        if res.count('*') == 0:
                            f = 1
                            break
                if f == 1:
                    break
            else:
                wrong += 1
                print("\t", guess, "is not in the word")
        else:
            print("\t", guess, "is already in the word")
        print("(Guess) Enter a letter in word", ''.join(res), end=' ')

    print("The word is", ''.join(res) + ". You missed", wrong,"time")
    print()
    
    #Reset the wrong time and ask for do you want to play again.
    wrong = 0
    playAgain = input("Do you want to guess another word? Enter y or n").lower()