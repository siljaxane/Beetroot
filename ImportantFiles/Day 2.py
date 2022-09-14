Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
(see open()).b
SyntaxError: invalid syntax. Perhaps you forgot a comma?
(see open()).'b'
SyntaxError: invalid syntax. Perhaps you forgot a comma?
see.open().b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    see.open().b
NameError: name 'see' is not defined. Did you mean: 'set'?
with open ('workfile') as f:
    read_data = f.read()

    
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    with open ('workfile') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'workfile'
f = open('workfile', 'w')
with open ('workfile') as f:
    read_data = f.read()

    
f.closed
True


class Person:
    def greet(self):
        print("Hello, I'm Voldemort")

        
person1 = Person()
print(person1.name)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(person1.name)
AttributeError: 'Person' object has no attribute 'name'














pip
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    pip
NameError: name 'pip' is not defined. Did you mean: 'zip'?
$ pip install -U Flask

SyntaxError: invalid syntax


pip install -U Flask

SyntaxError: invalid syntax. Perhaps you forgot a comma?

$ python --version
SyntaxError: invalid syntax
python --version
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    python --version
NameError: name 'python' is not defined
version
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    version
NameError: name 'version' is not defined. Did you mean: 'Person'?



















# measuee some strings:
words = ['rocket', 'Moon', 'Mars']
for w in words:
    print(w , len(w))

    
rocket 6
Moon 4
Mars 4
words_2 = ['letter', 'computer', 'drink']
for e in words_2:
    print(e, len(e))

    
letter 6
computer 8
drink 5



individuals = {'Pluto': 'active', 'Goofy': 'inactive', 'Sofie': 'active'}

for individual, status in individuals.copy().items():
    if status == 'inactive':
        del individuals[individual]

        
active_users = {}
for individual, status in individuals.items():
    if status == 'active':
        active_individuals[individual] = status

        
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    active_individuals[individual] = status
NameError: name 'active_individuals' is not defined



list(range(5, 10))
[5, 6, 7, 8, 9]
list(range(68, 150))

[68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]




a = ['Mike', 'Harry', 'Olle', 'Christmas', ' New York']
for i in range(len(a)):
    print(i, a[i])

    
0 Mike
1 Harry
2 Olle
3 Christmas
4  New York
b = ['This is a sentence in a list']
for i in range(len(b[i]))
SyntaxError: expected ':'
for i in range(len(b)):
    print(i, b[i])

    
0 This is a sentence in a list
for i in range(100):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
sum(range(10))
45
str.center(10[, fillchar])
SyntaxError: invalid syntax
str.center(10[ fillchar])
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    str.center(10[ fillchar])
NameError: name 'fillchar' is not defined
str.center(width[10])
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    str.center(width[10])
NameError: name 'width' is not defined
g = ["What a lovely evening"]
print(g(str.expandtabs(tabsize=5))

      )
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print(g(str.expandtabs(tabsize=5))
TypeError: unbound method str.expandtabs() needs an argument
str.expandtabs(tabsize=5)
          
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    str.expandtabs(tabsize=5)
TypeError: unbound method str.expandtabs() needs an argument
str.expandtabs(g, tabsize=5)
          
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str.expandtabs(g, tabsize=5)
TypeError: descriptor 'expandtabs' for 'str' objects doesn't apply to a 'list' object

h = "This is great"
          
str.expandtabs(h, tabsize=5)
          
'This is great'
str.expandtabs(h, tabsize=15)
          
'This is great'
J = "Great day"
          
K = "Awesome room"
          
L = "Lovely computer"
          
P = J+K+L
          
str.expandtabs(P, tabsize=15)
          
'Great dayAwesome roomLovely computer'
# Instead of creating 4 strings to use the 'str.expandtabs' method/string formatting, you can do the following:
          
"Great\Awesome\Apple\Spacex\Family\Green" .expandtabs(100)
          
'Great\\Awesome\\Apple\\Spacex\\Family\\Green'
"Great\Awesome\Apple\Spacex\Family\Green" .expandtabs()

'Great\\Awesome\\Apple\\Spacex\\Family\\Green'
"Great\tAwesome\tApple\tSpacex\tFamily\tGreen" .expandtabs(100)
          
'Great                                                                                               Awesome                                                                                             Apple                                                                                               Spacex                                                                                              Family                                                                                              Green'
"Great\tAwesome\tApple\tSpacex\tFamily\tGreen" .expandtabs(15)
          
'Great          Awesome        Apple          Spacex         Family         Green'



# So what you see above, is applying several strings into one pair of "", and seperating the strings by '\t' method >>> one\tstring
          

'one\tstring' .expandtabs(12)
          
'one         string'

# Initially, the 'str.expandtabs()' already says that you can apply the actual string to the 'str' part of the method. And applying multiple strings into the 'str' place is done by using the '\t' method!!
          

# 'sub' stands for 'substring'!
          

"Elon" in "Spacex was started by Elon Musk and today run by himself as well"
          
True



# The 'str.format()' is great and useful, where you can use it as following:
          

"Silja has been depressed for somewhat {} weeks and she is looking to find answeres that will eventually ease and remove the depression" .format(3)
          
'Silja has been depressed for somewhat 3 weeks and she is looking to find answeres that will eventually ease and remove the depression'



print("%(language)s has %(number)03d quote types." % {"language": "Python", "number": 2})
          
Python has 002 quote types.
# The above is a given 'format % values' (where format is a string), % conversion specifications in format are replaced with zero or more elements of values.
          

# So the above print statement is a string with modulo (%) >>> will ask help from Sergey!
          

file = open("sample.bin", "wb")
file. write(b"This binary string will be written to sample.bin")
file
          

open file
          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
open, file
          
(<built-in function open>, <_io.BufferedWriter name='sample.bin'>)




==================== RESTART: Shell ====================



# Below is me fixing HW#7, task 2.
          

def make_country(name, capital):
    my_dict = {'name': name, 'capital': capital}
    print(my_dict)

    
make_country_('Sweden', 'Stockholm')
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    make_country_('Sweden', 'Stockholm')
NameError: name 'make_country_' is not defined. Did you mean: 'make_country'?
make_country('Sweden', 'Stockholm')
{'name': 'Sweden', 'capital': 'Stockholm'}



with open('workfile') as f:
    read_data = f.read()

    
f.closed
True
f.open
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    f.open
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
f.read()
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.


f.readline()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.



f.write('jhjhbfjwefwqefbiwefiwfuwiufwefwefuwbfibbbbf')
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    f.write('jhjhbfjwefwqefbiwefiwfuwiufwefwefuwbfibbbbf')
ValueError: I/O operation on closed file.
