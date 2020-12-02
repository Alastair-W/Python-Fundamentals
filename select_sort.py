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



