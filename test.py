def count_positives(arr):
    sum = 0
    for index, item in enumerate(arr):
        if item > 0:
            sum = sum + 1
    arr[-1] = sum
    return print(arr)

count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])


# def count_positives(arr):
#     sum = 0
#     for i in arr:
#         print(i)
#         if i > 0:
#             sum += 1
#     arr[-1] = sum
#     return arr

# print(count_positives([1,6,-4,-2,-7,-2]))