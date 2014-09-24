import sys
from random import shuffle

# Attempt to open file specified in argument.
try:
    fileName = sys.argv[1]
    f = open(fileName, 'r')
except:
    sys.exit("This program needs a valid argument. Example: randomizer.py classlist.txt")

# Make each line an element of an array, removing line breaks.
names = [line.strip() for line in f.readlines()]

# Shuffle names and output in numbered, random order.
shuffle(names)
for i in range(len(names)):
    print str(i+1) + ": " + names[i]
