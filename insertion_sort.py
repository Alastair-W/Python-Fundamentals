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