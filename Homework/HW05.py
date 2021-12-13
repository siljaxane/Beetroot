# TASK 1
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

list_1 = []
for i in range(0, 9):
    list_1.append(random.randint(0, 9))

print(max(list_1))


# TASK 2
# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

list1 = [3, 6, 7, 0, 2, 5, 4, 6, 7, 8]
list2 = [2, 4, 6, 7, 8, 1, 3, 4, 5, 5]

list(set(list1).intersection(list2))


# TASK 3
# Make a list that contains all integers from 1 to 100, 
# then find all integers from the list that are divisible by 7 but not a multiple of 5, 
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration.

i = 0

while i < len([1, 101]): 
    list.index(i / 7 != i * 5)
    i += 1


