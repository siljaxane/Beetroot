# Write a Python program to access a function inside a function (Tips: use function, which returns another function)


# ********************************************************************************************************************

def fivers(x):
    return 5 * 5 * x

def sixers(y):
    def resulting_func(x):
        return y(y(x))

    return resulting_func

result = sixers(fivers)
print(result(5))

