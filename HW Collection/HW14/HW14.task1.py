# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# The function, should have a decorator that prints a "decordator version of the function", and not the result of the function.

# accepts another function "func" as an argument
def logger(func):
    def inner(list_of_tuples):      
        return [func(val[0], val[1]) for val in list_of_tuples]      
    return inner

@logger
def add(x, y):
    return x + y 

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add([(4, 5)]))
# so in the print statement above, the list is "nested" in two parantheses, and one bracket, so: ([(X)])
print(square_all([(2, 9), (3, 2)]))