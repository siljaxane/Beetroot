# Inheritance, Task 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, classyear):
        Person.__init__(self, name, age)
        self.classyear = classyear


class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary




student_1 = Student("Mike", 15, 9)
student_2 = Student("Sarah", 11, 5)

print(student_1.name)
print(student_1.age)
print(student_1.classyear)

print(student_2.name)
print(student_2.age)
print(student_2.classyear)

music_teacher = Teacher("Ken", 33, 35000)
math_teacher = Teacher("Annika", 25, 40000)

print(music_teacher.name)
print(music_teacher.age)
print(music_teacher.salary)

print(math_teacher.name)
print(math_teacher.age)
print(math_teacher.salary)



# Inheritance, Task 2

class Mathematician:                                                 
    def square_nums(self, numbers):
        return[n*n for n in numbers] 

# 'Square number for number in the list of numbers.'

m = Mathematician()

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

print(m.square_nums([7, 11, 5, 4]))

# Note to self: Why you want to insert 'n*n for n in numbers' is because nr 1. the task 2 asks for you to get the square number out of...
# list in the print statement. So how you do that is by first understanding how to get a square value of an integer. Simply, '7*7'...
# is getting the square value of the number, 7. But to insert this in the method (aka definition) you can use the 'return' method...
# >again lol< which I have to look into! But, what the code says is: 'n*n', aka could be any number replacing the 'n' - a usual...
# example is to use x, so 'x*x'. So any given number multiplied with itself, 



# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# remove_positives (takes a list of integers and returns it without positive numbers


pn = (+n)
n = (-n)

class Mathematician:                                                 
    def remove_positives(self, numbers):
        for numbers = negative:


    def positive_numbers(self, posNum):
        while posNum != 



m = Mathematician()

print(m.remove_positives([26, -11, -8, 13, -90]))
