sort_arr = [21,233,12,5,8,7,4]

def select_sort(sort_arr):
    for j in range(len(sort_arr)):
        for x in range(j, len(sort_arr)):
            min_num = sort_arr[j]
            # print("Min Num ", min_num)
            # print("Value ", sort_arr[x])
            if sort_arr[x] < sort_arr[j]:
                sort_arr[x], sort_arr[j] = sort_arr[j], sort_arr[x]
    return sort_arr

print (select_sort(sort_arr))


# Alternative from Coding Dojo Solution

# my_arr = [-64, 25, -12, 22, 11] 
  
# for i in range(len(my_arr)): 
#     min_idx = i 
#     for j in range(i+1, len(my_arr)): 
#         if my_arr[min_idx] > my_arr[j]: 
#             min_idx = j
#     temp = my_arr[i]
#     my_arr[i] = my_arr[min_idx]
#     my_arr[min_idx] = temp

# print(my_arr)   
