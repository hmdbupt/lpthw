# Exercise 44a - implicit inheritance

# base parent class having a method called implicit
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

# child class inherits the implicit method from parent class
class Child(Parent):
    pass

# creating a dad instance of Parent class
dad = Parent()
# creating a son instance of Child class
son = Child()

dad.implicit()
# the son is a child class. Remember that the child class does
# not have the implicit method. However, we can call this method
# because it inherits this method from the parent class. In this
# way it is obvious (implicit) that the child will inherit all the
# features of the parent class
son.implicit()
