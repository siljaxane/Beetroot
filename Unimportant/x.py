Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def make_country(name, capital):
    country_capital = {
        "UK": "London",
        "Sweden": "Stockholm",
        "Finland": "Helsinki",
    }

    
print(make_country)
<function make_country at 0x105111510>
print(country_capital)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(country_capital)
NameError: name 'country_capital' is not defined
print(make_country[name, capital])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(make_country[name, capital])
NameError: name 'name' is not defined



def make_country(name, capital):
    dict1 = {
        "name=Sweden": "capital=Stockholm",
    }

    
print(dict1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
print(make_country)
<function make_country at 0x107252b90>



def make_country(name, capital):
    make_country(dict1 = {
        "name=Sweden": "capital=Stockholm",
    })

    
print(make_country)
<function make_country at 0x107252cb0>
print(dict1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?



def make_country(name, capital):
    make_country(dict = {
        "name=Sweden": "capital=Stockholm",
    })

print(dict)
<class 'dict'>
print(make_country)
<function make_country at 0x107252dd0>





def make_country(name, capital):
    dict1 = {
        "name=Sweden": "capital=Stockholm",
    }
print(dict1)
SyntaxError: invalid syntax
def make_country(name, capital):
    dict1 = {
        "name=Sweden": "capital=Stockholm",
    }
    print(dict1)

    
make_country
<function make_country at 0x107252b90>






================================ RESTART: Shell ================================











def make_country(name, capital):
    print(name + " " + "has " + capital + " as its capital.")

    
make_country({"Sweden": "Stockholm
              
SyntaxError: unterminated string literal (detected at line 1)
make_country({"Sweden": "Stockholm",})
              
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    make_country({"Sweden": "Stockholm",})
TypeError: make_country() missing 1 required positional argument: 'capital'



















def make_country(name, capital):
    print(name + " " + "has " + capital + " as its capital.")

    

make_country({"Sweden": "Stockholm"})
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    make_country({"Sweden": "Stockholm"})
TypeError: make_country() missing 1 required positional argument: 'capital'
make_country({"name=Sweden": "capital=Stockholm"})
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    make_country({"name=Sweden": "capital=Stockholm"})
TypeError: make_country() missing 1 required positional argument: 'capital'
make_country('Sweden', 'Stockholm')
Sweden has Stockholm as its capital.






def make_country(name, capital):
    a_dict = dict(
        name='Sweden'
        capital='Stockholm'
    )
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?

def make_country(name, capital):
    a_dict = dict(
        name='Sweden'
        capital='Stockholm'
    )
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def make_country(name, capital):
    a_dict = dict(
        name='Sweden'
        capital='Stockholm'
    ):
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def make_country(name, capital):
    a_dict = dict(
        name='Sweden',
        capital='Stockholm'
    )
    print(name + " " + "has " + capital + " as its capital.")

print(a_dict)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(a_dict)
NameError: name 'a_dict' is not defined. Did you mean: 'dict'?
def make_country(name, capital):
    a_dict = dict(
        name='Sweden',
        capital='Stockholm'
    )
        print(name + " " + "has " + capital + " as its capital.")
        
SyntaxError: unexpected indent
def make_country(name, capital):
    a_dict = dict(
        name='Sweden',
        capital='Stockholm'
    )
    print(name + " " + "has " + capital + " as its capital.")

    
print(dict)
<class 'dict'>
print(make_country)
<function make_country at 0x101e4add0>
make_country(a_dict)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    make_country(a_dict)
NameError: name 'a_dict' is not defined. Did you mean: 'dict'?
make_country(dict)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    make_country(dict)
TypeError: make_country() missing 1 required positional argument: 'capital'





def make_country(name, capital):
    a_dict = dict(
        name='Sweden',
        capital='Stockholm'
    )
    print(a_dict)

    
a_dict
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a_dict
NameError: name 'a_dict' is not defined. Did you mean: 'dict'?
a_dict[make_country]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a_dict[make_country]
NameError: name 'a_dict' is not defined. Did you mean: 'dict'?
print(make_country(dict(a_dict)))
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print(make_country(dict(a_dict)))
NameError: name 'a_dict' is not defined. Did you mean: 'dict'?
def make_country(name, capital):
    country = {'name': 'Sweden'}
    capital = {'capital': 'Stockholm'}

    
make_country
<function make_country at 0x101e4b0a0>



def make_country(name, capital):
    my_dict = {'name': 'Sweden', 'capital': 'Stockholm'}
    print(my_dict)

    
make_country
<function make_country at 0x101e4ab90>
print(my_dict)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print(my_dict)
NameError: name 'my_dict' is not defined
name
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    name
NameError: name 'name' is not defined
print(make_country['name'])
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print(make_country['name'])
TypeError: 'function' object is not subscriptable
def make_country(name, capital):
    name = {'Sweden'}
    capital = {'Stockholm'}

    
make_country
<function make_country at 0x101e4b250>
