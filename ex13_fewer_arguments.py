# Exercise 13 - Practice exercise with fewer arguments for argv
from sys import argv

# argument variable unpacked into three variables
script, fruit_one, fruit_two = argv

print("The script is ", script)
print("The first fruit is ", fruit_one)
print("The second fruit is ", fruit_two)
