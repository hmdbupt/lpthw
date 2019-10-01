# types of people
types_of_people = 10
# f here means format. It is used to put the variable types_of_people inside
# string. x saves the string message.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# y saves the string with formatted variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# prints x and y on the screen
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# saves the string with a placeholder for variable
joke_evaluation = "Isn't that joke so funny?! {}"

# passing hilarious as a variable to the format function of variable
# joke_evaluation. This will put the value of hilarious inside the string
# when the program runs
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = " a string with a right side."

# combines w and e and prints them on screen
print(w + e)
