# Exercise 15 - Reading files
from sys import argv

# Getting filename using argv
script, filename = argv

# Opens file in read mode (read is the default mode) and save it into txt
txt = open(filename)

# prints the name of the file
print(f"Here's your file {filename}:")
# prints the contents of the file
# .read() function reads the contents of the file
print(txt.read())
# Closes the file. It is important to close the file when the job is done.
# This will consume less memory.
txt.close()

# Getting filename using input
print("Type the filename again:")
file_again = input("> ")

# opens file and saves it into txt_again
txt_again = open(file_again)

# reads the file contents and prints it on the screen
print(txt_again.read())
# Closes the file. It is important to close the file when the job is done.
# This will consume less memory.
txt_again.close()
