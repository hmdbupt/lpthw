# Exercise 16 - Study drill - Remove unnecessary repetitions from the file

from sys import argv

# takes arguments from power shell and saves it in the variables
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# deletes everything from the file
# we don't have to use truncate if the file is opened by using the 'w' write mode
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1} \n {line2} \n {line3} \n")

print("And finally, we close it.")
target.close()
