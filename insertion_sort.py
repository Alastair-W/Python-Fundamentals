new_list = [12,3,6,2,3,5,6,7,8]*400

def insertion_sort(new_list):
    for x in range(1, len(new_list)):
        # print()
        # print("# Evaluated :" ,new_list[x])
        for y in range(x):
            # print("# Compared Against :", new_list[y])
            if new_list[x] < new_list[y]:
                new_list[x], new_list[y] = new_list[y], new_list[x]
                # print("INSERTED")
            # else:
                # print("NO CHANGE")
    return new_list
print("Complete")

insertion_sort(new_list)

#Solution from Coding Dojo
# my_arr = [12,3,6,2,3,5,6,7,8]*400

# def dojo_insert(my_arr):
#     for idx in range(1, len(my_arr)): 
#         temp = my_arr[idx] 
#         prev_idx = idx-1
#         while prev_idx >= 0 and temp < my_arr[prev_idx]: 
#             my_arr[prev_idx + 1] = my_arr[prev_idx] 
#             prev_idx -= 1
#         my_arr[prev_idx + 1] = temp 
#     return my_arr
# print("Complete")

# dojo_insert(my_arr)