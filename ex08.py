# a variable that saves string with four placeholders {} for future use
# variables can be put inside {}
formatter = "{} {} {} {}"

# .format function sends the values to the string
# here 1, 2, 3, and 4 are send to formatter string
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))

# this will just print the content of formatter four times
print(formatter.format(formatter, formatter, formatter, formatter))

# it looks complicated but actually it isn't. I am just passing the
# clauses (parts of sentences) into each {} in the variable formatter
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
