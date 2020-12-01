# Loop
for x in range(0, 10, 1):
    print (x)

# Loop through list
my_list = [1,2,4,6,8]
for x in range(0, len(my_list)):
    print(x, my_list[x])

for v in my_list:
    print(v)

# Loop through dictionary
my_dict = {"name": "John", "age": 40, "height": 178}
for k in my_dict:
    print (k, my_dict[k])

for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

for random_variable in my_dict.values():
    print(random_variable)

for key, val in my_dict.items():
    print(key, " = ", val)

# While Loops
count = 0
while count <5:
    print("looping - ", count)
    count+=1

y = 3
while y > 0:
    print(y)
    y = y-1
else:
    print("final else statement")

# Breaks
for val in 'string':
    if val == 'i':
        break
    print(val)

y = 3
while y >0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:
    print("final else statement")

# Continue
for val in 'string':
    if val == 'i':
        continue
    print(val)


