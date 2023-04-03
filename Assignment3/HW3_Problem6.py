"""
cs521
Problem6
"""

# Open the txt file, put the file in a value
f = open('sample_input_charles_dickens.txt','r')

#Set a output file named output.txt
filename = "output.txt"

lines = f.read()
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#Caculate the total letter in the txt file
a = 0
for c in lines:
    if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHJIJKLMNOPQRSTUVWXYZ':
        a += 1
#Ignore cases and non-alphabetic characters
lines = lines.upper()
lines = ''.join([i for i in lines if not i.isdigit()])

#Open the output file and write in it
file = open(filename, 'w')

#Check the letter number and output int to the file
l = len(lines)

file.write('Char\tFreq\t%total'+'\n')

for i in alphabets:
    c = lines.count(i)
    file.write('%s\t%s\t%s' %(i,c,round(c/a*100,2))+'\n')