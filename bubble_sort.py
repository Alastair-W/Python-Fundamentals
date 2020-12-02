unsorted_list = [12,3,6,2,3,5,6,7,8]

def bubble_sort(a_list):
    for j in range(len(a_list)-1):
        # print("Iteration ", j)
        for x in range(len(a_list)-1-j):
            # print()
            # print("Comparing ", a_list[x], a_list[x+1])
            if a_list[x] > a_list[x+1]:
                a_list[x], a_list[x+1] = a_list[x+1], a_list[x]
                # print("Swapped", a_list[x], a_list[x+1])
            # else:
            #     print("No Swap")
    return a_list

print(bubble_sort(unsorted_list))
