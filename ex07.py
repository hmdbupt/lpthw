# Exercise 7 - More printing
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")

# prints . ten times
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try to remove it to see what happens
# when I remove end = ' ' from the code the program just prints Cheese
# on one line and Burger on the next. But with the end = ' ' the Cheese Burger
# is written on the same line with a space between the two words.
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
