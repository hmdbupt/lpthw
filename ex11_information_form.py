first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")

state = "Your name is {} {} \nYour age is {} \nYour email address is {}"
print(state.format(first_name, last_name, age, email))
