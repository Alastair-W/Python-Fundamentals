# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. 
# (x[1][0]) = 15
# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name'] = 'Bryant'
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
#OR
# for x in range(0, len(sports_directory['soccer']), 1):
#     if sports_directory['soccer'][x] == 'Messi':
#             sports_directory['soccer'][x] = 'Andres'
# print(sports_directory)

# Change the value 20 in z to 30
# z[0]['y'] = 20
# print(z)
# OR
# for i in range(0, len(z[0]), 1):
#     if i == 20:
#         i = 30
# print (z)


# Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# print(len(students), len(students[0]))

# def iterateDictionary(students):
#     for i in students:
#         print(f'first_name - ', i['first_name']+",", 'last_name - ', i['last_name'])
        
# iterateDictionary(students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

# def iterateDictionary2(input, students):
#     for i in range(0, len(students), 1):
#         print(students[i][input])
    
# iterateDictionary2('last_name', students)



dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list.

def printInfo(dict):
    for k in dict:
        print()
        print(len(dict[k]), k.upper())
        for v in range(0, len(dict[k]), 1):
            print(dict[k][v])

printInfo(dojo)

