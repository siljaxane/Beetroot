# TASK 1
# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError

try:
    IndexError
except:
    print("This is an IndexError")


def oops1():
    pass

try:
    def oops():
        raise IndexError
except: print("Oopsi daisy")


########## With Key error##########
def oops():
    raise KeyError

try:
    KeyError
except:
    print("This is an KeyError")


def oops1():
    pass

try:
    def oops():
        raise KeyError
except: print("Oopsi daisy")


# TASK 2
# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
# and if value b was zero (cannot divide by zero).    

def TwoNumbers(a, b):
    return 



# Hi. You just need to name function arguments as a  and b and do math operation on them.

a = []
b =[]
c = a + b

[c*c / b]