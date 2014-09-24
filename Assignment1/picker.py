import sys
from random import choice

# Attempt to open file specified in argument.
try:
    fileName = sys.argv[1]
    f = open(fileName, 'r')
except:
    sys.exit("This program needs a valid argument. Example: randomizer.py classlist.txt")

# Make each line an element of an array, removing line breaks.
names = [line.strip() for line in f.readlines()]

# Pick a name to output.
try:
    print choice(names)
except IndexError:
    print "Your list is empty."
