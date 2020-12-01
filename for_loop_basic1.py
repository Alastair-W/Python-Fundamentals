# Basic - Print all integers from 0 to 150
for basic in range(0, 151, 1):
    print(basic)

# Multiples of Five - Print all the multiples of 5 from 1000
for m in range(5, 1001, 5):
    print(m)

# Counting, The Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range(1, 100, 1):
    if  y % 10 == 0:
        print ('Coding Dojo')
    elif y % 5 == 0:
        print ('Coding')
    else:
        print(y)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for odd in range(1, 500000, 2):
    print(odd)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for pos in range(2018, 0, -4):
    print(pos)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for q in range(lowNum, highNum+1, 1):
    if(q % 3 == 0):
        print (q)