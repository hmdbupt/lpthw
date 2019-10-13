# Exercise 19 - Functions and variables

# a function that takes in the amount of cheese and crackers and prints them
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# calling the function by passing arguments of the amount of cheese and crackers
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# passing cheese and crackers by means of variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# performing arithmatic operation in arguments
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
# arithmatic operation on variables in arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
