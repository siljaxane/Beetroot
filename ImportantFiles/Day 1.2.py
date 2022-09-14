Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
SyntaxError: multiple statements found while compiling a single statement
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    print('The End')

    
0
The End
1
The End
1
The End
2
The End
3
The End
5
The End
8
The End
# On the above, the 'while loop' is executed as long as the statement/condition of (a<10) is true.
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

    
0
1
1
2
3
5
8
# My error in my first attempt under doc 'Day 1' was putting (a, b = a, a+b), which made the loop being '0' endlessly.
#a, b = 0, 1
while a < 10:
    print(a)
    a, b = a, a+b
#

# STRINGS :)

x = 'Mars'
print("It would be great to one day travel to ", x)
It would be great to one day travel to  Mars
person = 'Elon Musk'
print("It would be great to one day travel to", x, " so hopefully", person, " will take us there!")
It would be great to one day travel to Mars  so hopefully Elon Musk  will take us there!
