# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).

# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    new_arr = []
    for i in range(num, -1, -1):
        new_arr.append(i)
    print(new_arr)

countdown(4)

# Print and Return - Create a function that will receive a list with 
# two numbers. Print the first value and return the second.

# Example: print_and_return([1,2]) should print 1 and return 2

def print_ret(a_list):
    if len(a_list) == 2:
        print(a_list[0])
        return a_list[1]
    else:
        return "Error - this function only accepts lists with 2 items"

test_list = [4,77]
print(print_ret(test_list))

# First Plus Length - Create a function that accepts a list and 
# returns the sum of the first value in the list plus the list's length.

# Example: first_plus_length([1,2,3,4,5]) should return 6 
# (first value: 1 + length: 5)

def first_length(fl_list):
    return fl_list[0] + len(fl_list)

fl_array = [10,3,4,5,6,7]
print (first_length(fl_array))


# Values Greater than Second - Write a function that accepts a 
# list and creates a new list containing only the values from 
# the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

# Example: values_greater_than_second([5,2,3,2,1,4]) 
# should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def greater_than(values_list):
    if len(values_list) >= 2:
        small_list = []
        for item in range(0, len(values_list), 1):
            if values_list[item] > 2:
                small_list.append(values_list[item])
    else:
        return False
    print(len(small_list))
    return small_list

example_list = [5,2,3,2,1,4]
print(greater_than(example_list))


# This Length, That Value - Write a function that accepts 
# two integers as parameters: size and value. 
# The function should create and return a list whose length is 
# equal to the given size, and whose values are all the given value.

# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_value(x,y):
    new_list = []
    for i in range(0, x, 1):
        new_list.append(y)
    return new_list

test_new_list = [6,2]
print(length_value(test_new_list[0], test_new_list[1]))