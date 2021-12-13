class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

person1 = Person("Voldemort")
print(person1.name)
person1.greet()

person2 = Person("Harry", age=16)
print(person2.name)
person2.greet()
# The "__init__" is a method used to build the class above. Its just a specific construct within Python!

