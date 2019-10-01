# importing from sys module argv (argument variable)
from sys import argv
# read the WYSS section for how to run this
# To run this script do the following:
# python ex13.py first second third OR
# python ex13.py Monkey Gorilla Chimpanzee
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
