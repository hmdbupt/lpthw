# Exercise 13 - Practice exercise with more arguments for argv
from sys import argv

# argument variable unpacked into five variables
script, animal_one, animal_two, animal_three, animal_four = argv

print("The script is ", script)
print("The first animal is ", animal_one)
print("The second animal is ", animal_two)
print("The third animal is ", animal_three)
print("The fourth animal is ", animal_four)
