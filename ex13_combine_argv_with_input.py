# Exercise 13 - Practice exercise that combines input with argv
from sys import argv

script, username = argv

print("The script is ", script)
print("The username is ", username)
password = input("Enter your password: ")
print("Your password is ", password)
