import math
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".

# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie(a_list):
    for a in range(0, len(a_list), 1):
        if a_list[a] > 0:
            a_list[a] = "big"
    return a_list

test_a_list = [-1, 3, 5, -5]
print(biggie(test_a_list))

# Count Positives - Given a list of numbers, create a function to replace the last value with the 
# number of positive values. (Note that zero is not considered to be a positive number).

# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(b_list):
    count = 0
    for b in range(0, len(b_list), 1):
        if b_list[b] > 0:
            count += 1
    b_list[-1] = count
    return b_list 

test_b_list = [1,6,-4,-2,-7,-2]
print(count_positives(test_b_list))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(c_list):
    sum = 0
    for c in range(0, len(c_list), 1):
        sum += c_list[c]
    return sum

test_c_list = [6,3,-2]
print(sum_total(test_c_list))

# Average - Create a function that takes a list and returns the average of all the values.

# Example: average([1,2,3,4]) should return 2.5

def average(d_list):
    sum = 0
    for d in range(0, len(d_list), 1):
        sum += d_list[d]
    average = sum/len(d_list)
    return average

test_d_list = [1,2,3,4]
print(average(test_d_list))

# Length - Create a function that takes a list and returns the length of the list.

# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(e_list):
    return len(e_list)

test_e_list = [37,2,1,-9]
print(length(test_e_list))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.

# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(f_list):
    if len(f_list) > 0:
        min = f_list[0]
        for f in range(1, len(f_list), 1):
            if f_list[f] < min:
                min = f_list[f]
    else:
        return False
    return min

test_f_list = [37,2,1,-9]
print(minimum(test_f_list))


# Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.

# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(g_list):
    if len(g_list) > 0:
        max = g_list[0]
        for g in range(0, len(g_list), 1):
            if g_list[g] > max:
                max = g_list[g]
        return max
    else:
        return False

test_g_list = [37,2,1,-9]
print(maximum(test_g_list))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has 
# the sumTotal, average, minimum, maximum and length of the list.

# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(h_list):
    new_dict = {}
    sumTotal = 0
    minimum = h_list[0]
    maximum = h_list[0]
    for h in range(0, len(h_list), 1):
        sumTotal += h_list[h]
        if h_list[h] < minimum:
            minimum = h_list[h]
        if h_list[h] > maximum:
            maximum = h_list[h]
    average = sumTotal/len(h_list)
    new_dict.update({'sumTotal': sumTotal})
    new_dict.update({'average': average})
    new_dict.update({'minimum': minimum})
    new_dict.update({'maximum': maximum})
    new_dict.update({'length': len(h_list)})
    return new_dict

test_h_list = [37,2,1,-9]
print(ultimate_analysis(test_h_list))


# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(i_list):
    length = len(i_list)
    half_length = math.floor(length/2)
    for i in range(0, half_length, 1):
        i_list[i], i_list[length-(1+i)] = i_list[length-(1+i)], i_list[i]
    return i_list

test_i_list = [37,2,1,-9]
print(reverse_list(test_i_list))

