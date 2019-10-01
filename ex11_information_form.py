# the end = ' ' in this line lets you get the input on the same line
print("Enter your first name:", end = ' ')
first_name = input()
print("Enter your last name:", end = ' ')
last_name = input()
print("Enter your age:", end = ' ')
age = input()
print("Enter your email address:", end = ' ')
email = input()

state = "Your name is {} {} \nYour age is {} \nYour email address is {}"
print(state.format(first_name, last_name, age, email))
