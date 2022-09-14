#Write a Python program to detect the number of local variables declared in a function.

#Tip:
# In a function named func, use the syntax func.variable = value to store value in variable as an attribute of func. 
# To access value outside of func, use func() to run func, then use the syntax function_name.variable to access value.

from collections import Counter


def func():
  func.variable = "John"

func()

print(func.variable)

# ********************************************************************************************************************

items = ["white sock", "blue top", "white sock", "red shirt"]


def func():
    func.variable = items

func()
#The above >> finc() << is crucial for the print outcome.

print(Counter(func.variable))

