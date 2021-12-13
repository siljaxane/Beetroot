class Person:
    number_of_persons = 0

    def __init__(self, name, age=22):
        self.name = name
        self.age = age

        Person.number_of_persons += 1
        # or
        # self.number_of_persons += 1

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

    def celebrate_birthday(self):
        self.age = self.age + 1
        # or
        # self.age += 1

        print(f"Today is my birthday! Now, I'm {self.age} years old.")

print("Total persons:", Person.number_of_persons)

person1 = Person("Voldemort")
print(person1.name)
person1.greet()

person2 = Person("Harry", age=16)
print(person2.name)
person2.greet()
# The "__init__" is a method used to build the class above. Its just a specific construct within Python!

person3 = Person("Ken", age=30)
person3.greet()

print('Total persons:', Person.number_of_persons)