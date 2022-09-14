Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
python -c command [arg] ...
SyntaxError: invalid syntax. Perhaps you forgot a comma?
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful!")

    
Be careful!
# -*- coding: encoding -*-
# prompt in python is the '>>>' or '...' which is the computer telling you that its ready for instructions.
    # lines without a prompt or that does not begin with one, are outputs from the inpretender.
    
# Comments in python starts with '#'
2 + 2
4
2+2
4
# integer numbers have the type 'int'
# remember that '%' in calculations is for the purpose to tell you the remainer out of for example 17%3 = 2 (how many times does 3 go in 17, the answer to '%' is the amount remaining if any out of how many times 3 fits in 17)
# '=' is used to assign values to variables, and if a variable is not defined in your program when you try to run it, it will give you an error.
# '\' can be used to escape the chosed quotation marks.
'doesn\'t'
"doesn't"
"\"Yes,\" they said."
'"Yes," they said.'
# you may 'escape' unique characters with the backslash symbol.
# '\n' means new line
a = 'First line.\nSecond line.'
a
'First line.\nSecond line.'
print(s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(s)
NameError: name 's' is not defined
print(a)
First line.
Second line.
b = "I like Elon. \nHe does not like me. \nAlthough he inspires me. n\To push and work hard."
print(b)
I like Elon. 
He does not like me. 
Although he inspires me. n\To push and work hard.
# variable 'b' had an error that the interpreter did not mark is that I made a human error, for the last sentence I placed 'n\' instead of '\n'!
# To print a 'raw' string, you place 'r' in your print statement, and before the quotation marks.
print(r"We like sauce {} but still don't")
We like sauce {} but still don't
# 'concatenated' means putting strings together with the '+' (operator) and (repeated) with '*'!
5 * 'Elon' + ' ' + 'Musk'
'ElonElonElonElonElon Musk'
5 * 'Elon' + 5 * ' ' + 5 * 'Elon'
'ElonElonElonElonElon     ElonElonElonElonElon'
# You can place several strings within paranteses and they will connect / be printed in the same statement.
statement = ("We like candy ""and also veggies")
statement
'We like candy and also veggies'
# You cannot have variables named the same!
a_word = "Py"
a_word = "thon"
print(a_word)
thon
a_word + "thon"
'thonthon'
# Get an index from a character in variable
get_index = "Python"
get_index[3]
'h'
# Remmeber that fetching/getting an index is alsways used by []!
# a positive index number fetches the number from the left - a negative idex number (indices) fetches from the right.
get_index[-2]
'o'
# You also use [] for slicing! Ex. [2:0]
word_2 = 'Love'
word[:1] + word[1:]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    word[:1] + word[1:]
NameError: name 'word' is not defined. Did you mean: 'a_word'?
word_2[:1] + word_2[1:]
'Love'
# Se above :)

# Remember that strings are immutable, ie, cannot be changed!
# we have been confused by Sergey using 'len()' in his code, and what it SIMPLY means, is to fetch the lenght of a string.
a_string = "I don't understand Sergey and they way he teaches"
len(a_string)
49
# >>>> testing str() <<<<<


str(a_string)
"I don't understand Sergey and they way he teaches"
str.format(a_string)
"I don't understand Sergey and they way he teaches"
# the 'str.format()' allows you to change something in your string, which is placed between the '()'. Example,

str.capitalize(a_string)
"I don't understand sergey and they way he teaches"
#above string format returns the string with first letter in capital.
"The sum of 1 + 4 is ".format(1+5)
'The sum of 1 + 4 is '
"The sum of 1 + 4 is " .format(1+5)
'The sum of 1 + 4 is '
"The sum of 1 + 4 is ".format(1+4)
'The sum of 1 + 4 is '
print("The sum of 1 + 4 is ".format(1+5))
The sum of 1 + 4 is 
print("The sum of 1 + 4 is {}".format(1+5))
The sum of 1 + 4 is 6
# What we can see above is that the ".format()" is not activated without placing the {} at the end of our string/quation marks.
print("I hate my job and want to change to full time {}".format(programming))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print("I hate my job and want to change to full time {}".format(programming))
NameError: name 'programming' is not defined
job = 'programming'
print("I hate my job and want to change to full time {}".format(job))
I hate my job and want to change to full time programming
time = 'full time'
print("I hate my job and want to change to {}  time programming".format(time))
I hate my job and want to change to full time  time programming
# What we can see above (right above), is that the '{}' can be placed anywhere we want in the string and our defined variable in the format input will be printed and replaced with the {}!


# Lists are "comma seperated values, in square brackets"
# The values in the lists are also called, Items!
a_list = [1, 2, 3, 4, 5]
a_list[1]
2
a_list[:2]
[1, 2]
a_list + [6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2_list = ["A lot of letters"]
SyntaxError: invalid decimal literal
second_list = ["A lot of letters"]
second_list + [" but not enough words"]
['A lot of letters', ' but not enough words']
third_list = [testing without quotations]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
third_list = [testing without quotations,]

SyntaxError: invalid syntax. Perhaps you forgot a comma?

# A note regarding lists, if the item(s) are to be sentences and letters and words, then use quotation marks!
fourth_list = ["I need to create a new vision in my life"]
len(fourth_list)
1
# So for the above (fourth_list), why your 'len()' gave the result of '1', is because you only had one (1) item in your assigned list. if you use 'len()' for lists, the reult will be on the x amount of items.


# Below is something I just copied over from Python tutorial 3.2
a, b = 0, 1
while a < 10:
    print(a)
    a, b = a, a+b

    
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
l0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0l
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0