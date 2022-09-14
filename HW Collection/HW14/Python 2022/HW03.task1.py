# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'

# Expected Result : 'held'

# Sample String: 'my'

# Expected Result : 'mymy'

# Sample String: 'x'

# Expected Result: Empty String

#Tips:

#Use built-in function len() on an input string
#Use positive indexing to get the first characters of a string and negative indexing to get the last characters

string1 = "Beige-Universe"

first_two = string1[:2]
last_two = string1[-2:]

oddword = first_two + last_two

if len(oddword) < 2:
    print()

print(oddword)


# len() - Defintion:
# Definition and Usage. The len() function returns the number of items in an object. 
# When the object is a string, the len() function returns the number of characters in the string.
