# Exercise 11 - Asking questions
# end = ' ' is used at the end of each print line to tell print not to
# end the line witha a newline character and go to the next line.
print("How old are you?", end = ' ')

# input() is used to take input from user
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you are {age} old, {height} tall, and {weight} heavy.")
