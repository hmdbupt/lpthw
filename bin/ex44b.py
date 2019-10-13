# Exercise 44b - Override explicitly
# Sometimes you don't want the child to have a specific features
# that is different from the parent so you create that feature
# in the child class explicitly. This is called overriding and
# this is how we override explicitly.

# parent class with override function
class Parent(object):

    def override(self):
        print("PARENT override()")

# child class with a different override function
class Child(Parent):

    def override(self):
        print("CHILD override()")

# creating a dad instance of Parent class
dad = Parent()
# creating a son instance of Child class
child = Child()

# both override functions will print different things
dad.override()
child.override()
