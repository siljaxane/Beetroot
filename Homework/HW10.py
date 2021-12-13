# Task 1 below!

# Make a class called Person. 
# Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. 
# Make another method called talk() which makes prints a greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

person1 = Person("Elon", "Musk", 50)

def talk():
    message = ("Hello, my name is ", person1.firstname, " ", person1.lastname, " and I'm ", person1.age, "years old.")


#Task 2 below :)

# Create a class Dog with class attribute `age_factor` equals to 7. 
# Make __init__() which takes values for a dog’s age. 
# Then create a method `human_age` which returns the dog’s age in human equivalent.#


class Dog():
    age_factor = 7
    def __init__(self, age):
        self.age = age

# dogs age in human years, 7 dog years is 50 human years. So 14 dog years is 100 human years. So its approximately 7 human years more than one dog year?

BigDog = Dog(7)

human_age = (BigDog + (BigDog*7))






