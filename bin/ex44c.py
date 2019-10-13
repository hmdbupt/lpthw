# Exercise 44c - alter before or after running the parent features

# parent class with altered method
class Parent(object):

    def altered(self):
        print("PARENT altered()")

# child class with altered method
class Child(Parent):

    def altered(self):
        # first this statement will run
        print("CHILD, BEFORE PARENT altered()")
        # then super will call the altered method in
        # the parent class and run it. This will print
        # the message "PARENT altered()"
        # Read this as "call super with arguments Child and
        # self, then call the function altered on whatever
        # it returns."
        super(Child, self).altered()
        # finally this statement will run
        print("CHILD, AFTER PARENT altered()")

# creating a dad instance of Parent class
dad = Parent()
# creating a son instance of Child class
son = Child()


dad.altered()
son.altered()
