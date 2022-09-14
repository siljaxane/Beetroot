# Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
# If all nums inside the list are positive, execute the first function on that list and return the result of it. 
# Otherwise, return the result of the second one
# ********************************************************************************************************************
# A tip: Look for built-in-functions

#def choose_func(number, func1, func2):
######    # A Simple soultion
#####    is_all_positive = True
####   for number in numbers:
###        if number < 0:
 ###           is_all_positive = False
 #           break

    #if is_all_positive:
        #return func1(numbers)

    #return func2(numbers)

    # Example using the "min()" built-in-function
    #is_all_positive = min(numbers) >= 0

    # Using the "all()" function
    # is_all_positive = all([number >= 0 for number in numbers])

    #if is_all_positive:
        #return func1(numbers)

    #return func2(numbers)


def choose_func(numbers, func1, func2):
    is_all_positive = min(numbers) >= 0
    if is_all_positive:
        return func1(numbers)

    return func2(numbers)

def square_nums(nums):

    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]
    

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

print (choose_func(nums1, square_nums, remove_negatives)) == [1, 4, 9, 16, 25]

print (choose_func(nums2, square_nums, remove_negatives)) == [1, 3, 5]