from sys import argv

script, input_file = argv

# this function prints the whole file
def print_all(f):
    print(f.read())

# this function takes the reading cursor back to the start
def rewind(f):
    # the seek(0) deals in bytes. It takes the reading head to the 0 byte
    # that is, the beginning of the file
    f.seek(0)

# this function prints only one line
def print_a_line(line_count, f):
    # inside readline() is code that scans each byte of file until it finds \n
    # character, then stops reading the file to return what it found. The file
    # f is responsible for maintaining the current position in the file after
    # each readline() call, so that it will keep reading each line.

    # the readline() function returns the \n that is at the end of that line.
    # Add a end = "" at the end of print function calls to avoid adding double
    # \n to every line.
    print(line_count, f.readline(), end = "")

# opens the file and puts it in current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

# calling function to print the whole file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# calling function to bring back the cursor back to the start
rewind(current_file)

print("Let's print three lines:")

current_line = 1
# calling function to print only one line
# since the cursor is in start position the function will only print the first line
print_a_line(current_line, current_file)

# here current_line += 1 means current_line = current_line + 1
current_line += 1
# printing second line
print_a_line(current_line, current_file)

current_line += 1
# printing third line
print_a_line(current_line, current_file)
