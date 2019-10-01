# Exercise 13 - Parameters, unpacking, variables
# importing from sys module argv (argument variable)
# The argv is used to take input from the user while opening/running the script
# It is similar to input() but input takes the input from user during
# the execution of the program
from sys import argv
# To run this script do the following:
# python ex13.py first second third OR
# python ex13.py Monkey Gorilla Chimpanzee
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
