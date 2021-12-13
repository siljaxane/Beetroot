# TASK 1
# Make a program that has some sentence (a string) on input and returns a dict 
# containing all unique words as keys and the number of occurrences as values. 

from typing import Union


a_string = "Something to say"

a_string = {
    'Somthing': 1,
    'to': 1,
    'say': 1
}

print(a_string)




# TASK 2
# Input data:

#stock = {
    #"banana": 6,
    #"apple": 0,
    #"orange": 32,
    #"pear": 15
#}
#prices = {
    #"banana": 4,
    #"apple": 2,
    #"orange": 1.5,
    #"pear": 3
#}

# Create a function which takes as input two dicts with structure mentioned above, 
# then computes and returns the total price of stock.

def Stockvalue(stock, prices):
    
    #while Stockvalue == (stock, {}) * (prices, {}):

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }

    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    return[stock*prices]


    #return[stock*prices for total in function]
    #(f"Total value of following stock:", {}) 

get_total = ((stock, {})*(prices, {}))

print(Stockvalue ['apple'])
# return((stock, {}) * (prices, {}))




# TASK 3
# Use a list comprehension to make a list 
# containing tuples (i, j) where `i` goes from 1 to 10 
# and `j` is corresponding to `i` squared.

i = (1, 10)
j = ()
a_tuple = (i, j)

for i in a_tuple:
    print(range(10), [i*i for j in i])




